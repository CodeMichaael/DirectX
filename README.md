# DirectX
Simple tool that  helps you manage files and folders, allowing you to create, delete, read, and write files, as well as create and navigate directories, with built-in error handling.

# Examples (For each file)

**File Manager Examples**

```py
from file import FileManager

file_manager = FileManager()

# Write content to a file
file_manager.write_content("my_file.txt", "Hello, world!")

# Write content to a file in a specific directory
file_manager.write_content("my_file.txt", "Hello, world!", "/path/to/your/directory")

# Read content from a file
content = file_manager.read_content("my_file.txt")

# Read content from a file in a specific directory
content_from_directory = file_manager.read_content("my_file.txt", "/path/to/your/directory")

# Get size of a file
size_in_kilobytes, size_in_bytes = file_manager.get_size("my_file.txt")

# Get size of a file from a specific directory
size_from_directory_in_kilobytes, size_from_directory_in_bytes = file_manager.get_size("my_file.txt", "/path/to/your/directory")

# Get creation date of a file
creation_date = file_manager.get_creation_date("my_file.txt")

# Get creation date of a file from a specific directory
creation_date_from_directory = file_manager.get_creation_date("my_file.txt", "/path/to/your/directory")
```

**Directory Manager Examples**
```py
from directory import DirectoryManager

directory_manager = DirectoryManager()

# Create a directory
directory_manager.create_directory("my_directory")

# Get the current directory
current_directory = directory_manager.current_directory()

# Set the directory
directory_manager.set_directory("/path/to/your/directory")

# List contents of a directory
contents = directory_manager.list_contents("/path/to/your/directory")

# Delete a directory
directory_manager.delete_directory("my_directory")
```

**System Manager Examples**
```py
from filesystem import SystemManager

system_manager = SystemManager()

# Create a file
system_manager.create_file("my_file.txt")

# Create a file in a specific directory
system_manager.create_file("my_file.txt", "/path/to/your/directory")

# Delete a file
system_manager.delete_file("my_file.txt", None)

# Delete a file from a specific directory
system_manager.delete_file("my_file.txt", "/path/to/your/directory")
```
