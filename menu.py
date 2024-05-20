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

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order_list: list[dict[str, float | int]] = []

# Launch the store and present a greeting to the customer
print("Welcome to Bob's food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:

    # Ask the customer from which menu category they want to order
    print("\nFrom which menu category would you like to order?\n")

    # Create a variable for the menu category number
    category_counter: int = 1
    # Create a dictionary to store the menu for later retrieval
    menu_categories: dict[int, str] = {}

    # Print the options to choose from menu categories (all the first level
    # dictionary items in menu).
    for menu_category in menu.keys():
        print(f"{category_counter}: {menu_category}")
        # Store the menu category associated with its menu item number
        menu_categories[category_counter] = menu_category
        # Add 1 to the menu category number
        category_counter += 1

    # Get the customer's numeric input
    menu_category_num = input("\nType menu category number: ")

    # Check if the customer's input is a number
    if menu_category_num.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category_num) in menu_categories.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_categories[int(menu_category_num)]
            # Print out the menu category name they selected
            print(f"\nYou selected {menu_category_name}.")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?\n")
            item_counter = 1
            menu_items: dict[int, dict[str, float]] = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for menu_item, price_or_dict in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(price_or_dict) is dict:
                    for sub_item, sub_price in price_or_dict.items():
                        # Print the menu item
                        sub_item_name = f"{menu_item} - {sub_item}"
                        print(
                            f"{item_counter:>6} | {sub_item_name:<24} | {sub_price:>6.2f}")
                        # Add the menu item to the menu_items dictionary
                        menu_items[item_counter] = {
                            "ItemName": sub_item_name,
                            "Price": sub_price
                        }
                        # Add 1 to the menu item counter
                        item_counter += 1
                else:
                    # Print the menu item
                    print(
                        f"{item_counter:>6} | {menu_item:<24} | {price_or_dict:>6.2f}")
                    menu_items[item_counter] = {
                        "ItemName": menu_item,
                        "Price": price_or_dict
                    }
                    # Add 1 to the menu item counter
                    item_counter += 1

            # 2. Ask customer to input menu item number
            selected_item_str = input("\nEnter the item # you want to order: ")

            # 3. Check if the customer typed a number
            if selected_item_str.isdigit():

                # Convert the menu selection to an integer
                item_num = int(selected_item_str)

                # 4. Check if the menu selection is in the menu items
                if item_num in menu_items.keys():

                    # Store the item name as a variable
                    item_name: str = menu_items[item_num]["ItemName"]

                    # Ask the customer for the quantity of the menu item
                    item_quantity_str = input(
                        f"How many {item_name}s would you like? ")

                    # Check if the quantity is a number, default to 1 if not
                    if item_quantity_str.isdigit():
                        item_quantity = int(item_quantity_str)
                    else:
                        item_quantity = 1

                    # Add the item name, price, and quantity to the order list
                    order_list.append({
                        "ItemName": item_name,
                        "Price": menu_items[item_num]["Price"],
                        "Quantity": item_quantity})

                else:
                    # Tell the customer that their input isn't a valid option
                    print(f"{item_num} is not an item # option.")

            else:
                # Tell the customer they didn't select a number
                print("You didn't select a number.")

        else:
            # Tell the customer they didn't select a menu category option
            print(f"{menu_category_num} is not a menu category option.")

    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

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
            # Customer decided to stop ordering, thank them for their order
            if len(order_list) > 0:
                print("Thank you for your order.")
            # Exit the keep ordering question loop
            break
        else:
            # Tell the customer they didn't select a valid option
            print("You didn't select a valid option. Please try again.")

if len(order_list) <= 0:
    # Tell the customer they didn't order anything
    print("You didn't order anything.")
    print("I guess you aren't hungry. Have a nice day!")
    # Exit the program
    exit()

# Print out the customer's order
print("\nThis is what we are preparing for you:\n")

# Uncomment the following line to check the structure of the order
# print(order_list)

print("Item name                 |  Price | Quantity | Item Amount ")
print("--------------------------|--------|----------|-------------")

# 6. Loop through the items in the customer's order
for item in order_list:
    # 7,8,9, and 10. Print the item name, price, and quantity
    price = item['Price']
    quantity = item['Quantity']
    print(
        f"{item['ItemName']:<25} | {price:>6.2f} | {quantity:>8,} | {price * quantity:>11,.2f}")

# 11. Calculate the total amount of the order
# Multiply the price by quantity for each item in the order list
total_amount: list[float | int] = [order_list[i]['Price'] *
                                   order_list[i]['Quantity'] for i in range(len(order_list))]

# 12. Calculate, format, and print the total amount of the order
print("==========================|========|==========|============")
total_amt_str = f"${sum(total_amount):,.2f}"
print(f"Total Amount: {total_amt_str:>45}\n")
