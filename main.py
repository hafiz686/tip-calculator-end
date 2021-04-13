#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places.


print("Welcome to the tip calculator!")

#enter the bill amount.
bill = float(input("What was the total bill? $"))

#enter the tip percentage. 
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

#enter the people in which you want to split the bill.
people = int(input("How many people to split the bill?"))

#formula for tip calculator.
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")
#
#the end.
