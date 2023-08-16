import unittest
from unittest.mock import patch, mock_open
from your_module import SystemManager
from colorama import Fore
import os

class TestSystemManager(unittest.TestCase):

    def setUp(self):
        self.system_manager = SystemManager()

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.join", return_value="test_file.txt")
    def test_create_file(self, mock_join, mock_open):
        self.system_manager.create_file("test_file.txt")
        mock_open.assert_called_with("test_file.txt", "w")
        
        self.system_manager.create_file("test_file.txt", "test_directory")
        mock_join.assert_called_with("test_directory", "test_file.txt")
        mock_open.assert_called_with("test_directory/test_file.txt", "w")

    @patch("os.remove")
    @patch("os.path.join", return_value="test_file.txt")
    def test_delete_file(self, mock_join, mock_remove):
        self.system_manager.delete_file("test_file.txt")
        mock_remove.assert_called_with("test_file.txt")
        
        self.system_manager.delete_file("test_file.txt", "test_directory")
        mock_join.assert_called_with("test_directory", "test_file.txt")
        mock_remove.assert_called_with("test_directory/test_file.txt")

if __name__ == "__main__":
    unittest.main()
