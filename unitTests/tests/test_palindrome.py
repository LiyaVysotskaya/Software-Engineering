import unittest
from src.palindrome import is_palindrome

class TestIsPalindrome(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(is_palindrome("radar"))
        self.assertTrue(is_palindrome("level"))
        self.assertTrue(is_palindrome("а роза упала на лапу азора"))
    
    def test_non_palindrome(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("world"))
        self.assertFalse(is_palindrome("example"))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

    def test_single_character(self):
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome("1"))

if __name__ == "__main__":
    result = unittest.TextTestRunner().run(unittest.makeSuite(TestIsPalindrome))
    if result.wasSuccessful():
        print("YES")
    else:
        print("NO")
