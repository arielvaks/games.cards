from strings.games.deckofcards import Deckofcards
from strings.games.player import Player
# from strings.games.card import Card


class Cardgame:
    # מאתחל את המשחק קלפים
    def __init__(self, player1, player2, number_of_cards_for_all_players = 10):
        if type(number_of_cards_for_all_players) == int:
            if 0 < number_of_cards_for_all_players <= 26:
                self.number_of_cards_for_all_players = number_of_cards_for_all_players
            else:
                self.number_of_cards_for_all_players = 10
        else:
            self.number_of_cards_for_all_players = 10
            print("next time enter a number")
        if type(player1) == str:
            pass
        else:
            raise ValueError("please enter an str")
        if type(player2) == str:
            pass
        else:
            raise ValueError("please enter an str")

        self.deck_of_cards = Deckofcards()
        self.player1 = Player(player1, self.number_of_cards_for_all_players)
        self.player2 = Player(player2, self.number_of_cards_for_all_players)
        self.start_game = False
        self.new_game()
        self.start_game = True

    #מגדיר את השחקנים ומערבב את החפיסה
    def new_game(self):
        if self.start_game == False:
            self.deck_of_cards.shuffle()
            self.player1.set_hand(self.deck_of_cards)
            self.player2.set_hand(self.deck_of_cards)
        else:
            raise ValueError("you cant call new_game again")

    #מתודה שמחזירה את המנצח
    def get_winner(self):
        if self.player1.number_of_cards > self.player2.number_of_cards:
            return self.player2.name
        elif self.player2.number_of_cards > self.player1.number_of_cards:
            return self.player1.name
        else:
            return None


# gamenumber1=Cardgame("ariel","dolfin","dgrdgrd")
# gamenumber1.player1.show_hand()
# gamenumber1.player2.show_hand()
# gamenumber1.player1.cardsofplayer.pop()
# gamenumber1.player1.numberofcards-=1
#
# gamenumber1.player1.show_hand()
# print("the winner is",gamenumber1.get_winner())