from models import Driver, Worker, Pallet, Shelf, Warehouse

class WarehouseSystem:
    def __init__(self):
        self.drivers = []
        self.workers = []
        self.pallets = []
        self.warehouses = []
        self.shelves = []

        self.pending_shelf = None   
        self.pending_driver = None
        self.pending_pallet = None

        self._next_driver_id = 1
        self._next_worker_id = 1
    
    # ------- driver ---------

    def find_or_create_driver(self, name: str) -> Driver:
        for d in self.drivers:
            if d.name == name:
                return d
        driver = Driver(self._next_driver_id, name)
        self.drivers.append(driver)
        self._next_driver_id += 1
        return driver
    
    # ------- worker ---------

    def find_or_create_worker(self, name: str) -> Worker:
        for w in self.workers:
            if w.name == name:
                return w
        worker = Worker(self._next_worker_id, name)
        self.workers.append(worker)
        self._next_worker_id += 1
        return worker

    # ------- pallet ---------
    def scan_pallet(self, pallet: Pallet):
        pallet.status = "WAITING"
        self.pallets.append(pallet)

    def get_waiting_pallets(self):
        for p in self.pallets:
            if p.status.upper() == "WAITING":  
                return p
        return None

    # ------- warehouse ---------
    def get_warehouse_capacity(self) -> Warehouse:
        if not self.warehouses:
            self.warehouses.append(Warehouse(10))
        return self.warehouses[0]
        
    def store_pallet(self, pallet: Pallet, shelf: Shelf, driver: Driver):
        
        wh = self.get_warehouse_capacity()
        wh.add_capacity()

        pallet.shelf_id = shelf.shelf_id
        pallet.driver_id = driver.driver_id
        pallet.status = "Stored"
        
    # ------- shelf ---------
    def init_shelves(self):
        if not self.shelves:
            self.shelves.append(Shelf(1, "A1"))
            self.shelves.append(Shelf(2, "A2"))
            self.shelves.append(Shelf(3, "B1"))

    def get_free_shelf(self) -> Shelf | None:
        for shelf in self.shelves:
            used = False
            for p in self.pallets:
                if p.shelf_id == shelf.shelf_id:
                    used = True
                    break
            if not used:
                return shelf
        return None
        
    # ------- notification ---------
    def notify_driver(self, driver: Driver, message: str) -> None:
        print(f"Ειδοποίηση προς οδηγό {driver.name}: {message}")  

    # ------- confirmation message ---------
    def confirmation_message(self, message: str) -> None:
        print(f"Μήνυμα επιβεβαίωσης: {message}")    
