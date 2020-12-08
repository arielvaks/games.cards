from unittest import TestCase
from strings.games.card import Card


class TestCard(TestCase):

	def setUp(self):
		self.a = Card(1, 2)

	def test_init(self):
	# בודק מקרים שבהם מכניסים ערכים לא נכונים לאתחול של קלף
	# ערך שלילי לוואליו
		with self.assertRaises(ValueError):
			test_illegal_card = Card(-1, 2)

	#ערך לא תקין לסוג הקלף
		with self.assertRaises(ValueError):
			test_illegal_card = Card(-1, 0)

	#ערך סטרינגי לסוג
		with self.assertRaises(ValueError):
			test_illegal_card = Card(-1, "bla bla")

	#כאשר לא ניתן קלף בכלל
		with self.assertRaises(ValueError):
			test_illegal_card = Card()

	#כאשר מכניסים קלף תקין
	#בדיקת קצה תחתון של ערך וסוג
		test_legal_card = Card(1, 1)
		self.assertEqual(test_legal_card.value, "2")
		self.assertEqual(test_legal_card.suit, "diamond")
	#בדיקת קצה עליון של ערך וסוג
		test_legal_card = Card(13, 4)
		self.assertEqual(test_legal_card.value, "ace")
		self.assertEqual(test_legal_card.suit, "club")

	def test_str(self):
		#בודק שהמתודה מדפיסה את הערכים הנכונים
		test_proper_values = Card(3, 2)
		self.assertEqual(test_proper_values.__str__(), "4,spade")

		#בדיקת ערך קצה גבוה
		test_biggest_card = Card(13, 4)
		self.assertEqual(test_biggest_card.__str__(), "ace,club")

		#בדיקת ערך קצה מינמלי
		test_smallest_card = Card(1, 1)
		self.assertEqual(test_smallest_card.__str__(), "2,diamond")

	def test__gt__(self):
		#בודק שהמתודה מחזירה את הקלף היותר גדול
		test_equal_card = Card(1, 2)
		test_smaller_card = Card(1, 1)
		test_bigger_and_proper_card = Card(11, 4)

		#כאשר קלף 1 קטן מהשני
		self.assertFalse(test_smaller_card > self.a)

		#כאשר קלף אחד שווה לשני
		self.assertFalse(self.a > test_equal_card)

		#כאשר קלף אחד גדול מהשני
		self.assertTrue(test_bigger_and_proper_card > self.a)

	def test__eq__(self):
		#בודק שהמתודה משווה בין קלפים
		#כאשר הקלפים שווים
		test_equal_card = Card(1, 2)
		self.assertEqual(test_equal_card, self.a)

		#כאשר הקלפים לא שווים
		test_not_equal_card = Card(7, 2)
		self.assertNotEqual(test_not_equal_card, self.a)