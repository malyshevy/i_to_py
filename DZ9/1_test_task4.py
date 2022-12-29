import unittest
import task4


class test_task4(unittest.TestCase):
    # Тест на a является None
    def test_assertIsNone(self):
        task4.my_string = None
        rec = task4.my_string
        self.assertIsNone(rec)


# Запуск через консоль
if __name__ == "__main__":
    unittest.main()
