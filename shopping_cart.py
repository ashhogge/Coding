print("Welcome to the Shopping Cart Program!")

menu = """
Menu:
1. Add a new item
2. Remove an item
3. Show the contents in the cart
4. Find total
5. Quit
"""

shopping_cart = []

while True:
    print(menu)
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        item = {}  
        item["name"] = input("What is the item? ")
        item["price"] = float(input("What is the price of '{}'?".format(item["name"])))
        item["quantity"] = int(input("How many are you getting? "))

        shopping_cart.append(item)
        print("Item added to the shopping cart.")

    elif choice == "2":
        item_name = input("Enter the name of the item to remove: ")
        for item in shopping_cart:
            if item["name"] == item_name:
                shopping_cart.remove(item)
                print("Item removed from the shopping cart.")
                break
        else:
            print("Cannot find the item in the shopping cart.")

    elif choice == "3":
        print("Shopping Cart:")
        for item in shopping_cart:
            print(f"Name: {item['name']}, Price: {item['price']}, Quantity: {item['quantity']}")

    elif choice == "4":
        total = sum(item["price"] * item["quantity"] for item in shopping_cart)
        print(f"Total cost: {total}")

    elif choice == "5":
        print("Thank you for using the Shopping Cart Program. Goodbye!")
        break

    else:
        print("Please choose a number 1-5")
