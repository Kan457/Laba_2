import unittest
from main import create_login
text = 'lisa434@mail.ru'
create_login(text)
def test_valid_postal_code():
    assert create_login(text) is True

def test_postal_code_with_letters():
    assert create_login(text) is False

def test_short_postal_code():
    assert create_login(text) is False

def test_long_postal_code():
   assert create_login(text) is False

if __name__ == "__main__":
    unittest.main()
