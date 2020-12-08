from unittest import TestCase
from strings.games.player import Player
from strings.games.deckofcards import Deckofcards
from strings.games.card import Card


class TestPlayer(TestCase):

	def setUp(self):
		pass

	def test__init__(self):
		#בודק מקרה שבו מכניסים שם שלא מסוג מחרוזת
		test_player = Player(3, 15)
		self.assertEqual(type(test_player.name), str)

		#בודק מקרה שבו מכניסים מספר קלפים גדול מ-26
		test_player = Player('eran', 27)
		self.assertEqual(test_player.number_of_cards, 26)

		# בדיקה כאשר מספר הקלפים הוא 26 קצה
		test_player = Player('eran', 26)
		self.assertEqual(test_player.number_of_cards, 26)

		# בודק מקרה שבו מכניסים מספר קלפים קטן או שווה ל-0
		test_player = Player('eran', 0)
		self.assertEqual(test_player.number_of_cards, 10)

		# בדיקה כאשר מספר הקלפים הוא 1 קצה
		test_player = Player('eran', 1)
		self.assertEqual(test_player.number_of_cards, 1)

		#בודק כאשר מזינים ערכים תקינים
		test_player = Player('eran', 15)
		self.assertEqual(test_player.number_of_cards, 15)

		#בודק כאשר מזינים מספר קלפים לא מסוג אינט
		with self.assertRaises(ValueError):
			test_player = Player('eran', 'abc')


	def test_set_hand(self):
		#בודק שמספר הקלפים שהשחקן יקבל בעזרת המתודה הזאת שווה למספר שהוגדר לו
		hafisa = Deckofcards()
		test_player = Player("jhonny")
		test_player.set_hand(hafisa)
		self.assertEqual(len(test_player.cards_of_player), test_player.number_of_cards)
		#בודק האם הקלפים שהשחקן קיבל כבר לא בחפיסה שממנה הוא לקח את הקלפים
		for i in test_player.cards_of_player:
			self.assertNotIn(i, hafisa.cards)

	def test_show_hand(self):
		pass

	def test_get_card(self):
		#בודק מה קורה כאשר אין לשחקן קלפים
		test_player = Player("jhonny")
		with self.assertRaises(ValueError):
			test_player.get_card()

		#בודק האם המתודה מחזירה לי קלף שנמצא אצל השחקן. תפקודה התקין
		hafisa = Deckofcards()
		test_player.set_hand(hafisa)
		self.assertIn(test_player.get_card(), test_player.cards_of_player)

	def test_add_card(self):
		#בודקים שהמתודה הוסיפה את הקלף לרשימה של השחקן
		test_player = Player("ariel")
		test = Card(1, 2)
		test_player.add_card(test)
		self.assertIn(test, test_player.cards_of_player)

		#בודקים מה קורה כאשר נותנים כפרמטר משהו לא מסוג קלף
		with self.assertRaises(ValueError):
			test_player.add_card(3)

		# בודקים שהמתודה מעלה את המספר קלפים של השחקן באחד כאשר זה הוספנו קלף חוקי
		hafisa = test_player.number_of_cards
		test_player.add_card(Card(2, 2))
		self.assertEqual(test_player.number_of_cards, hafisa + 1)