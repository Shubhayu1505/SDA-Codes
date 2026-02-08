from abc import ABC, abstractmethod
from typing import Type, Protocol

# Abstract Products
class Button(ABC):
    @abstractmethod
    def click(self) -> None: 
        """Perform button click action"""
        pass
    
    @abstractmethod
    def render(self) -> None:
        """Render the button visually"""
        pass

class Checkbox(ABC):
    @abstractmethod
    def check(self) -> None: 
        """Perform checkbox check action"""
        pass
    
    @abstractmethod
    def render(self) -> None:
        """Render the checkbox visually"""
        pass

# Concrete Products - Windows Family
class WinButton(Button):
    def click(self) -> None: 
        print("Windows Button clicked")
    
    def render(self) -> None:
        print("Rendering Windows-style button")

class WinCheckbox(Checkbox):
    def check(self) -> None: 
        print("Windows Checkbox checked")
    
    def render(self) -> None:
        print("Rendering Windows-style checkbox")

# Concrete Products - Mac Family
class MacButton(Button):
    def click(self) -> None: 
        print("Mac Button clicked")
    
    def render(self) -> None:
        print("Rendering macOS-style button")

class MacCheckbox(Checkbox):
    def check(self) -> None: 
        print("Mac Checkbox checked")
    
    def render(self) -> None:
        print("Rendering macOS-style checkbox")

# Abstract Factory using Protocol (alternative to ABC)
class GUIFactory(Protocol):
    """Factory interface for creating UI components"""
    def create_button(self) -> Button:
        """Create a platform-specific button"""
        ...
    
    def create_checkbox(self) -> Checkbox:
        """Create a platform-specific checkbox"""
        ...

# Concrete Factories
class WinFactory:
    def create_button(self) -> Button:
        return WinButton()
    
    def create_checkbox(self) -> Checkbox:
        return WinCheckbox()

class MacFactory:
    def create_button(self) -> Button:
        return MacButton()
    
    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()

# Client Code
class Application:
    def __init__(self, factory: GUIFactory):
        self._factory = factory
        self._button = factory.create_button()
        self._checkbox = factory.create_checkbox()
    
    def create_ui(self) -> None:
        """Create and initialize the UI components"""
        self._button.render()
        self._checkbox.render()
    
    def simulate_interaction(self) -> None:
        """Simulate user interactions"""
        self._button.click()
        self._checkbox.check()
    
    @property
    def button(self) -> Button:
        return self._button
    
    @property
    def checkbox(self) -> Checkbox:
        return self._checkbox

# Factory selector (useful for dynamic factory selection)
class UIFactory:
    @staticmethod
    def get_factory(os_type: str) -> GUIFactory:
        """Factory method to get appropriate factory based on OS"""
        factories = {
            "windows": WinFactory,
            "mac": MacFactory,
            "win": WinFactory,
            "macos": MacFactory,
        }
        
        factory_class = factories.get(os_type.lower())
        if not factory_class:
            raise ValueError(f"Unsupported OS type: {os_type}")
        
        return factory_class()

# Main execution
if __name__ == "__main__":
    print("=== Windows UI Demo ===")
    win_factory = WinFactory()
    win_app = Application(win_factory)
    win_app.create_ui()
    win_app.simulate_interaction()
    
    print("\n" + "="*30 + "\n")
    
    print("=== Mac UI Demo ===")
    mac_factory = MacFactory()
    mac_app = Application(mac_factory)
    mac_app.create_ui()
    mac_app.simulate_interaction()
    
    print("\n" + "="*30 + "\n")
    
    print("=== Dynamic Factory Selection Demo ===")
    try:
        # Example of dynamic factory selection
        factory = UIFactory.get_factory("windows")
        app = Application(factory)
        app.create_ui()
        app.simulate_interaction()
    except ValueError as e:
        print(f"Error: {e}")
