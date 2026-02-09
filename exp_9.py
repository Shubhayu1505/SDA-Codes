from abc import ABC, abstractmethod
from typing import List

class Mediator(ABC):
    @abstractmethod
    def send_message(self, message: str, sender: 'User'):
        pass

class User(ABC):
    def __init__(self, name: str, mediator: Mediator):
        self.name = name
        self.mediator = mediator
    
    @abstractmethod
    def send(self, message: str):
        pass
    
    @abstractmethod
    def receive(self, message: str):
        pass

class ChatUser(User):
    def send(self, message: str):
        print(f"{self.name} sends: {message}")
        self.mediator.send_message(message, self)
    
    def receive(self, message: str):
        print(f"{self.name} receives: {message}")

class ChatMediator(Mediator):
    def __init__(self):
        self.users: List[User] = []
    
    def add_user(self, user: User):
        self.users.append(user)
    
    def send_message(self, message: str, sender: User):
        for user in self.users:
            if user != sender:
                user.receive(f"From {sender.name}: {message}")

class AuctionMediator(Mediator):
    def __init__(self):
        self.bidders: List[User] = []
        self.highest_bid = 0
        self.highest_bidder = None
    
    def add_bidder(self, bidder: User):
        self.bidders.append(bidder)
    
    def send_message(self, message: str, sender: User):
        try:
            bid_amount = int(message)
            if bid_amount > self.highest_bid:
                old_highest = self.highest_bidder.name if self.highest_bidder else "None"
                self.highest_bid = bid_amount
                self.highest_bidder = sender
                
                for bidder in self.bidders:
                    if bidder != sender:
                        bidder.receive(f"New highest bid: ${bid_amount} by {sender.name} (was ${self.highest_bid} by {old_highest})")
            else:
                sender.receive(f"Bid rejected: ${bid_amount} is not higher than current highest: ${self.highest_bid}")
        except ValueError:
            for bidder in self.bidders:
                if bidder != sender:
                    bidder.receive(f"{sender.name}: {message}")

class Bidder(User):
    def send(self, message: str):
        self.mediator.send_message(message, self)
    
    def receive(self, message: str):
        print(f"Bidder {self.name}: {message}")

if __name__ == "__main__":
    print("=== Chat Room Example ===")
    chat_mediator = ChatMediator()
    
    alice = ChatUser("Alice", chat_mediator)
    bob = ChatUser("Bob", chat_mediator)
    charlie = ChatUser("Charlie", chat_mediator)
    
    chat_mediator.add_user(alice)
    chat_mediator.add_user(bob)
    chat_mediator.add_user(charlie)
    
    alice.send("Hello everyone!")
    bob.send("Hi Alice!")
    charlie.send("Good morning!")
    
    print("\n=== Auction Example ===")
    auction_mediator = AuctionMediator()
    
    bidder1 = Bidder("John", auction_mediator)
    bidder2 = Bidder("Sarah", auction_mediator)
    bidder3 = Bidder("Mike", auction_mediator)
    
    auction_mediator.add_bidder(bidder1)
    auction_mediator.add_bidder(bidder2)
    auction_mediator.add_bidder(bidder3)
    
    print("\nStarting auction for vintage car...")
    bidder1.send("1000")
    bidder2.send("1500")
    bidder3.send("1200")
    bidder2.send("2000")
    bidder1.send("1800")
    
    print("\n=== Traffic Control Example ===")
    class TrafficLightMediator(Mediator):
        def __init__(self):
            self.vehicles = []
        
        def add_vehicle(self, vehicle: User):
            self.vehicles.append(vehicle)
        
        def send_message(self, message: str, sender: User):
            if message == "RED":
                for vehicle in self.vehicles:
                    if vehicle != sender:
                        vehicle.receive("Stop: Traffic light is red")
            elif message == "GREEN":
                for vehicle in self.vehicles:
                    if vehicle != sender:
                        vehicle.receive("Go: Traffic light is green")
    
    class Vehicle(User):
        def send(self, message: str):
            self.mediator.send_message(message, self)
        
        def receive(self, message: str):
            print(f"Vehicle {self.name}: {message}")
    
    traffic_mediator = TrafficLightMediator()
    car1 = Vehicle("Car1", traffic_mediator)
    car2 = Vehicle("Car2", traffic_mediator)
    truck = Vehicle("Truck", traffic_mediator)
    
    traffic_mediator.add_vehicle(car1)
    traffic_mediator.add_vehicle(car2)
    traffic_mediator.add_vehicle(truck)
    
    car1.send("RED")
    car2.send("GREEN")
