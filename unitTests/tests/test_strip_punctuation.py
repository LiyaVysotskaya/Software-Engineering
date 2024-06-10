import unittest
from src.strip_punctuation import strip_punctuation_ru

class TestStripPunctuationRU(unittest.TestCase):
    def test_punctuation_removal(self):
        self.assertEqual(strip_punctuation_ru("Привет, мир!"), "Привет мир")
        self.assertEqual(strip_punctuation_ru("Как дела?"), "Как дела")
        self.assertEqual(strip_punctuation_ru("Это тест."), "Это тест")
    
    def test_no_punctuation(self):
        self.assertEqual(strip_punctuation_ru("Привет мир"), "Привет мир")
        self.assertEqual(strip_punctuation_ru("Тест"), "Тест")

    def test_empty_string(self):
        self.assertEqual(strip_punctuation_ru(""), "")
    
    def test_only_punctuation(self):
        self.assertEqual(strip_punctuation_ru("!!!"), "")

if __name__ == "__main__":
    result = unittest.TextTestRunner().run(unittest.makeSuite(TestStripPunctuationRU))
    if result.wasSuccessful():
        print("YES")
    else:
        print("NO")
