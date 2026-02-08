from abc import ABC, abstractmethod
from typing import List

class FileSystemComponent(ABC):
    @abstractmethod
    def show_details(self, indent: int = 0) -> None:
        pass
    
    @abstractmethod
    def get_size(self) -> int:
        pass

class File(FileSystemComponent):
    def __init__(self, name: str, size: int):
        self.name = name
        self._size = size
    
    def show_details(self, indent: int = 0) -> None:
        print("  " * indent + "File: " + self.name + " (" + str(self._size) + " KB)")
    
    def get_size(self) -> int:
        return self._size

class Directory(FileSystemComponent):
    def __init__(self, name: str):
        self.name = name
        self.children = []
    
    def add(self, component):
        self.children.append(component)
    
    def remove(self, component):
        self.children.remove(component)
    
    def show_details(self, indent: int = 0) -> None:
        total_size = self.get_size()
        print("  " * indent + "Directory: " + self.name + " (" + str(total_size) + " KB)")
        for child in self.children:
            child.show_details(indent + 1)
    
    def get_size(self) -> int:
        total = 0
        for child in self.children:
            total += child.get_size()
        return total

if __name__ == "__main__":
    file1 = File("resume.pdf", 200)
    file2 = File("photo.png", 1500)
    file3 = File("notes.txt", 50)
    file4 = File("report.doc", 300)
    file5 = File("movie.mp4", 5000)
    
    root = Directory("MyComputer")
    documents = Directory("Documents")
    pictures = Directory("Pictures")
    videos = Directory("Videos")
    
    documents.add(file1)
    documents.add(file3)
    documents.add(file4)
    
    pictures.add(file2)
    
    videos.add(file5)
    
    root.add(documents)
    root.add(pictures)
    root.add(videos)
    
    print("File System Structure:")
    print("----------------------")
    root.show_details()
    
    print("\nSize Information:")
    print("File 'resume.pdf': " + str(file1.get_size()) + " KB")
    print("Directory 'Documents': " + str(documents.get_size()) + " KB")
    print("Total size: " + str(root.get_size()) + " KB")
