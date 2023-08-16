import os
from typing import Optional, Tuple
from colorama import Fore

class FileManager:
    
    def write_content(self, file_path: str, content: any, to_directory: Optional[str] = None) -> None:
        if to_directory is None:
            try:
                with open(file_path "w") as f:
                    f.write(content)
                    print(f"{Fore.GREEN}(File Action): Successfully written to {file_path}")
            except OSError as e:
                print(f"{Fore.RED}(Error): Could not write to {file_path}. Error: {e}")

        elif to_directory is not None:
            try:
                full_file_path = os.path.join(to_directory or "", file_path)
                with open(full_file_path, "w") as f:
                    f.write(content)
                    print(f"{Fore.GREEN}(File Action): Successfully written to {full_file_path}")
            except OSError as e:
                print(f"{Fore.RED}(Error): Could not write to {file_path}. Error: {e}")

    def read_content(self, file_path: str, from_directory: Optional[str] = None) -> str:
        if from_directory is None:
            try:
                with open(file_path, "r") as f:
                    return f.read()
            except OSError as e:
                print(f"{Fore.RED}(Error): Could not read from {file_path}. Error: {e}")

        elif from_directory is not None:
            try:
                full_file_path = os.path.join(from_directory or "", file_path)
                with open(full_file_path, "r") as f:
                    return f.read()
            except OSError as e:
                print(f"{Fore.RED}(Error): Could not read from {full_file_path}. Error: {e}")

    def get_size(self, file_path: str, from_directory: Optional[str] = None) -> Tuple[float, int]:
        if from_directory is not None:
            full_file_path = os.path.join(from_directory or "", file_path)
        
            try:
                size_in_bytes = os.path.getsize(full_file_path)
                size_in_kilobytes = size_in_bytes / 1024  # Convert bytes to kilobytes
                return size_in_kilobytes, size_in_bytes
            except FileNotFoundError:
                raise ValueError(f"{Fore.RED}(Error): Could not get size from {full_file_path}. Unable to find file.")
        
        elif from_directory is None:
            try:
                size_in_bytes = os.path.getsize(file_path)
                size_in_kilobytes = size_in_bytes / 1024  
                return size_in_kilobytes, size_in_bytes
            except FileNotFoundError:
                raise ValueError(f"{Fore.RED}(Error): Could not get size from {file_path}. Unable to find file.")

    def get_creation_date(self, file_path: str, from_directory: Optional[str] = None):
        if from_directory is not None:
            try:
                full_file_path = os.path.join(from_directory or "", file_path)
                creation_timestamp = os.path.getctime(full_file_path)
                creation_datetime = datetime.datetime.fromtimestamp(creation_timestamp)
                return creation_datetime
            except FileNotFoundError:
                raise ValueError(f"{Fore.RED}(Error): Could not get creation date from {full_file_path}. Unable to find file.")

        elif from_directory is None:
            try:
                creation_timestamp = os.path.getctime(file_path)
                creation_datetime = datetime.datetime.fromtimestamp(creation_timestamp)
                return creation_datetime
            except FileNotFoundError:
                raise ValueError(f"{Fore.RED}(Error): Could not get creation date from {file_path}. Unable to find file.")