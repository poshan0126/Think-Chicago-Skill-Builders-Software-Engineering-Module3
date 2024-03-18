class DataProcessor:
    def __init__(self, orders, contacts):
        self.orders = orders
        self.contacts = contacts

    def display_orders(self):
        print("Order Details:")
        for customer_name, product, quantity in self.orders:
            print(f"{customer_name} ordered {quantity} unit(s) of {product}.")

    def sort_contacts(self):
        sorted_contacts = sorted(self.contacts, key=lambda contact: contact[0])
        print("\nSorted Contacts:")
        for name, email, phone in sorted_contacts:
            print(f"Name: {name}, Email: {email}, Phone: {phone}")

    def filter_contacts(self, initial_letter):
        filtered_contacts = [contact for contact in self.contacts if contact[0].startswith(initial_letter)]
        print(f"\nContacts starting with '{initial_letter}':")
        for name, email, phone in filtered_contacts:
            print(f"Name: {name}, Email: {email}, Phone: {phone}")

# Sample data
orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
]
contacts = [
    ("Alice", "alice@email.com", "123-456-7890"),
    ("Bob", "bob@email.com", "234-567-8901"),
]

# Create an instance of DataProcessor
processor = DataProcessor(orders, contacts)

# Execute methods to display orders, sort, and filter contacts
processor.display_orders()
processor.sort_contacts()
processor.filter_contacts("A")
