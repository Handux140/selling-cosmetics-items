class CosmeticItem:
    def __init__(self, name, variant, price, stock):
        self.name = name
        self.variant = variant
        self.price = price
        self.stock = stock

    def calculate_selling_price(self):
        return self.price * 0.1

class CosmeticShop:
    def __init__(self):
        self.items = []
        self.transactions = 0
        self.profits = 0

    def add_item(self, item):
        self.items.append(item)

    def display_items(self):
        print("Available Items:")
        print("Name\t\tVariant\t\tPrice\tStock")
        for item in self.items:
            print(f"{item.name}\t\t{item.variant}\t${item.price}\t{item.stock}")

    def sell_item(self, item_index):
        item = self.items[item_index]
        if item.stock > 0:
            item.stock -= 1
            selling_price = item.calculate_selling_price()
            self.profits += selling_price
            self.transactions += 1
            print(f"Sold {item.name} ({item.variant}) for ${selling_price:.2f}")
        else:
            print("Item out of stock.")

    def display_summary(self):
        print("\nSummary:")
        print(f"Total Transactions: {self.transactions}")
        print(f"Total Profits: ${self.profits:.2f}")

def main():
    shop = CosmeticShop()

    # Adding sample items
    shop.add_item(CosmeticItem("Lipstick", "Matte Red", 15, 10))
    shop.add_item(CosmeticItem("Eyeshadow Palette", "Neutral Tones", 30, 5))
    shop.add_item(CosmeticItem("Mascara", "Lengthening", 12, 8))

    while True:
        print("\n1. Display available items")
        print("2. Sell item")
        print("3. Display summary")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            shop.display_items()
        elif choice == '2':
            item_index = int(input("Enter the index of the item to sell: "))
            shop.sell_item(item_index)
        elif choice == '3':
            shop.display_summary()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()