def update_menu_add_beverages(menu):
    """
    Adds a new category 'Beverages' with at least two items to the menu.
    """
    menu["Beverages"] = {"Coffee": 2.99, "Tea": 1.99}
    return menu

def update_menu_prices_remove_item(menu):
    """
    Updates the price of 'Steak' and removes 'Bruschetta' from 'Starters'.
    """
    # Update price of Steak
    menu["Main Course"]["Steak"] = 17.99
    
    # Remove Bruschetta from Starters
    if "Bruschetta" in menu["Starters"]:
        del menu["Starters"]["Bruschetta"]
    
    return menu

def main():
    # Initial menu structure
    restaurant_menu = {
        "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
        "Main Course": {"Steak": 15.99, "Salmon": 13.99},
        "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
    }

    # Task 1: Add Beverages category
    updated_menu = update_menu_add_beverages(restaurant_menu)
    print("Menu after adding Beverages:", updated_menu)
    
    # Task 2: Update prices and remove items
    final_menu = update_menu_prices_remove_item(updated_menu)
    print("Final updated menu:", final_menu)

# Call the main function to execute the updates
main()
