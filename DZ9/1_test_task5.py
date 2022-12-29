import unittest
from task5 import a


class test_task5(unittest.TestCase):
    # Тест на a в b
    def test_assertIn(self):
        self.assertIn(a[0], [10, 15, 20])


# Запуск через консоль
if __name__ == "__main__":
    unittest.main()
