import re
def check(text):
    valid = r'^(?![._-])(?!.*[._-]{2})[A-Za-z0-9._-]{6,18}(?![._-])@[A-Za-z0-9-]+\.(com|org|net|ru|info|biz|io|edu|gov)$'
    return bool(re.match(valid,text))

def error_dog(text):
    if text.count("@")>1:
        print("Ошибка @")
        return False

def len_str(variable):#ошибка длинны
    count = 0
    if variable.count("@")>1:
        index = variable.rfind("@")
        for i in range(index):
            count+=1
    else:
        for i in range(len(variable)):
            if variable[i] != '@':
                count += 1
            else:
                break

    if 6 < count < 18:
        return True
    else:
        print("Ошибка длинны")
        return False  # ошибка длины

def front_characters(text):#недопустимые символы в начале
    if ('-' not in text[0]) and ('.' not in text[0]) and ('_' not in text[0]):
        return True
    else:
        print("Ошибка первого символа")
        return False  # ошибка 1-го символа

def back_characters(text):#недопустимые символы в конце
    if ('-' not in text[-1]) and ('.' not in text[-1]) and ('_' not in text[-1]):
        return True
    else:
        print("Ошибка последнего символа")
        return False  # ошибка последнего символа
    
def impossible_characters(text):#недопустимые повторения
    if ('--' not in text) and ('..' not in text) and ('__' not in text):
        return True
    else:
        print("Ошибка здвоения спец. символов")
        return False  # ошибка задвоение спец символа
    
def valid_value(text):#недопустимые значения
    allowed = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@._-"
    for ch in text:
        if ch not in allowed:
            print("Ошибка некорректных символов")
            return False # ошибка неизвестного символа
    return True


def create_login(text):
    if check(text)==True:
        return True
    else:
        return False
        

if __name__ == "__main__":
    pass