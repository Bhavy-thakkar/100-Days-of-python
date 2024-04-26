print("Welcome to the tip calculator.")
bill = float(input("What is the total bill? $"))
tip = int(input("How much tip would you like to give? 10$ , 12$, or 15$?"))
people = int(input("How many peoples are you split the bill?"))
total_bill = tip / 100 * bill + bill
tip_per_person = tip/100 * bill
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Your total bill with tip is ${total_bill}")
print(f"You have to pay ${tip_per_person} tip")
print(f"Each person shold pay: ${final_amount}")
