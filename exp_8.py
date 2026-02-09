from abc import ABC, abstractmethod
from typing import List, Any

class Iterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        pass
    
    @abstractmethod
    def next(self) -> Any:
        pass

class BookCollection:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def get_forward_iterator(self):
        return ForwardIterator(self)
    
    def get_reverse_iterator(self):
        return ReverseIterator(self)

class ForwardIterator(Iterator):
    def __init__(self, collection):
        self.collection = collection
        self.index = 0
    
    def has_next(self) -> bool:
        return self.index < len(self.collection.books)
    
    def next(self) -> Any:
        if self.has_next():
            book = self.collection.books[self.index]
            self.index += 1
            return book
        return None

class ReverseIterator(Iterator):
    def __init__(self, collection):
        self.collection = collection
        self.index = len(self.collection.books) - 1
    
    def has_next(self) -> bool:
        return self.index >= 0
    
    def next(self) -> Any:
        if self.has_next():
            book = self.collection.books[self.index]
            self.index -= 1
            return book
        return None

class StudentList:
    def __init__(self):
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)
    
    def get_iterator(self):
        return ListIterator(self)

class ListIterator(Iterator):
    def __init__(self, collection):
        self.collection = collection
        self.index = 0
    
    def has_next(self) -> bool:
        return self.index < len(self.collection.students)
    
    def next(self) -> Any:
        if self.has_next():
            student = self.collection.students[self.index]
            self.index += 1
            return student
        return None

if __name__ == "__main__":
    print("=== Book Collection Example ===")
    library = BookCollection()
    library.add_book("Python Programming")
    library.add_book("Data Structures")
    library.add_book("Algorithms")
    library.add_book("Machine Learning")
    library.add_book("Database Systems")
    
    print("\nForward Traversal:")
    forward_iter = library.get_forward_iterator()
    while forward_iter.has_next():
        print(forward_iter.next())
    
    print("\nReverse Traversal:")
    reverse_iter = library.get_reverse_iterator()
    while reverse_iter.has_next():
        print(reverse_iter.next())
    
    print("\n=== Student List Example ===")
    students = StudentList()
    students.add_student("Alice")
    students.add_student("Bob")
    students.add_student("Charlie")
    students.add_student("David")
    students.add_student("Eve")
    
    print("\nStudent List:")
    student_iter = students.get_iterator()
    while student_iter.has_next():
        print(student_iter.next())
    
    print("\n=== Multiple Simultaneous Iterators ===")
    print("\nTwo independent forward iterators:")
    iter1 = library.get_forward_iterator()
    iter2 = library.get_forward_iterator()
    
    print("Iterator 1 first two books:")
    print(iter1.next())
    print(iter1.next())
    
    print("\nIterator 2 all books:")
    while iter2.has_next():
        print(iter2.next())
