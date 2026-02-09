from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def execute_query(self, query: str) -> str:
        pass

class RealDatabase(Database):
    def __init__(self, database_name: str):
        self.database_name = database_name
        print(f"Connecting to {self.database_name} database...")
        self.load_data()
    
    def load_data(self):
        print(f"Loading data from {self.database_name}...")
    
    def execute_query(self, query: str) -> str:
        print(f"Executing query on {self.database_name}: {query}")
        return f"Results for: {query}"

class DatabaseProxy(Database):
    def __init__(self, database_name: str):
        self.database_name = database_name
        self._real_database = None
        self.access_level = "admin"
    
    def execute_query(self, query: str) -> str:
        if self._real_database is None:
            self._real_database = RealDatabase(self.database_name)
        
        if self.check_access():
            result = self._real_database.execute_query(query)
            self.log_query(query)
            return result
        else:
            return "Access Denied: Insufficient permissions"
    
    def check_access(self) -> bool:
        if self.access_level == "admin":
            return True
        elif self.access_level == "user":
            return False
        return False
    
    def log_query(self, query: str):
        print(f"Log: Query executed - {query}")

class CachedDatabaseProxy(Database):
    def __init__(self, database_name: str):
        self.database_name = database_name
        self._real_database = None
        self._cache = {}
    
    def execute_query(self, query: str) -> str:
        if query in self._cache:
            print(f"Returning cached results for: {query}")
            return self._cache[query]
        
        if self._real_database is None:
            self._real_database = RealDatabase(self.database_name)
        
        result = self._real_database.execute_query(query)
        self._cache[query] = result
        return result

if __name__ == "__main__":
    print("=== Regular Database Access ===")
    real_db = RealDatabase("ProductionDB")
    print(real_db.execute_query("SELECT * FROM users"))
    
    print("\n=== Proxy with Access Control ===")
    proxy = DatabaseProxy("SecureDB")
    print(proxy.execute_query("SELECT * FROM employees"))
    
    print("\n=== Proxy with Caching ===")
    cached_proxy = CachedDatabaseProxy("ProductDB")
    print(cached_proxy.execute_query("SELECT * FROM products"))
    print(cached_proxy.execute_query("SELECT * FROM products"))
    print(cached_proxy.execute_query("SELECT * FROM orders"))
    print(cached_proxy.execute_query("SELECT * FROM products"))
    
    print("\n=== Testing Access Control ===")
    proxy.access_level = "user"
    print(proxy.execute_query("DELETE FROM users"))
