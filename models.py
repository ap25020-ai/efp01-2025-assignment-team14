from datetime import datetime

class Driver: # Represents a driver
    def __init__(self, driver_id: int, name: str):
        self.driver_id = driver_id
        self.name = name

    def __str__(self) -> str: # String representation of the Driver 
        return f"{self.driver_id}: {self.name}"

class Worker: # Represents a worker
    
    def __init__(self, worker_id: int, name: str):
        self.worker_id = worker_id
        self.name = name

    def __str__(self) -> str: # String representation of the Worker 
        return f"{self.worker_id}: {self.name}"