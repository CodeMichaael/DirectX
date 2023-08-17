from directory import DirectoryManager
from file import FileManager
from filesystem import SystemManager

class DirectX(SystemManager, DirectoryManager, FileManager):
    pass