import unittest
from src.phone_number import is_correct_mobile_phone_number_ru

class TestIsCorrectMobilePhoneNumberRU(unittest.TestCase):
    def test_valid_numbers(self):
        self.assertTrue(is_correct_mobile_phone_number_ru("8(900)1234567"))
        self.assertTrue(is_correct_mobile_phone_number_ru("+7 900 123 45 67"))
        self.assertTrue(is_correct_mobile_phone_number_ru("+7 900-123-45-67"))
    
    def test_invalid_numbers(self):
        self.assertFalse(is_correct_mobile_phone_number_ru("9001234567"))
        self.assertFalse(is_correct_mobile_phone_number_ru("7 900 123 4567"))
        self.assertFalse(is_correct_mobile_phone_number_ru("+1 900 123 4567"))

if __name__ == "__main__":
    result = unittest.TextTestRunner().run(unittest.makeSuite(TestIsCorrectMobilePhoneNumberRU))
    if result.wasSuccessful():
        print("YES")
    else:
        print("NO")
