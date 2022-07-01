print('''\n============// Add Items to the cart //================= \n''')
print('''\n================= List of Items ===============================

1. Book at 12.49
2. Music CD at 14.99
3. Choclate Bar at 0.85
4. Imported box of choclates at 10.00
5. Imported bottle of perfume at 47.50
6. Imported bottle of perfume at 27.99
7. Bottle of Perfume at 18.99
8. Packet of Headache pills at 9.75
9. Box of Imported choclates at 11.25

 \n''')

item = input("What do you want to add to your cart: ")
category = input("Input your category: ")
qty = int(input("Input Quantity: "))
price = float(input("Product Price: "))
imported = input("Is it imported category? y/n: ")

#Condition for filtering type

if imported == 'n' or category != "book" and category != "food" and category != "pills":
    tax = price * 0.10 # 10% Sales Tax
    price = price + tax
    print('''\n============// RECEIPT //================= \n''')
    print(qty,item)
    print('Sales Tax ',tax)
    print('Total ',round(price,2))

    if imported == 'y':
        import_duty = price * 0.05 # 5% Import duty
        price2 = price + import_duty
        print('''============// RECEIPT //=============== ''')
        #print(qty,category)
        #print('Import Duty',import_duty)
        print('Total with Import Duty ',round(price2,2))
    
else:
    print('Total',qty,item,round(price,2))
