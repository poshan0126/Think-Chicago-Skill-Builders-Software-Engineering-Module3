import copy

class SalesDataManager:
    def __init__(self, sales_data):
        self.sales_data = sales_data

    def clone_and_update_sales(self, week, category, new_sales):
        """
        Creates a deep copy of the sales data and updates the sales figure
        for a specific category in a given week.
        """
        sales_copy = copy.deepcopy(self.sales_data)
        try:
            if week in sales_copy and category in sales_copy[week]:
                sales_copy[week][category] = new_sales
                print(f"Sales updated. New sales for {category} in {week}: {new_sales}")
            else:
                print("Week or category not found.")
        except KeyError as e:
            print(f"Error updating sales: {e}")
        return sales_copy

# Initial sales data
weekly_sales = {
    "Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
    "Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
}

# Create an instance of the class with the initial sales data
manager = SalesDataManager(weekly_sales)

# Demonstrate cloning and updating sales figures
updated_sales = manager.clone_and_update_sales("Week 2", "Electronics", 18000)

# Display the updated sales data
print("\nUpdated Sales Data:")
for week, data in updated_sales.items():
    print(f"{week}: {data}")
