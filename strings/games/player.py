import random
from random import randint
from strings.games.card import Card
from strings.games.deckofcards import Deckofcards


class Player:
	#מאתחל את השחקן
	def __init__(self, name, number_of_cards = 10):
		# def_str is variable of str if the name is not str
		def_str = "a" + str(randint(1, 100000000000000))
		# check if the type is str then check if the number of cards is proper
		if type(name) == str:
			self.name = name
		else:
			self.name = def_str
		if type(number_of_cards) == int:
			if number_of_cards > 26:
				self.number_of_cards = 26

			elif number_of_cards <= 0:
				self.number_of_cards = 10

			else:
				self.number_of_cards = number_of_cards

		else:
			raise ValueError("please enter right parameters")
		self.cards_of_player = []

	# מוציא קלפים מחפיסת קלפים ונותן לשחקן
	def set_hand(self, deck_of_cards):
		self.cards_of_player = []
		i = 1
		while i <= self.number_of_cards:

			self.cards_of_player += [deck_of_cards.deal_one()]
			i += 1

	# מראה כמה קלפים נשארו לשחקן
	def show_hand(self):
		print("the cards of ", str(self.name), "is")
		number_of_card = 1
		for i in self.cards_of_player:
			print("card number ", number_of_card)
			print(i)
			number_of_card += 1

	#מתודה שמחזירה קלף רנדומלי ששייך לשחקן
	def get_card(self):
		if self.cards_of_player == []:
			raise ValueError("the list is empty")
		else:
			return random.choice(self.cards_of_player)

	#מתודה שמוסיפה קלף  לשחקן
	def add_card(self, card):
		if isinstance(card, Card):
			self.cards_of_player += [card]
			self.number_of_cards += 1
		else:
			raise ValueError("please enter right parameters")

# ariel = Card(1,2)
# # gilad = Player("gilad")
# #
# # gilad.add_card(ariel)
# # # gilad.show_hand()