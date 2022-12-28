import unittest
from task3 import func_out_user


class test_task3(unittest.TestCase):
    # Тест на a является b
    def test_assertIs(self):
        rec = func_out_user('Sancho', 'Panso', '1870', 'Marokko', '', '')
        self.assertIs(rec['name'], 'Sancho')


# Запуск через консоль
if __name__ == "__main__":
    unittest.main()
