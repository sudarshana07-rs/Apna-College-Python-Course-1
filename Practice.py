item_list=[]
print("Welcome to R.S Grocery Store!!!")
print("Gorcery List")
print('-'*30)
name=input("Enter your name: ")
phone=input("Enter your contact: ")
choice= input("Type YES or yes or Yes to check the available items: ")
if (choice == 'Yes' or choice== 'YES' or choice== 'yes' ): 
    print("HERE IS THE AVAILABLE ITEMS:")
    print('*' * 30)
    print(f'''\t\tItems\t Price\n
            Milk\t Rs.30
            Paneer\t Rs.50
            Mushroom\t Rs.80
            Atta\t Rs.150
            Rice\t Rs.300''')
    print('-'*30)
else: 
    print("Recomended to see the available items!!!")
items=['Milk','Paneer','Mushroom','Atta','Rice']
prince=[30,50,80,150,300]
item_no=int(input("Enter the no. of item to be purchased(5 or below): "))
if (item_no <= 5):
    for i in range(item_no):
        purchased_items=input("Enter the item: ")
        item_list.append(purchased_items)
        if (purchased_items not in items):
            print("OOPS item not availabe!!!")
else: 
    print("Items availabe is only 5!!!")    
print(f'Purchased Item List: {item_list}')