print("welcome to the tip calculator")
bill = float(input("what was the total bill:"))
tip = int(input("what percentage tip would you like to give? 10,12,or 15? "))
person = int(input("How many people to split the bill? "))
bill_and_tips = ((tip/100)*bill) + bill
print("total bill:",round(bill_and_tips))
total = bill_and_tips/person
print("Each person should pay :{}".format(round(total,2)))
