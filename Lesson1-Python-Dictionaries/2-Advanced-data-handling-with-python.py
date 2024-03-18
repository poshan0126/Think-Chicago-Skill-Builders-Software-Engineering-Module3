class HotelBookingTracker:
    def __init__(self):
        self.hotel_rooms = {
            "101": {"status": "available", "customer": ""},
            "102": {"status": "booked", "customer": "John Doe"}
        }

    def book_room(self, room_number, customer_name):
        if self.hotel_rooms.get(room_number, {}).get("status") == "available":
            self.hotel_rooms[room_number] = {"status": "booked", "customer": customer_name}
            return f"Room {room_number} successfully booked for {customer_name}."
        else:
            return f"Room {room_number} is not available."

    def check_out_customer(self, room_number):
        if self.hotel_rooms.get(room_number, {}).get("status") == "booked":
            self.hotel_rooms[room_number] = {"status": "available", "customer": ""}
            return f"Room {room_number} is now available."
        else:
            return f"Room {room_number} is already available or does not exist."

    def display_room_status(self):
        for room, details in self.hotel_rooms.items():
            print(f"Room {room}: {details['status']}, Customer: {details['customer']}")

class EcommerceProductSearch:
    def __init__(self):
        self.products = {
            "1": {"name": "Laptop", "category": "Electronics", "price": 800},
            "2": {"name": "Shirt", "category": "Clothing", "price": 20}
        }

    def search_products(self, search_query):
        matching_products = []
        for product_id, details in self.products.items():
            if search_query.lower() in details["name"].lower():
                matching_products.append(details)
        return matching_products if matching_products else "No matching products found."

# Instantiate and use the classes
hotel_tracker = HotelBookingTracker()
print(hotel_tracker.book_room("101", "Alice Smith"))
print(hotel_tracker.check_out_customer("102"))
hotel_tracker.display_room_status()

ecommerce_search = EcommerceProductSearch()
matching_products = ecommerce_search.search_products("laptop")
print(matching_products)
