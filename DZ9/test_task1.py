import unittest
from task1 import hour_min_sec


class test_task1(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    # Тест на ==
    def test_assertEqual(self):
        self.assertEqual(hour_min_sec(3661), [1, 1, 1])


# Запуск через консоль
if __name__ == "__main__":
    unittest.main()
