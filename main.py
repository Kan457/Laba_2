import re
valid = re.compile(r'(?![._-])(?!.*[._-]{2})[A-Za-z0-9._-]{6,18}(?<![._-])@[A-Za-z0-9-]+\.(com|org|net|ru|info|biz|io|edu|gov)')

def check(text):
    return bool(re.search(valid,text))

def error_dog(text):
    if text.count("@")>1:
        return False
    else:
        return True

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
        return False  # ошибка длины

def front_characters(text):#недопустимые символы в начале
    if ('-' not in text[0]) and ('.' not in text[0]) and ('_' not in text[0]):
        return True
    else:
        return False 

def back_characters(text):#недопустимые символы в конце
    index = text.rfind("@")
    if ('-' not in text[index-1]) and ('.' not in text[index-1]) and ('_' not in text[index-1]):
        return True
    else:
        return False  
    
def impossible_characters(text):#недопустимые повторения
    if ('--' not in text) and ('..' not in text) and ('__' not in text):
        return True
    else:
        return False  
    
def valid_value(text):#недопустимые значения
    allowed = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@._-"
    for ch in text:
        if ch not in allowed:
            return False 
    return True


def create_login(text):
    if check(text)==True:
        return True
    else:
        return False
        

if __name__ == "__main__":
    pass