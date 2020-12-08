from strings.games.cardgame import Cardgame
# from strings.games.card import Card
# from strings.games.player import Player
# import random
# from strings.games.deckofcards import Deckofcards

game_number = Cardgame("ariel", "dolfin","DHRTD")
print(game_number.player1.name)
game_number.player1.show_hand()
print("")
print(game_number.player2.name)
game_number.player2.show_hand()
print("")

for i in range(10):
    card1 = game_number.player1.get_card()
    card2 = game_number.player2.get_card()
    if card1 > card2:
        game_number.player2.add_card(card1)
        game_number.player1.cards_of_player.remove(card1)
        game_number.player1.number_of_cards -= 1
        print("the card that lost is ", card2)
        print("the winner is", game_number.player1.name)
    else:
        game_number.player1.add_card(card1)
        game_number.player2.cards_of_player.remove(card2)
        game_number.player2.number_of_cards -= 1
        print("the card that lost is", card1)
        print("the winner is", game_number.player2.name)

print("")
print("the winner of the game  is ", game_number.get_winner())
print("")
game_number.player1.show_hand()
game_number.player2.show_hand()