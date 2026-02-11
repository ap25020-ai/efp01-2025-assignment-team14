from services import WarehouseSystem
from models import Pallet
from datetime import datetime

def main():
    system = WarehouseSystem()
    print("Καλωσήρθατε στο σύστημα διαχείρισης αποθήκης!")

    while True:
        print("\n--- Μενού ---")
        print("1. Εισαγωγή Υπαλλήλου")
        print("2. Σκανάρισμα Παλέτας")
        print("3. Εισαγωγή Οδηγού")
        # print("4. Εμφάνιση Ειδοποίησης σε οδηγό")
        # print("4. Εμφάνιση μηνύματος επιβεβαίωσης")
        print("4. Λίστα παλετών ανά ράφι και οδηγό")
        print("0. Έξοδος")

        choice = input("Επιλογή: ")

        if choice == "1":
            name = input("Δώσε όνομα υπαλλήλου: ")
            worker = system.find_or_create_worker(name)
            print(f"Υπάλληλος δημιουργήθηκε/βρέθηκε: {worker}")

        elif choice == "2":
            barcode = int(input("Δώσε barcode παλέτας: "))
            date_time_received = datetime.now()
            pallet = Pallet(barcode, date_time_received)
            system.scan_pallet(pallet)
            print(f"Παλέτα σκαναρίστηκε: {pallet}")

        elif choice == "3":
            name = input("Δώσε όνομα οδηγού: ")
            driver = system.find_or_create_driver(name)
            print(f"Οδηγός δημιουργήθηκε/βρέθηκε: {driver}")
        
        # elif choice == "4":
            pallet = system.get_waiting_pallets()
            warehouse = system.get_warehouse_capacity()
            system.init_shelves()
            shelf = system.get_free_shelf()
            if not pallet:
                print("Δεν υπάρχει παλέτα προς αποθήκευση")
                continue

            if not warehouse.has_free_spot():
                print("Δεν υπάρχει διαθέσιμος χώρος στην αποθήκη")
                continue
            
            
            if not shelf:
                print("Δεν υπάρχει διαθέσιμο ράφι")
                continue

            # if not system.drivers:
            #     print("Δεν υπάρχει οδηγός για ειδοποίηση")
                
            system.pending_shelf = shelf
            system.pending_driver = driver
            system.pending_pallet = pallet
            driver = system.drivers[0]  # απλή επιλογή πρώτου οδηγού
            system.notify_driver(driver, f"Αποθήκευσε παλέτα {pallet.barcode} στο ράφι {shelf.shelf_id}")
