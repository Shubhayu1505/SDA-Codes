import threading
from typing import Any, Dict, Optional, ClassVar

class SingletonMeta(type):
    """Metaclass for thread-safe singleton pattern"""
    _instances: Dict[type, Any] = {}
    _lock: threading.Lock = threading.Lock()
    
    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        """Thread-safe singleton instance creation"""
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
                print(f"Created new {cls.__name__} instance")
            else:
                print(f"Returning existing {cls.__name__} instance")
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    """Singleton class implementation with thread safety"""
    _initialized: ClassVar[bool] = False
    
    def __init__(self):
        """Initialize the singleton instance only once"""
        if not self._initialized:
            self.data = "Singleton Data"
            self.__class__._initialized = True
            print(f"Initialized {self.__class__.__name__}")
    
    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} at {hex(id(self))}>"
    
    def show_data(self) -> None:
        """Display singleton data"""
        print(f"Data: {self.data}")
    
    def add_data(self, new_data: str) -> None:
        """Add to singleton data"""
        self.data += f", {new_data}"
    
    def clear_data(self) -> None:
        """Clear singleton data (reset to default)"""
        self.data = "Singleton Data"
        print("Data cleared to default")


# Alternative implementation with decorator (thread-safe)
def singleton(cls):
    """Thread-safe decorator-based singleton implementation"""
    instances = {}
    lock = threading.Lock()
    
    def get_instance(*args, **kwargs):
        with lock:
            if cls not in instances:
                instances[cls] = cls(*args, **kwargs)
                print(f"Created new {cls.__name__} instance via decorator")
            else:
                print(f"Returning existing {cls.__name__} instance via decorator")
        return instances[cls]
    
    return get_instance


@singleton
class ConfigManager:
    """Singleton configuration manager"""
    def __init__(self):
        self.config = {"theme": "dark", "language": "en", "version": "1.0.0"}
        print("ConfigManager initialized")
    
    def __repr__(self) -> str:
        return f"<ConfigManager at {hex(id(self))}>"
    
    def get_config(self, key: str) -> Optional[Any]:
        """Get configuration value by key"""
        return self.config.get(key)
    
    def set_config(self, key: str, value: Any) -> None:
        """Set configuration value"""
        self.config[key] = value
        print(f"Updated config: {key} = {value}")
    
    def remove_config(self, key: str) -> bool:
        """Remove configuration key"""
        if key in self.config:
            del self.config[key]
            print(f"Removed config key: {key}")
            return True
        return False
    
    def show_all_configs(self) -> None:
        """Display all configurations"""
        print("Current configuration:")
        for key, value in self.config.items():
            print(f"  {key}: {value}")
    
    @classmethod
    def reset(cls) -> None:
        """Reset the singleton instance (for testing)"""
        global instances
        if cls in singleton.instances:
            del singleton.instances[cls]


# Another example: Database connection pool
class DatabaseConnection(metaclass=SingletonMeta):
    """Singleton database connection pool"""
    def __init__(self, connection_string: str = "default://localhost:5432"):
        if not hasattr(self, '_initialized'):
            self.connection_string = connection_string
            self.connections = []
            self.max_connections = 10
            print(f"Database pool initialized: {connection_string}")
            self._initialized = True
    
    def get_connection(self):
        """Get a database connection from the pool"""
        # Simulated connection logic
        return f"Connection from {self.connection_string}"
    
    def close_all(self):
        """Close all connections in the pool"""
        self.connections.clear()
        print("All database connections closed")


# Main execution
if __name__ == "__main__":
    print("=== SINGLETON PATTERN DEMONSTRATION ===\n")
    
    # Test basic Singleton
    print("1. Basic Singleton Implementation (Thread-Safe):")
    print("-" * 40)
    
    # Create first instance
    s1 = Singleton()
    s1.show_data()
    s1.add_data("Additional Info")
    
    # Try to create second instance
    s2 = Singleton()
    s2.show_data()  # Should show the same data
    s2.add_data("More Data")
    
    # Verify they are the same instance
    print(f"\nAre s1 and s2 the same instance? {s1 is s2}")
    print(f"s1: {s1}")
    print(f"s2: {s2}")
    
    # Test data persistence
    s1.show_data()
    
    # Test decorator-based Singleton
    print("\n\n2. Decorator-based Singleton:")
    print("-" * 40)
    
    # Create first ConfigManager instance
    config1 = ConfigManager()
    print(f"Config theme: {config1.get_config('theme')}")
    config1.set_config("language", "fr")
    config1.set_config("timeout", 30)
    config1.show_all_configs()
    
    # Try to create second instance
    config2 = ConfigManager()
    print(f"\nConfig language from config2: {config2.get_config('language')}")
    
    # Verify they are the same
    print(f"\nAre config1 and config2 the same instance? {config1 is config2}")
    print(f"config1: {config1}")
    print(f"config2: {config2}")
    
    # Test removal
    config1.remove_config("timeout")
    config1.show_all_configs()
    
    # Demonstration with multiple calls
    print("\n\n3. Multiple Singleton Calls:")
    print("-" * 40)
    
    # All these should return the same instance
    instances = [Singleton() for _ in range(3)]
    for i, instance in enumerate(instances, 1):
        print(f"Instance {i}: {instance}")
    
    print(f"\nAll instances are the same: {all(instances[0] is i for i in instances)}")
    
    # Test database connection singleton
    print("\n\n4. Database Connection Singleton Example:")
    print("-" * 40)
    
    db1 = DatabaseConnection("postgresql://localhost:5432/mydb")
    db2 = DatabaseConnection()  # Should return existing instance
    print(f"db1 connection: {db1.get_connection()}")
    print(f"db1 is db2: {db1 is db2}")
    
    # Test thread safety demonstration
    print("\n\n5. Thread Safety Demonstration:")
    print("-" * 40)
    
    def create_singleton_thread(name: str):
        """Function to create singleton from different threads"""
        s = Singleton()
        print(f"[{name}] Singleton id: {id(s)}")
    
    # Create threads to test thread safety
    threads = []
    for i in range(5):
        thread = threading.Thread(target=create_singleton_thread, args=(f"Thread-{i}",))
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    print("\n✓ All threads completed successfully!")
