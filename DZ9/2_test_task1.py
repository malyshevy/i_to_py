import unittest
from task1 import hour_min_sec


class test_task1(unittest.TestCase):
    # Тест на !=
    def test_assertNotEqual(self):
        self.assertNotEqual(hour_min_sec(3661), [0, 0, 1])


# Запуск через консоль
if __name__ == "__main__":
    unittest.main()
