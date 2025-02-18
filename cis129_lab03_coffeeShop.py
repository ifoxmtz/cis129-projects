#Declare my constants (name of item, number of items purchased, price of items)
COFFEE_PRICE = 5
MUFFIN_PRICE = 4
TAX = int(0.06)

#Display café name
print('***************************************')
print('My Coffee and Muffin Shop')

#Create input variables for customer
coffee = input("Number of coffees bought?")
muffin = input("Number of muffins bought?")

#Processing: Calculate the total cost
coffee_total = coffee * COFFEE_PRICE
muffin_total = muffin * MUFFIN_PRICE
total_tax = TAX * (coffee_total + muffin_total)
total_cost = total_tax + coffee_total + muffin_total

#Output: Display the receipt to the customer
    #display name of item, number of items bought, price, and total cost
print('***************************************\n***************************************')
print('My Coffee and Muffin Shop Receipt')
print(coffee "Coffee at $" COFFEE_PRICE "each: $" coffee_total)
