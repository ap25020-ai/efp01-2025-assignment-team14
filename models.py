from datetime import datetime   

class Driver: # Represents a drievr
    def __init__(self, driver_id: int , name: str):
        self.driver_id = driver_id
        self.name = name

    def __str__(self) -> str: # String representation of the driver
        return f"{self.driver_id}: {self.name} "
    
class Worker: # Represents a worker
    def __init__(self, worker_id: int, name: str):
        self.worker_id = worker_id
        self.name = name

    def __str__(self) -> str: # String representation of the worker
        return f"{self.worker_id}: {self.name}"
    
class Pallet: # Represents a pallet
    def __init__(self, barcode : int, date_time_received: datetime):
        self.barcode = barcode
        self.date_time_received = date_time_received
        self.status = "WAITING"
        self.shelf_id = None
        self.driver_id = None

    def __str__(self) -> str: # String representation of the pallet
        return f"Barcode {self.barcode}: ({self.date_time_received}) Status: {self.status} Shelf ID: {self.shelf_id}"   
    
class Shelf: # Represents a shelf
    def __init__(self, shelf_id: int, kapacity: str, current_kapacity: int = 0):
        self.shelf_id = shelf_id
        self.kapacity = kapacity
        self.current_kapacity = current_kapacity


    def has_free_Spot(self) -> bool:
        # TODO: επιστρέψτε True αν υπάρχει διαθέσιμη θέση
        return self.current_kapacity < self.kapacity

    def add_kapacity(self) -> None:
        # TODO: αυξήστε τον αριθμό αποθέματος κατά 1
        self.current_kapacity += 1

    def __str__(self) -> str: # String representation of the class shelf
        return (f"{self.current_kapacity}/{self.kapacity} ")
    
class Warehouse: # Represents a warehouse
    def __init__(self, capacity: int, current_capacity: int = 0):
        self.capacity = capacity
        self.current_capacity = current_capacity

    def has_free_spot(self) -> bool:
        # TODO: επιστρέψτε True αν υπάρχει διαθέσιμη θέση
        return self.current_capacity < self.capacity

    def add_capacity(self) -> None:
        # TODO: αυξήστε τον αριθμό αποθέματος κατά 1
        self.current_capacity += 1

    def __str__(self) -> str: # String representation of the class Warehouse
        return (f"{self.current_capacity}/{self.capacity} ")
    
