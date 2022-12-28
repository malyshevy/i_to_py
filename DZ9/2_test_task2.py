import unittest
from task2 import big_number


class test_task2(unittest.TestCase):
    # Тест на False
    def test_assertFalse(self):
        self.assertFalse(big_number('0'))


# Запуск через консоль
if __name__ == "__main__":
    unittest.main()
