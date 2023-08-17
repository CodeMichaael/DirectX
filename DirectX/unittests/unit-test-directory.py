import unittest
from unittest.mock import patch
from your_module import DirectoryManager
from colorama import Fore

class TestDirectoryManager(unittest.TestCase):

    def setUp(self):
        self.dir_manager = DirectoryManager()

    def test_create_directory(self):
        with patch("os.mkdir") as mock_mkdir:
            self.dir_manager.create_directory("test_dir")
            mock_mkdir.assert_called_with("test_dir")

    def test_current_directory(self):
        with patch("os.getcwd") as mock_getcwd:
            mock_getcwd.return_value = "/path/to/directory"
            result = self.dir_manager.current_directory()
            self.assertEqual(result, "/path/to/directory")

    def test_set_directory(self):
        with patch("os.chdir") as mock_chdir:
            self.dir_manager.set_directory("new_dir")
            mock_chdir.assert_called_with("new_dir")

    def test_list_contents(self):
        with patch("os.listdir") as mock_listdir:
            mock_listdir.return_value = ["file1.txt", "file2.txt"]
            result = self.dir_manager.list_contents(".")
            self.assertEqual(result, ["file1.txt", "file2.txt"])

    def test_delete_directory(self):
        with patch("shutil.rmtree") as mock_rmtree:
            self.dir_manager.delete_directory("test_dir")
            mock_rmtree.assert_called_with("test_dir")

if __name__ == "__main__":
    unittest.main()
