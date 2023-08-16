import unittest
from unittest.mock import patch
from your_module import FileManager
from colorama import Fore
import datetime

class TestFileManager(unittest.TestCase):

    def setUp(self):
        self.file_manager = FileManager()

    def test_write_content(self):
        with patch("builtins.open") as mock_open:
            self.file_manager.write_content("test_file.txt", "Hello, world!")
            mock_open.assert_called_with("test_file.txt", "w")
            
    def test_read_content(self):
        with patch("builtins.open") as mock_open:
            mock_open.return_value.__enter__.return_value.read.return_value = "Hello, world!"
            result = self.file_manager.read_content("test_file.txt")
            self.assertEqual(result, "Hello, world!")

    def test_get_size(self):
        with patch("os.path.getsize") as mock_getsize:
            mock_getsize.return_value = 1024  # 1 KB
            size_kb, size_bytes = self.file_manager.get_size("test_file.txt")
            self.assertEqual(size_kb, 1.0)
            self.assertEqual(size_bytes, 1024)

    def test_get_creation_date(self):
        with patch("os.path.getctime") as mock_getctime:
            mock_getctime.return_value = 1678880000  # A timestamp in seconds
            expected_datetime = datetime.datetime.fromtimestamp(1678880000)
            creation_date = self.file_manager.get_creation_date("test_file.txt")
            self.assertEqual(creation_date, expected_datetime)

if __name__ == "__main__":
    unittest.main()
