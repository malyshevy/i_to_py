import unittest
from task5 import a


class test_task4(unittest.TestCase):
    # Тест на a не в b
    def test_assertNotIn(self):
        self.assertNotIn(a[0], [10])


# Запуск через консоль
if __name__ == "__main__":
    unittest.main()
