"""
Module 2 Challenge - Food Truck Menu Ordering

This script allows the user to select a menu category from a list of
first level keys in the menu dictionary. It then displays a list of
menu items from the selected menu category. The user can then select
an item from the list and enter the quantity that they want to order.
When the user is done ordering, it calculates the total cost of the
order and prints a reciept to the console.

Author: Jim Gile
Date: 5/18/2024
"""

from food_truck_classes import FoodTruck

# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

food_truck = FoodTruck("Bob's")
food_truck.load_menu("Menu", menu)
food_truck.place_order()

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:

    # Ask the customer from which menu category they want to order
    print("\nFrom which menu category would you like to order?\n")
    food_truck.print_menu_categories()

    # Get the customer's numeric input
    selected_category_str = input("\nType menu category number: ")

    # Check if the customer's input is a valid option
    category_num, category = food_truck.get_menu_category_by_num(selected_category_str)
    if category_num > 0:
        # Save the menu category name to a variable and print it out
        # Print out the menu options from the menu_category_name
        menu_category_name = category.name
        print(f"\nYou selected {menu_category_name}.")
        print(f"What {menu_category_name} item would you like to order?\n")
        category.print_menu_items()
        selected_item_str = input("\nEnter the item # you want to order: ")
        item_num, item = category.get_menu_item_by_num(selected_item_str)
        if item_num > 0:
            # Store the item name as a variable
            # Ask the customer for the quantity of the menu item
            item_name = item.name
            item_quantity_str = input(f"How many {item_name}s would you like? ")
            # Add the item and quantity to the order list
            food_truck.add_item_to_order(item, item_quantity_str)
        else:
            # Tell the customer that their input isn't a valid option
            print(f"{selected_item_str} is not a valid item # option.")
    else:
        # Tell the customer that their input isn't a valid option
        print(f"{selected_category_str} is not a valid category # option.")

    # 4. Check if the customer wants to keep ordering
    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input(
            "\nWould you like to keep ordering? (Y)es or (N)o ")

        # 5. Check the customer's input
        if keep_ordering.upper() == "Y":
            # Keep ordering
            place_order = True
            # Exit the keep ordering question loop
            break
        elif keep_ordering.upper() == "N":
            # Complete the order
            place_order = False
            # Exit the keep ordering question loop
            break
        else:
            # Tell the customer they didn't select a valid option
            print("You didn't select a valid option. Please try again.")

food_truck.print_order()
