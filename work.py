import re
def check(text):
    valid = r'^(?![._-])(?!.*[._-]{2})[A-Za-z0-9._-]{6,18}(?![._-])@[A-Za-z0-9-]+\.(com|org|net|ru|info|biz|io|edu|gov)$'
    return bool(re.match(valid,text))

def create_login():
    text = input("Введите имя почты: ")
    if check(text)==True:
        print("Логин подходит по шаблону")
        return 0
    else:
        print("Ошибка! Логин не подходит")
        return create_login()
    
create_login()
