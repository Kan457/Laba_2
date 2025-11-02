import re

def valid_login(login : str)->bool:
    valid = r'^(?![._-])(?!.*[._-]{2})[A-Za-z0-9._-]{8,16}(?![._-])@[A-Za-z0-9-]+\.(com|org|net|mail.ru|info|biz|io|edu|gov)$'
    return bool(re.match(valid,login))

def create_login(text):
    if valid_login(text)==True:
        print("Логин подходит по шаблону")
        return text
    else:
        print("Ошибка! Логин не подходит")

text = input("Введите логин: ")    
create_login(text)
