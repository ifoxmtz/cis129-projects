#Declare my constants (price of items)
COFFEE_PRICE = 5
MUFFIN_PRICE = 4
TAX = 0.06
TEA_PRICE = 2
SANDWICH_PRICE = 7.5

#Display café name
print('***************************************')
print("Isabella's Café")

#Create input variables for customer
coffee = int(input("Number of coffees bought? "))
muffin = int(input("Number of muffins bought? "))
tea = int(input("Number of teas bought? "))
sandwich = int(input("Number of sandwiches bought? "))

#Processing: Calculate the total cost
coffee_total = coffee * COFFEE_PRICE
muffin_total = muffin * MUFFIN_PRICE
tea_total = tea * TEA_PRICE
sandwich_total = sandwich * SANDWICH_PRICE
total_tax = TAX * (coffee_total + muffin_total + tea_total + sandwich_total)
total_cost = total_tax + coffee_total + muffin_total + tea_total + sandwich_total

#Output: Display the receipt to the customer - display name of item, number of items bought, price, and total cost
print('***************************************\n\n***************************************')
print("Isabella's Café Receipt")
print(str(coffee) + ' Coffee at $' + str(COFFEE_PRICE) + ' each: $' + str(coffee_total))
print(str(muffin) + ' Muffin at $' + str(MUFFIN_PRICE) + ' each: $' + str(muffin_total))
print(str(tea) + ' Tea at $' + str(TEA_PRICE) + ' each: $' + str(tea_total))
print(str(sandwich) + ' Sandwich at $' + str(SANDWICH_PRICE) + ' each: $' + str(sandwich_total))
print('6% tax: $' + str(total_tax))
print('---------')
print('Total: ' + str(total_cost))

#Thank you for using this script! -IBF
