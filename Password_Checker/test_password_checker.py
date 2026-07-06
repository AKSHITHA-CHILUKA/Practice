import unittest

from password_checker import validate_password


class TestValidatePassword(unittest.TestCase):
    def test_valid_password(self):
        self.assertTrue(validate_password("ValidPass1!"))

    def test_too_short_password(self):
        self.assertFalse(validate_password("Aa1!a"))

    def test_too_long_password(self):
        self.assertFalse(validate_password("VeryLongPassword1!VeryLong"))

    def test_missing_digit(self):
        self.assertFalse(validate_password("ValidPass!"))

    def test_missing_uppercase(self):
        self.assertFalse(validate_password("validpass1!"))

    def test_missing_lowercase(self):
        self.assertFalse(validate_password("VALIDPASS1!"))

    def test_missing_special_character(self):
        self.assertFalse(validate_password("ValidPass12"))


if __name__ == "__main__":
    unittest.main()