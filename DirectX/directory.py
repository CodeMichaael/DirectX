import os
from typing import Optional
from colorama import Fore
import shutil

class DirectoryManager:

    def create_directory(self, name: str):
        try:
            os.mkdir(name)
            print(f"{Fore.GREEN}(File Action): Successfully created directory {name}")
        except OSError as e:
            print(f"{Fore.RED}(Error): Unable to create directory {name}. Error: {e}")

    def current_directory(self, directory: str):
        current_directory = os.getcwd()
        return current_directory

    def set_directory(self, directory_path: str):
        try:
            os.chdir(directory_path)
        except OSError as e:
            print(f"{Fore.RED}(Error): Unable to set directory. Error: {e}")
    
    def list_contents(self, directory_path: str):
        try:
            result = os.listdir(directory_path)
            return result
        except OSError as e:
            return "Unable to list contents."

    def delete_directory(self, directory_path: str):
        try:
            shutil.rmtree(directory_path)
            print(f"{Fore.GREEN} Successfully deleted directory.")
        except OSError as e:
            print(f"{Fore.RED}(Error): Unable to delete directory. Error: {e}")

            



    
