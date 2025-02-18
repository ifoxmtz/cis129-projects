#Declare my constants (price of items)
COFFEE_PRICE = 5
MUFFIN_PRICE = 4
TAX = 0.06

    #Add new menu prices: tea, sandwich

#Display café name
print('***************************************')
print('My Coffee and Muffin Shop')

#Create input variables for customer
coffee = int(input("Number of coffees bought? "))
muffin = int(input("Number of muffins bought? "))

    #Add new menu items: tea, sandwich

#Processing: Calculate the total cost
coffee_total = coffee * COFFEE_PRICE
muffin_total = muffin * MUFFIN_PRICE
    Add new menu totals: tea, sandwich
total_tax = TAX * (coffee_total + muffin_total)
total_cost = total_tax + coffee_total + muffin_total

#Output: Display the receipt to the customer
    #display name of item, number of items bought, price, and total cost
print('***************************************\n\n***************************************')
print('My Coffee and Muffin Shop Receipt')
print(str(coffee) + ' Coffee at $' + str(COFFEE_PRICE) + ' each: $' + str(coffee_total))
print(str(muffin) + ' Muffin at $' + str(MUFFIN_PRICE) + ' each: $' + str(muffin_total))
    #Add new menu items: tea, sandwich
print('6% tax: $' + str(total_tax))
print('---------')
print('Total: ' + str(total_cost))
