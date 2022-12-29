import unittest
import task4


class test_task4(unittest.TestCase):
    # Тест на a не является None
    def test_assertIsNotNone(self):
        task4.my_string = 1
        rec = task4.my_string
        self.assertIsNotNone(rec)


# Запуск через консоль
if __name__ == "__main__":
    unittest.main()