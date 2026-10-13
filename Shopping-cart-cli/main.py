Menu = [
    {"earphone": 500},
    {"laptop": 5006},
    {"iphone": 5055},
    {"samsung": 50034},
    {"chini": 5003},
    {"itel": 200},
    {"pixel": 300},
    {"shamir": 200},
    {"cover": 500},
    {"buds": 500},
    {"vivo": 500},
    {"redmi": 500},
]

cart = []


def view_menu():
    for item in Menu:
        print(item)


def view_cart():
    return cart


while True:
    user_input = input(
        "\n1. View Menu\n"
        "2. Add to Cart\n"
        "3. View Cart\n"
        "4. Remove from Cart\n"
        "5. Checkout\n"
        "6. Quit\n"
        "Enter your choice: "
    )

    if user_input == "1":
        view_menu()

    elif user_input == "2":
            
            item_input = input("Enter item name to add: ").lower()
            for item in Menu:
                if item_input in item:
                    cart.append(item.copy())
                    print("Item added successfully")
                    break
            else:
                print("Item not found in menu")

    elif user_input == "3":
        if not cart:
            print("Your Cart is Empty")
        else:
            print("Your cart:")
            print(view_cart())

    elif user_input == "4":
        item_input = input("Enter item name to remove: ").lower()

        for item in cart:
            if item_input in item:
                cart.remove(item)
                print("Item removed successfully")
                break
        else:
            print("Item not found in cart")

    elif user_input == "5":
        total_price = 0 

        print("Checkout & total")
        for item in cart:
            for name, price in item.items():
                print(f"Item: {name} | Price: {price}")
                total_price += price

        print("--------------------")
        print("Total Items:", len(cart))
        print("Total Price:", total_price)

    elif user_input == "6" or user_input.lower() == "quit":
        print("Thank you!")
        break

    else:
        print("Enter a valid choice")