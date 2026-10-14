
bill = float(input("Enter total restaurant bill: "))
tip_percent = float(input("Enter tip percentage: "))
people = int(input("Enter number of people: "))

if bill < 0 or tip_percent < 0 or people <= 0:
    print("Please enter valid values.")
else:
    tip = bill * tip_percent / 100
    total_bill = bill + tip
    per_person = total_bill / people

    print("Total Tip:", round(tip, 2))
    print("Bill Including Tip:", round(total_bill, 2))
    print("Each Person Pays:", round(per_person, 2))
