menu ={
    'Pizza':50, 'Burger':80, 'Coffee':40, 'Tea':30 , 'Pasta':60
    }
menu = {k.lower(): v for k, v in menu.items()}

print("Welcome to Star Resturant")
print("Pizza: Rs50\nBurger: Rs80\nCoffee: Rs40\nTea: Rs30\nPasta: Rs60")

item_1=input("Enter the name  of item you want to order = ")
order_total=0

if item_1 in menu:
    order_total += menu[item_1] 
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} has not available yet")

another_order=input("Do you want to another item? (Yes/No) ")

if another_order=="yes":
    item_2=input("Enter the name of second item = ")
    if item_2 in menu:
        order_total +=menu[item_2]
        print(f"Item {item_2} has been order")
    else:
        print(f"Order item {item_2} is not available ")

print(f"The total amount of items to pay {order_total}")


