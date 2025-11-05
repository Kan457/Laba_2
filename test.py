import unittest
from file_request import from_my_url
from main import create_login, len_str, front_characters, back_characters, impossible_characters , valid_value , error_dog

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


print("Если вы хотите проверить корректность почты через файл — введите 1")
print("Если вы хотите проверить корректность почты через ввод с консоли — введите 2")
print("Если вы хотите проверить корректность почты через ввод с сайта — введите 3")
message = input("Введите выбор: ")

if message == "1": # Проверка через файл
    try:
        with open('testing_file.txt', 'r', encoding='utf-8') as f:
            data = [line.strip() for line in f.readlines()]
        print("Файл успешно считан ")

    except FileNotFoundError:
        print("Ошибка: файл не найден.")


    unittest.main()

elif message == "2":# Проверка через консоль

    text = input("Введите почту: ")
    data = text.split()


    unittest.main()
elif message == "3":# Проверка с сайта
    data = from_my_url('https://gist.github.com/Kan457/589b69ca0c16d69116487aeb92f2cb9d/raw')
    
    unittest.main()

else:
    print("Некорректный ввод. Попробу")

if __name__ == "__main__":
    pass



