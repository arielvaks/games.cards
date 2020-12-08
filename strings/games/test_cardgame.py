from unittest import TestCase
from strings.games.cardgame import Cardgame
# from strings.games.card import Card
# from strings.games.deckofcards import Deckofcards
# from strings.games.player import Player


class TestCardgame(TestCase):
	def test__init(self):
		#בדיקה כאשר כל הפרמטרים שהוזנו חוקיים
		test_card_game = Cardgame('dolfin', 'ariel', 5)
		self.assertEqual(test_card_game.player1.number_of_cards, 5)
		self.assertEqual(test_card_game.player2.number_of_cards, 5)

		#בדיקה כאשר מזינים שם של שחקן במשתנה שאינו מסוג סטרינג
		with self.assertRaises(ValueError):
			test_card_game = Cardgame(1, 'ariel', 5)

		with self.assertRaises(ValueError):
			test_card_game = Cardgame('dolfin', 1, 5)

		#בדיקה כאשר מזינים מספר חלוקה של קלפים מסוג משתנה שאינו אינט
		test_card_game = Cardgame('dolfin', 'ariel', 'hello')
		self.assertEqual(test_card_game.number_of_cards_for_all_players, 10)

		#בדיקה כאשר מספר הקלפים מסוג אינט אבל גדול מ-26 או קטן שווה ל-0
		test_card_game = Cardgame('dolfin', 'ariel', 800)
		self.assertEqual(test_card_game.number_of_cards_for_all_players, 10)

		test_card_game = Cardgame('dolfin', 'ariel', 0)
		self.assertEqual(test_card_game.number_of_cards_for_all_players, 10)

		#מקרה קצה כאשר שווה 1
		test_card_game = Cardgame('dolfin', 'ariel', 1)
		self.assertEqual(test_card_game.number_of_cards_for_all_players, 1)

		# מקרה קצה כאשר שווה 26
		test_card_game = Cardgame('dolfin', 'ariel', 26)
		self.assertEqual(test_card_game.number_of_cards_for_all_players, 26)

		#בדיקה כאשר לא מזינים צספר קלפים בכלל
		test_card_game = Cardgame('dolfin', 'ariel')
		self.assertEqual(test_card_game.number_of_cards_for_all_players, 10)

	def test_new_game(self):
		#בדיקה שהתוכנית מוציאה שגיאה במידה ומפעילים את המתודה עוד פעם
		test_card_game = Cardgame('dolfin', 'ariel', 5)
		with self.assertRaises(ValueError):
			test_card_game.new_game()

	def test_get_winner(self):
		# בדיקה כאשר מספר הקלפים זהה אצל 2 השחקנים
		test_card_game = Cardgame('dolfin', 'ariel', 5)
		self.assertEqual(test_card_game.get_winner(),  None)

		#בדיקה כאשר המנצח הוא שחקן מספר 1
		test_card_game.player1.number_of_cards -= 1
		self.assertEqual(test_card_game.get_winner(), test_card_game.player1.name)

		# בדיקה כאשר המנצח הוא שחקן מספר 2
		test_card_game.player2.number_of_cards -= 2
		self.assertEqual(test_card_game.get_winner(), test_card_game.player2.name)