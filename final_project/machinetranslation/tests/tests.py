import unittest
from translator import english_to_french, french_to_english

class TestEnglishFunction(unittest.TestCase):
    def test_english(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertEqual(english_to_french("What's your name"), "Quel est votre nom")
        self.assertNotEqual(english_to_french("Bonjour"), "Hello")

class TestFrenchFunction(unittest.TestCase):
    def test_french(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english("Quel est votre nom"), "What's your name")
        self.assertNotEqual(french_to_english("Hello"), "Bonjour")
if __name__ == "__main__":
    unittest.main()