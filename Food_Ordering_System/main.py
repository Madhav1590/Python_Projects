import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display 

## Function to display the bill at the end of the order
def display_bill():
    global bill, name
    total_bill_price = bill["Total Price"].sum() #15   
    bill.loc[len(bill.index)]  = ['', '', '', total_bill_price]   ## To add the total bill price at the end of bill
    display(bill)

    bill.to_csv(name + '.csv')  ## Save the .csv (bill) file to computer

    bill = bill[0:0]    ## To clear the items ordered by customer and get the original format for bill


## Function to display the visualization of contribution of each item to the bill
def display_visualization():
    global bill, name
    bill.plot(kind='bar', x="Food Item", y="Total Price", \
              title="Contribution of each item", figsize=(10, 10))
    plt.savefig(name + ".png")  ## Save the visualization to computer
    plt.show()


## Program starts here :
menu = pd.read_csv("FOOD_MENU.csv") #Menu
bill = pd.read_csv("Bill.csv")  #template

print("Hello and Welcome to our Restaurant.")
name = str(input("Please enter your name: "))
display(menu)       # To display csv file on the screen

while True:         # waiter
    print(' ')
    order = input("Press O to add items \n"
                  "Press D to delete items \n"
                  "Press U to update number of units in order \n"
                  "Press E to end the order : ").lower()
    
    ## If customer wants to order or add more items
    if order == 'o' :
        item_number = int(input("Select the number of your food item : "))
        no_items = int(input("How many units do you want to order ? "))
        
        item_name = menu.iloc[item_number, 0]   #salad
        item_price = menu.iloc[item_number, 1]  #250
        total_price = item_price * no_items     #250*5

        print(item_name + " added successfully")
        print('')

        ## Add items to the end of the bill
        bill.loc[len(bill.index)]  = [item_name, no_items, item_price, total_price]
        display(bill)

    ## If customer wants to delete the items in the menu
    elif order == 'd':
        display(bill)
        item_number = int(input("Select the number of your food item to be deleted: "))
        item_name = bill.iloc[item_number, 0]

        bill.drop(item_number, inplace=True)
        print(item_name + " deleted successfully.")
        print('')

        bill.index = list(range(len(bill)))
        display(bill)

    ## If customer wants to update the bill
    elif order == 'u':
        display(bill)
        item_number = int(input("Select the number of your food item whose units need to be updated: "))
        no_items = int(input("Enter the updated number of units: "))
        
        item_name = bill.iloc[item_number, 0]
        item_price = (bill.iloc[item_number, 3] / bill.iloc[item_number, 1]) 
        total_price = item_price * no_items

        bill.loc[item_number]  = [item_name, no_items, item_price, total_price]
        print(item_name + " updated successfully")
        print('')


    ## If customer decides to end the order
    else:
        display_visualization()
        display_bill()
        break

