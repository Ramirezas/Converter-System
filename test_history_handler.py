import unittest
from history_handler import HistoryHandler
import os

class TestHistoryHandler(unittest.TestCase):
    def test_read_history(self):
        handler = HistoryHandler("test_history.txt")
        self.assertEqual(handler.read_history(), [])

    def test_write_history(self):
        handler = HistoryHandler("test_history.txt")
        handler.write_history("Test conversion")
        with open("test_history.txt", "r") as file:
            self.assertEqual(file.read(), "Test conversion\n")

    def tearDown(self):
        if os.path.exists("test_history.txt"):
            os.remove("test_history.txt")

if __name__ == "__main__":
    unittest.main()