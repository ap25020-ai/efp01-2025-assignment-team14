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