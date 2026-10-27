class Menu:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        self.items[name] = price

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
        else:
            print("Item not found")

    def get_item_price(self, name):
        return self.items.get(name, "Item not found")

    def display_menu(self):
        for item, price in self.items.items():
            print(f"{item}: {price}")


class Order:
    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity):
        if name in menu.items:
            self.items[name] = quantity
        else:
            print("Item not found")

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
        else:
            print("Item not found")

    def display_order(self):
        for item, quantity in self.items.items():
            print(f"{item}: {quantity}")


class Table:
    def __init__(self, table_number):
        self.table_number = table_number
        self.order = Order()

    def place_order(self, order):
        self.order = order

    def display_order(self):
        self.order.display_order()


class Staff:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def display_info(self):
        print(f"Name: {self.name}, Role: {self.role}")


class Bill:
    def __init__(self, table):
        self.table = table
        self.total = 0

    def calculate_total(self):
        for item, quantity in self.table.order.items.items():
            price = menu.get_item_price(item)
            self.total += float(price) * quantity

    def display_bill(self):
        print(f"Table {self.table.table_number} Bill:")
        self.table.display_order()
        print(f"Total: {self.total}")


# Initialize menu
menu = Menu()

# Add items to menu
menu.add_item("Burger", 10.99)
menu.add_item("Fries", 3.99)
menu.add_item("Soda", 2.99)

# Initialize tables
tables = [Table(i) for i in range(1, 11)]

# Initialize staff
staff = [Staff("John", "Manager"), Staff("Jane", "Waitress")]

# Initialize bills
bills = []

# Main loop
while True:
    print("\n1. Menu management")
    print("2. Table reservation and ordering")
    print("3. Order tracking")
    print("4. Billing and payment processing")
    print("5. Staff management")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("\nMenu management")
        print("1. Add item")
        print("2. Remove item")
        print("3. Display menu")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            menu.add_item(name, price)
        elif choice == "2":
            name = input("Enter item name: ")
            menu.remove_item(name)
        elif choice == "3":
            menu.display_menu()

    elif choice == "2":
        print("\nTable reservation and ordering")
        table_number = int(input("Enter table number: "))
        for table in tables:
            if table.table_number == table_number:
                print("1. Place order")
                print("2. Display order")
                choice = input("Choose an option: ")

                if choice == "1":
                    while True:
                        item = input("Enter item name: ")
                        quantity = int(input("Enter quantity: "))
                        table.order.add_item(item, quantity)
                        choice = input("Enter another item (y/n): ")
                        if choice.lower() != "y":
                            break
                elif choice == "2":
                    table.display_order()
                break
        else:
            print("Table not found")

    elif choice == "3":
        print("\nOrder tracking")
        table_number = int(input("Enter table number: "))
        for table in tables:
            if table.table_number == table_number:
                print("1. Display order")
                table.display_order()
                break
        else:
            print("Table not found")

    elif choice == "4":
        print("\nBilling and payment processing")
        table_number = int(input("Enter table number: "))
        for table in tables:
            if table.table_number == table_number:
                bill = Bill(table)
                bill.calculate_total()
                bill.display_bill()
                break
        else:
            print("Table not found")

    elif choice == "5":
        print("\nStaff management")
        print("1. Display staff info")
        choice = input("Choose an option: ")

        if choice == "1":
            for staff_member in staff:
                staff_member.display_info()

    elif choice == "6":
        break

    else:
        print("Invalid choice")
