inventory = {}

while True:
    print("Inventory menu!")
    print("1. Add new items")
    print("2. Show all items")
    print("3. Search item")
    print("4. Update stock")
    print("5. Delete item")
    print("6. Data analysis")
    print("7. Exit")

    choice = input("Please input your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        price = float(input("Enter price: "))
        stock = int(input("Enter stock: "))
        inventory[name] = (price, stock)
        print("Item added")

    elif choice == "2":
        if len(inventory) == 0:
            print("No items in inventory")
        else:
            for item in inventory:
                price, stock = inventory[item]
                print(item, "- Price:", price, "Stock:", stock)

    elif choice == "3":
        name = input("Ennter item name: ")
        if name in inventory:
            price, stock = inventory[name]
            print("Item found! - Price:", price, "Stock: ", stock)
        else:
            print("Not found.")
    elif choice == "4":
        name = input("Enter item name to update stock! ")
        if name in inventory:
            new_stock = int(input("Amount: "))
            price = inventory[name][0]
            inventory[name] = (price, new_stock)
            print("Stock updated.")
        else:
            print("Item not found!")
    elif choice == "5":
        name = input("Enter name to delete")
        if name in inventory:
            del inventory[name]
            print("Deleted!")
        else:
            print("Not found!")
    elif choice == "6":
        if len(inventory) == 0:
            print("No data to analyze!")
        else:
            prices = []
            total_value = 0
            for item in inventory:
                price, stock = inventory[item]
                prices.append((item, price))
                total_value += price * stock
            
            most_expensive = max(prices, key=lambda x: x[1])
            cheapest = min(prices, key=lambda x: x[1])

            print("Most expensive: ", most_expensive[0], "- Price: ", most_expensive[1])
            print("Cheapest: ", cheapest[0], "-price: ", cheapest[1])
            print("Total stock value: ", total_value)

    elif choice == "7":
        print("EXITING PROGRAM.")
        break

    else:
        print("Invalid. Please type the correct number like above.")