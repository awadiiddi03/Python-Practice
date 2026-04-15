stock_items = ("Bread", 17.50, "Milk", 15.90,"Coke", 20.30, "Chocolate", 19.20, "Cooking Oil", 24.65) 
 
cart = []
option = 6
item = ""
quantity = 0
cost = 0.0

while option != 7:
        #counter = 1 starts the counter at 1 whenever you enter any value
    counter = 1
    for index in range (0,len(stock_items),2):
        #len is used to iterate through the exact length of the array
        #index starts at 0 and ends at 9 (10)
        
        #range(10) - prints 0 to 9
        #range(10, 2) - starts at 10 and ends at 2
        #range(10, 2, 3) starts at 10, ends at 2 and step/counts in 3's
        
        
        
        #the 0 is used it start at index 0
        #the 2 is used to count in 2's (0, 2, 4, 6, 8)
        print(f"{counter}. {stock_items[index]} ({stock_items [index +1]})")
        
        counter += 1
    print(f"{counter}. Checkout")
    counter += 1
    print(f"{counter}. Exit")

    option = int(input("Please choose a menu option: "))
            
    
    if option <=  5 and option >= 1:
        if option == 1:
            item = "Bread"
        elif option == 2:
            item = "Milk"
        elif option == 3:
            item = "Coke"
        elif option == 4:
            item = "Chocolate"
        else:
            item = "Cooking Oil"
            
    
        quantity = int(input(f"How many {item}s do you want? "))
        
#         while quantity <= 0:
#             quantity = int(input("ITEMS CANNOT BE ZERO OR NEGATIVE!" ))
#             
        if item in cart:
             pos = cart.index(item) #if there is already an item
             cart[pos+ 1] += quantity #increase it in the list
             
        else:
             cart.append(item)
             cart.append(quantity)
        
    elif option == 6:
            if len(cart) >= 1:
                print (f"{'Receipt' :^36}")
                print (f"{'ITEMS' :<15} {'QTY' :>5} {'UNIT' :>10}{'TOTAL$' :>10}")
                total_cost = 0
                for index in range(0,len(cart),2):
                    items = cart[index]
                    quantity = cart[index +1]
                    pos = stock_items.index(items)
                    price = stock_items[pos + 1]
                    total = quantity * price
                    total_cost += total 
                    print (f"{items:<15}{quantity :>5} {price :>11}{total :>10}")
                print("_" *45)
                tax_amount = total_cost * 0.15
                print(f"{'Tax (15%)':>27} {tax_amount:9.2f}")
                final_total = total_cost + tax_amount
                print(f"{'GrandTotal':>27} {final_total:9.2f}\n")
            else:
                print("Your shopping cart is empty")
                
    
    elif option == 7:
        print("Thank you shopping with us!!")
    else:
        print("Invalid menu option, chose between 1 and 7")