import unittest
from task2 import big_number


class test_task2(unittest.TestCase):
    # Тест на True
    def test_assertTrue(self):
        self.assertTrue(big_number('123'))


# Запуск через консоль
if __name__ == "__main__":
    unittest.main()