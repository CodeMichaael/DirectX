from colorama import Fore
from typing import Optional

class SystemManager:

    def create_file(self, name: str, to_directory: Optional[str] = None) -> None:
        if to_directory is None:
            try:
                with open(file_path "w") as f:
                    pass
                    print(f"{Fore.GREEN}(File Action): Successfully created {file_path}")
            except OSError as e:
                print(f"{Fore.RED}(Error): Could not create {file_path}. Error: {e}")

        elif to_directory is not None:
            try:
                full_file_path = os.path.join(to_directory or "", file_path)
                with open(full_file_path, "w") as f:
                    pass
                    print(f"{Fore.GREEN}(File Action): Successfully created {full_file_path}")
            except OSError as e:
                print(f"{Fore.RED}(Error): Could not create {file_path}. Error: {e}")

    def delete_file(file_path: str, from_directory: Optional[str]) -> None:
        if from_directory is None:
            try:
                os.remove(file_path)
                print(f"{Fore.GREEN}(File Action): Successfully deleted {file_path}")
            except OSError as e:
                print(f"{Fore.RED}(Error): Could not delete {file_path}. Error: {e}")

        elif from_directory is not None:
            try:
                full_file_path = os.path.join(from_directory or "", file_path)
                os.remove(full_file_path)
                print(f"{Fore.GREEN}(File Action): Successfully deleted {full_file_path}")
            except OSError as e:
                print(f"{Fore.RED}(Error): Could not delete {file_path}. Error: {e}")
