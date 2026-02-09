from abc import ABC, abstractmethod

class Visitor(ABC):
    @abstractmethod
    def visit_book(self, book):
        pass
    
    @abstractmethod
    def visit_mobile(self, mobile):
        pass
    
    @abstractmethod
    def visit_saree(self, saree):
        pass

class Item(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class Book(Item):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def accept(self, visitor):
        return visitor.visit_book(self)

class Mobile(Item):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def accept(self, visitor):
        return visitor.visit_mobile(self)

class Saree(Item):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def accept(self, visitor):
        return visitor.visit_saree(self)

class PriceVisitor(Visitor):
    def __init__(self):
        self.total = 0
    
    def visit_book(self, book):
        self.total += book.price
        return book.price
    
    def visit_mobile(self, mobile):
        self.total += mobile.price
        return mobile.price
    
    def visit_saree(self, saree):
        self.total += saree.price
        return saree.price

class TaxVisitor(Visitor):
    def visit_book(self, book):
        return book.price * 0.05
    
    def visit_mobile(self, mobile):
        return mobile.price * 0.18
    
    def visit_saree(self, saree):
        return saree.price * 0.12

class DiscountVisitor(Visitor):
    def visit_book(self, book):
        return book.price * 0.10
    
    def visit_mobile(self, mobile):
        return mobile.price * 0.15
    
    def visit_saree(self, saree):
        return saree.price * 0.20

if __name__ == "__main__":
    items = [
        Book("Ramayana", 500),
        Mobile("Smartphone", 15000),
        Saree("Silk Saree", 3000),
        Book("Mahabharata", 600),
        Mobile("Tablet", 8000)
    ]
    
    print("=== Shopping Cart ===")
    for item in items:
        print(f"{type(item).__name__}: {item.name} - Rs.{item.price}")
    
    price_visitor = PriceVisitor()
    for item in items:
        item.accept(price_visitor)
    print(f"\nTotal Price: Rs.{price_visitor.total}")
    
    tax_visitor = TaxVisitor()
    total_tax = 0
    for item in items:
        tax = item.accept(tax_visitor)
        total_tax += tax
    print(f"Total Tax: Rs.{total_tax:.2f}")
    
    discount_visitor = DiscountVisitor()
    total_discount = 0
    for item in items:
        discount = item.accept(discount_visitor)
        total_discount += discount
    print(f"Total Discount: Rs.{total_discount:.2f}")
    
    print(f"\nFinal Amount: Rs.{price_visitor.total + total_tax - total_discount:.2f}")
