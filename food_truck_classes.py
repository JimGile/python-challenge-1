
class MenuItem:

    # Class level properties shared by all instances
    num_col_width = 6
    name_col_width = 24
    price_col_width = 6

    @classmethod
    def set_num_col_width(cls, num_col_width: int) -> None:
        cls.num_col_width = num_col_width

    @classmethod
    def set_name_col_width(cls, name_col_width: int) -> None:
        cls.name_col_width = name_col_width

    @classmethod
    def set_price_col_width(cls, price_col_width: int) -> None:
        cls.price_col_width = price_col_width

    @classmethod
    def print_header(cls) -> None:
        print("Item # | Item name                | Price")
        print("-------|--------------------------|-------")

    def __init__(self, num: int, name: str, price: float) -> None:
        self.num = num
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f"{self.num} - {self.name} - ${self.price}"

    def print_item(self) -> None:
        print(f"{self.num:>6} | {self.name:<24} | {self.price:>6,.2f}")


class MenuCategory:

    def __init__(self, num: int, name: str, *menu_items_dict: dict[str, float | dict]) -> None:
        self.num = num
        self.name = name
        self.menu_items: dict[int, MenuItem] = {}
        if len(menu_items_dict) > 0:
            self.load_menu_items(menu_items_dict[0])

    def load_menu_items(self, menu_items_dict: dict[str, float | dict]) -> None:
        num = 1
        for item_name, price_or_dict in menu_items_dict.items():
            num = self.add_menu_item_from_dict(num, item_name, price_or_dict)

    def add_menu_item_from_dict(self, num: int, name: str, price_or_dict: float | dict) -> int:
        if type(price_or_dict) is dict:
            for sub_item, sub_price in price_or_dict.items():
                menu_item = MenuItem(num, name + " - " + sub_item, sub_price)
                self.add_menu_item(menu_item)
                num += 1
        else:
            menu_item = MenuItem(num, name, price_or_dict)
            self.add_menu_item(menu_item)
            num += 1
        return num

    def add_menu_item(self, menu_item: MenuItem) -> None:
        self.menu_items[menu_item.num] = menu_item

    def print_menu_items(self) -> None:
        MenuItem.print_header()
        for menu_item in self.menu_items.values():
            menu_item.print_item()

    def get_menu_item_by_num(self, user_itemn_num: str) -> tuple[int, MenuItem]:
        # Get the menu category based on the user's input
        if user_itemn_num.isdigit() is False:
            return -1, None
        num = int(user_itemn_num)
        return num, self.menu_items[num]


class Menu:

    def __init__(self, name: str, *menu_dict: dict[str, dict[str, float | dict]]) -> None:
        self.name = name
        self.menu_categories: dict[int, MenuCategory] = {}
        if len(menu_dict) > 0:
            self.load_menu_categories(menu_dict[0])

    def load_menu_categories(self, menu_dict: dict[str, dict[str, float | dict]]) -> None:
        num = 1
        for category_name, menu_items_dict in menu_dict.items():
            self.add_menu_category_from_dict(num, category_name, menu_items_dict)
            num += 1

    def add_menu_category_from_dict(self, num: int, name: str, menu_items_dict: dict[str, float | dict]) -> None:
        menu_category = MenuCategory(num, name, menu_items_dict)
        self.menu_categories[menu_category.num] = menu_category

    def add_menu_item(self, menu_category: MenuCategory) -> None:
        self.menu_categories[menu_category.num] = menu_category

    def print_menu_categories(self) -> None:
        for menu_category in self.menu_categories.values():
            print(f"{menu_category.num}: {menu_category.name}")

    def get_menu_category_by_num(self, num: int) -> MenuCategory:
        return self.menu_categories[num]


class OrderItem:
    def __init__(self, menu_item: MenuItem, quantity: int) -> None:
        self.menu_item = menu_item
        self.quantity = quantity
        self.amount = menu_item.price * quantity

    def __str__(self) -> str:
        return f"{self.menu_item} - {self.quantity}"

    def print_order_item(self) -> None:
        # Print the item name, price, quantity, and amount
        name = self.menu_item.name
        price = self.menu_item.price
        print(f"{name:<25} | {price:>6.2f} | {self.quantity:>8,} | {self.amount:>11,.2f}")


class Order:
    def __init__(self, order_num: int) -> None:
        self.order_num = order_num
        self.order_items: list[OrderItem] = []

    def add_order_item(self, order_item: OrderItem) -> None:
        self.order_items.append(order_item)

    def __str__(self) -> str:
        return f"Order #{self.order_num}"

    def print_order(self) -> None:
        if len(self.order_items) <= 0:
            # Tell the customer they didn't order anything
            print("You didn't order anything.")
            print("I guess you aren't hungry. Have a nice day!")
        else:
            self.print_receipt()

    def print_receipt(self) -> None:
        # Print out the customer's order
        print("Thank you for your order.")
        print("\nThis is what we are preparing for you:\n")
        print("Item name                 |  Price | Quantity | Item Amount ")
        print("--------------------------|--------|----------|-------------")

        # Loop through the items in the customer's order
        for order_item in self.order_items:
            # Print the item name, price, quantity, and amount
            order_item.print_order_item()

        # Calculate the total amount of the order
        total_amount = sum([order_item.amount for order_item in self.order_items])

        # 12. Calculate, format, and print the total amount of the order
        print("==========================|========|==========|============")
        total_amt_str = f"${total_amount:,.2f}"
        print(f"Total Amount: {total_amt_str:>45}\n")


class FoodTruck:
    def __init__(self, name: str) -> None:
        self.order_num: int = 0
        self.name = name
        self.menu: Menu | None = None
        self.order: Order | None = None

    def load_menu(self, name: str, menu_dict: dict[str, dict[str, float | dict]]) -> None:
        self.menu = Menu(name, menu_dict)

    def place_order(self) -> None:
        # Start a new order and present a greeting to the customer
        self.order_num += 1
        self.order = Order(self.order_num)
        print(f"Welcome to {self.name} food truck. Your order number is {self.order_num}.")

    def print_menu_categories(self) -> None:
        self.menu.print_menu_categories()

    def get_menu_category_by_num(self, user_category_num: str) -> tuple[int, MenuCategory]:
        # Get the menu category based on the user's input
        if user_category_num.isdigit() is False:
            return -1, None
        num = int(user_category_num)
        return num, self.menu.get_menu_category_by_num(num)

    def add_item_to_order(self, menu_item: MenuItem, item_quantity_str: str) -> None:
        # Check if the quantity is a number, default to 1 if not
        if item_quantity_str.isdigit():
            item_quantity = int(item_quantity_str)
        else:
            item_quantity = 1
        self.order.add_order_item(OrderItem(menu_item, item_quantity))

    def print_order(self) -> None:
        self.order.print_order()
