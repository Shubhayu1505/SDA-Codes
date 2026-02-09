from abc import ABC, abstractmethod

class Coffee(ABC):
    @abstractmethod
    def get_cost(self) -> float:
        pass
    
    @abstractmethod
    def get_description(self) -> str:
        pass

class BasicCoffee(Coffee):
    def get_cost(self) -> float:
        return 5.0
    
    def get_description(self) -> str:
        return "Basic Coffee"

class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee
    
    def get_cost(self) -> float:
        return self._coffee.get_cost()
    
    def get_description(self) -> str:
        return self._coffee.get_description()

class MilkDecorator(CoffeeDecorator):
    def get_cost(self) -> float:
        return self._coffee.get_cost() + 1.5
    
    def get_description(self) -> str:
        return self._coffee.get_description() + ", Milk"

class SugarDecorator(CoffeeDecorator):
    def get_cost(self) -> float:
        return self._coffee.get_cost() + 0.5
    
    def get_description(self) -> str:
        return self._coffee.get_description() + ", Sugar"

class ChocolateDecorator(CoffeeDecorator):
    def get_cost(self) -> float:
        return self._coffee.get_cost() + 2.0
    
    def get_description(self) -> str:
        return self._coffee.get_description() + ", Chocolate"

class CreamDecorator(CoffeeDecorator):
    def get_cost(self) -> float:
        return self._coffee.get_cost() + 1.0
    
    def get_description(self) -> str:
        return self._coffee.get_description() + ", Cream"

if __name__ == "__main__":
    coffee1 = BasicCoffee()
    print("Order 1: " + coffee1.get_description())
    print("Cost: $" + str(coffee1.get_cost()))
    
    coffee2 = MilkDecorator(SugarDecorator(BasicCoffee()))
    print("\nOrder 2: " + coffee2.get_description())
    print("Cost: $" + str(coffee2.get_cost()))
    
    coffee3 = ChocolateDecorator(MilkDecorator(SugarDecorator(BasicCoffee())))
    print("\nOrder 3: " + coffee3.get_description())
    print("Cost: $" + str(coffee3.get_cost()))
    
    coffee4 = CreamDecorator(ChocolateDecorator(MilkDecorator(BasicCoffee())))
    print("\nOrder 4: " + coffee4.get_description())
    print("Cost: $" + str(coffee4.get_cost()))
    
    coffee5 = SugarDecorator(SugarDecorator(MilkDecorator(BasicCoffee())))
    print("\nOrder 5: " + coffee5.get_description())
    print("Cost: $" + str(coffee5.get_cost()))
