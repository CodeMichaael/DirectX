from colorama import Fore
from typing import Optional
import os

class SystemManager:

    def create_file(self, name: str, to_directory: Optional[str] = None) -> None:
        if to_directory is None:
            try:
                with open(name, "w") as f:
                    pass
                    print(f"{Fore.GREEN}(File Action): Successfully created {name}")
            except OSError as e:
                print(f"{Fore.RED}(Error): Could not create {name}. Error: {e}")

        elif to_directory is not None:
            try:
                full_file_path = os.path.join(to_directory or "", name)
                with open(full_file_path, "w") as f:
                    pass
                    print(f"{Fore.GREEN}(File Action): Successfully created {full_file_path}")
            except OSError as e:
                print(f"{Fore.RED}(Error): Could not create {full_file_path}. Error: {e}")

    def delete_file(self, file_path: str, from_directory: Optional[str] = None) -> None:
        if from_directory is None:
            try:
                os.remove(file_path)
                print(f"{Fore.GREEN}(File Action): Successfully deleted {file_path}")
            except OSError as e:
                print(f"{Fore.RED}(Error): Could not delete {file_path}. Error: {e}")
        else:
            try:
                full_file_path = os.path.join(from_directory or "", file_path)
                os.remove(full_file_path)
                print(f"{Fore.GREEN}(File Action): Successfully deleted {full_file_path}")
            except OSError as e:
                print(f"{Fore.RED}(Error): Could not delete {file_path}. Error: {e}")
