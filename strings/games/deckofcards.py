import random
from strings.games.card import Card
# from random import randint


class Deckofcards:

	# מאתחל את החפיסת קלפים
	def __init__(self):
		#מכניס קלפים לרשימה
		self.cards = []
		number1 = 1
		number2 = 1
		while number1 <= 4:
			while number2 <= 13:
				self.cards += [Card(number2, number1)]
				number2 += 1
			number2 = 1
			number1 += 1
		random.shuffle(self.cards)

	# מערבב את החפיסת קלפים
	def shuffle(self):
		random.shuffle(self.cards)

	#מוציא מהחפיסת קלפים קלף אחד
	def deal_one(self):
		return self.cards.pop()

	#מראה כמה קלפים נשארו בחפיסה
	def show(self):
		print("this is the cards that left in the packet")
		for i in self.cards:
			print(i)