class CustomerDataCleanup:
    def __init__(self, customer_ids):
        self.customer_ids = customer_ids

    def remove_duplicates(self):
        unique_ids = set(self.customer_ids)
        print("Unique Customer IDs:", unique_ids)

# Example usage
customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
cleanup = CustomerDataCleanup(customer_ids)
cleanup.remove_duplicates()
