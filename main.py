import unittest
from file_request import from_my_url
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