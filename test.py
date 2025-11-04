import unittest
from main import create_login, len_str, front_characters, back_characters, impossible_characters , valid_value , error_dog
import unittest

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

while True:
    print("Если вы хотите проверить корректность почты через файл — введите 1")
    print("Если вы хотите проверить корректность почты через ввод с консоли — введите 2")
    print("Если вы хотите выйти — введите 0")

    message = input("Введите выбор: ")

    if message == "1":
        # Проверка через файл
        with open('testing_file.txt', 'r', encoding='utf-8') as f:
            data = [line.strip() for line in f.readlines()]


        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(MailTest))
        suite.addTest(unittest.makeSuite(RegularTest))
        runner = unittest.TextTestRunner()
        runner.run(suite)

    elif message == "2":
        # Проверка через консоль
        text = input("Введите почту: ")
        data = text.split()


        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(MailTest))
        suite.addTest(unittest.makeSuite(RegularTest))
        runner = unittest.TextTestRunner()
        runner.run(suite)

    elif message == "0":
        print("Выход из программы.")
        break

    else:
        print("Некорректный ввод. Попробуйте снова.")



