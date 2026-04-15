stock_items = {
    "Bread": 17.50,
    "Milk": 15.90,
    "Coke": 20.30,
    "Chocolate": 19.20,
    "Cooking Oil": 24.65
}

cart = {}
items_list = list(stock_items.keys())

while True:
    print("\n--- SPAZA SHOP MENU ---")
    for i, name in enumerate(items_list, 1):
        print(f"{i}. {name} (R{stock_items[name]})")
    
    print(f"{len(items_list) + 1}. Checkout")
    print(f"{len(items_list) + 2}. Exit")

    try:
        option = int(input("\nPlease choose an option: "))
        
        # Adding items to cart
        if 1 <= option <= len(items_list):
            item_name = items_list[option - 1]
            qty = int(input(f"How many {item_name}s? "))
            
            if qty > 0:
                cart[item_name] = cart.get(item_name, 0) + qty
                print(f"Added {qty} {item_name}(s) to cart.")
            else:
                print("Quantity must be greater than 0.")

        # Checkout
        elif option == len(items_list) + 1:
            if not cart:
                print("\nYour cart is empty!")
            else:
                print(f"\n{'RECEIPT':^40}")
                print(f"{'ITEM':<15} {'QTY':>5} {'UNIT':>10} {'TOTAL':>10}")
                subtotal = 0
                for item, qty in cart.items():
                    price = stock_items[item]
                    line_total = qty * price
                    subtotal += line_total
                    print(f"{item:<15} {qty:>5} {price:>10.2f} {line_total:>10.2f}")
                
                tax = subtotal * 0.15
                print("-" * 42)
                print(f"{'Tax (15%)':>31} {tax:10.2f}")
                print(f"{'Grand Total':>31} {subtotal + tax:10.2f}")
                cart.clear() # Clear cart after purchase

        # Exit
        elif option == len(items_list) + 2:
            print("Thank you for shopping with us!")
            break
        else:
            print("Invalid selection.")
            
    except ValueError:
        print("Please enter a valid number.")
