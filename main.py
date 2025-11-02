import re
def check(text):
    valid = r'^(?![._-])(?!.*[._-]{2})[A-Za-z0-9._-]{6,18}(?![._-])@[A-Za-z0-9-]+\.(com|org|net|ru|info|biz|io|edu|gov)$'
    return bool(re.match(valid,text))

def len_str(variable):#ошибка длинны
    count = 0
    for i in range(len(variable)):
        if variable[i] != '@':
            count += 1
        else:
            break

    if 6 < count < 18:
        print("длинна норм")
        return 0  
    else:
        print("Ошибка длинны")
        return 1  # ошибка длины

def front_characters(text):#недопустимые символы в начале
    if ('-' not in text[0]) and ('.' not in text[0]) and ('_' not in text[0]):
        return 0
    else:
        print("Ошибка первого символа")
        return 2  # ошибка 1-го символа

def back_characters(text):#недопустимые символы в конце
    if ('-' not in text[-1]) and ('.' not in text[-1]) and ('_' not in text[-1]):
        return 0
    else:
        print("Ошибка последнего символа")
        return 3  # ошибка последнего символа
    
def impossible_characters(text):#недопустимые повторения
    if ('--' not in text) and ('..' not in text) and ('__' not in text):
        return 0
    else:
        print("Ошибка здвоения спец. символов")
        return 4  # ошибка задвоение спец символа
    
def valid_value(text):#недопустимые значения
    allowed = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789._@-"
    for ch in text:
        if ch not in allowed:
            print("Ошибка некорректных символов")
            return 5 # ошибка неизвестного символа
    return 0

def choose_error(text):
        request1 = len_str(text)
        request2 = front_characters(text)
        request3 = back_characters(text)
        request4 = impossible_characters(text)
        request5 = valid_value(text)
        if request1!=0:
            return request1
        else:
            if request2!=0:
                return request2
            else:
                if request3!=0:
                    request3
                else:
                    if request4!=0:
                        request4
                    else:
                        if request5!=0:
                            request5

def create_login(text):
    if check(text)==True:
        print("Логин подходит по шаблону")
        return 0
    else:
        print("Ошибка! Логин не подходит")
        return choose_error(text)
if __name__ == "__main__":
    pass