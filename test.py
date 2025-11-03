import unittest
from main import create_login, len_str, front_characters, back_characters, impossible_characters , valid_value , error_dog

text = input("Введите почту : ")
data=text.split()

class MailTest(unittest.TestCase):

    def test_error_dog(self):
        for text in data:
            assert error_dog(text) is True

    def test_len_str(self):
        for text in data:
            assert len_str(text) is True

    def test_front_characters(self):
        for text in data:
            assert front_characters(text) is True

    def test_back_characters(self):
        for text in data:
            assert back_characters(text) is True

    def test_impossible_characters(self):
        for text in data:
            assert impossible_characters(text) is True

    def test_valid_value(self):
        for text in data:
            assert valid_value(text) is True

class RegularTest(unittest.TestCase):
    
    def test_create_login(self):
        for text in data:
            assert create_login(text) is True

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(MailTest))
    suite.addTest(unittest.makeSuite(RegularTest))
    runner = unittest.TextTestRunner()
    runner.run(suite)