import unittest
from main import create_login  

# Ввод пользователя остаётся — как ты хотел
text = input("Введите логин: ")
req = create_login(text)
class TestAdd(unittest.TestCase):  
    
    def test_add_positive(self):
        self.assertEqual(req, 0) 

    def test_len_str(self):
        self.assertEqual(req, 1)  

    def test_front_characters(self):
        self.assertEqual(req, 2) 

    def test_back_characters(self):  
        self.assertEqual(req, 3)  

    def test_impossible_characters(self): 
        self.assertEqual(req, 4)  

    def test_valid_value(self):  
        self.assertEqual(req, 5) 

if __name__ == "__main__":
    unittest.main()
