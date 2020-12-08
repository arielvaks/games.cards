class Card:
	# מאתחל את הקלף
	def __init__(self, a = 0, b = 0):
		list_of_numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]
		list_of_types = ["diamond", "spade", "heart", "club"]
		if type(a) == int and type(b) == int and 0 < a <= 13 and 0 < b <= 4:
			self.value = list_of_numbers[a-1]
			self.suit = list_of_types[b-1]
			self.value_of_value = a
			self.value_of_suit = b
		else:
			raise ValueError("please enter right parameters")

	#מחזיר את הערכים של הקלף
	def __str__(self):
		return f"{self.value},{self.suit}"

	# אומר האם קלף גדול יותר מקלף אחר
	def __gt__(self, card):
		if self.value_of_value > card.value_of_value:
			return True
		if self.value_of_value < card.value_of_value:
			return False
		if self.value_of_value == card.value_of_value:
			if self.value_of_suit > card.value_of_suit:
				return True
			if self.value_of_suit < card.value_of_suit:
				return False
			else:
				return False

	#בודק האם קלף שווה לקלף אחר
	def __eq__(self, card):
		if self.value_of_value == card.value_of_value and self.value_of_suit == card.value_of_suit:
			return True
		else:
			return False