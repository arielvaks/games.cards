from unittest import TestCase
from strings.games.deckofcards import Deckofcards


class TestDeckofcards(TestCase):

	#יוצר חפיסה
	def setUp(self):
		self.a = Deckofcards()

	def tearDown(self):
		pass

	def test__init__(self):
		#בדיקה שבאמת נוצרה חפיסה שמכילה 52 קלפים
		self.assertEqual(len(self.a.cards), 52)

	def test_shuffle(self):
		#בדיקה החפיסה מתערבבת באמת
		test = self.a.cards
		self.assertNotEqual(test, self.a.shuffle())

	def test_deal_one(self):
		#בדיקה שבאמת הוצא הקלף האחרון מהרשימה
		the_last_value_to_check = self.a.cards[len(self.a.cards) - 1]
		the_last_value = self.a.deal_one()
		self.assertNotIn(the_last_value, self.a.cards)
		self.assertEqual(the_last_value, the_last_value_to_check)

	def test_show(self):
		pass