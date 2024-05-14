import unittest
from history_handler import HistoryHandler
import os

class TestHistoryHandler(unittest.TestCase):
    def setUp(self):
        # Reset the singleton instance before each test
        HistoryHandler._instance = None

    def test_singleton(self):
        handler1 = HistoryHandler("test_history.txt")
        handler2 = HistoryHandler("test_history.txt")
        self.assertIs(handler1, handler2)

    def test_read_history(self):
        handler = HistoryHandler("test_history.txt")
        self.assertEqual(handler.read_history(), [])

    def test_write_history(self):
        handler = HistoryHandler("test_history.txt")
        handler.write_history("Test conversion")
        with open("test_history.txt", "r") as file:
            self.assertEqual(file.read(), "Test conversion\n")

    def test_history_persistence(self):
        handler1 = HistoryHandler("test_history.txt")
        handler1.write_history("First conversion")
        handler2 = HistoryHandler("test_history.txt")
        self.assertEqual(handler2.read_history(), ["First conversion\n"])

    def tearDown(self):
        # Clean up the test file after each test
        if os.path.exists("test_history.txt"):
            os.remove("test_history.txt")

if __name__ == "__main__":
    unittest.main()
