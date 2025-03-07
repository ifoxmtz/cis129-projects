# Lab 5 The Bottle Return Program

# Step 1: Declare variables below 
total_bottles = 0 # store the accumulated bottle values
counter = 1 # control the loop
today_bottles = 0 # store the number of bottles returned on a day
total_payout = 0 # store the calculated value of totalBottles times .10
keep_going = "y" # used to run the program again

# Step 2: Loop to run program again
while keep_going == "y":
    # Step 3: Code to set value of variables
    DAYS = 7
    total_bottles = 0 # store the accumulated bottle values
    counter = 1 # control the loop
    today_bottles = 0 # store the number of bottles returned on a day
    total_payout = 0    
    while counter <= DAYS:
        print("Enter number of bottles returned for day #", counter, ":")
        today_bottles =  int(input()) # code to set value of variable todayBottles using user input
        total_bottles = total_bottles + today_bottles
        counter = counter + 1
        
        #code to calc payout
        PAYOUT_PER_BOTTLE = 0.1
        total_payout = 0
        total_payout = total_bottles * 0.1 # code to set value of variable totalPayout
	
    # code to print the number of total bottles and total payout
    print("Total number of bottles returned:", total_bottles)
    print("Total payout:", total_payout)
    
    print("Do you want to enter another week’s worth of data? (Enter y or n)")
    keep_going = input()
