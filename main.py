menu = {
    'Pizza': 1000, 'Burger': 80, 'Coffee': 40, 'Tea': 30, 'Pasta': 60,
    'Salad' : 70, 'Frankie': 80
}

# Convert all menu items to lowercase for consistent comparison
menu = {k.lower(): v for k, v in menu.items()}

print("Welcome to Star Restaurant")
print("Pizza: Rs50\nBurger: Rs80\nCoffee: Rs40\nTea: Rs30\nPasta: Rs60\nSalad: 70\nFrankie: 80")

item_1 = input("Enter the name of item you want to order: ").lower()  # Convert input to lowercase
order_total = 0

if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not available yet")

# Validation loop for "Do you want to order another item?"
while True:
    another_order = input("Do you want to order another item? (Yes/No): ").lower()
    if another_order == "yes":
        item_2 = input("Enter the name of second item: ").lower()  # Convert input to lowercase
        if item_2 in menu:
            order_total += menu[item_2]
            print(f"Item {item_2} has been added to your order")
        else:
            print(f"Ordered item {item_2} is not available")
        break
    elif another_order == "no":
        break
    else:
        print("If you want to order please write YES otherwise NO.")

print(f"The total amount to pay is Rs {order_total}")
