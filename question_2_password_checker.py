
password = input("Enter your password: ")

has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_number = any(char.isdigit() for char in password)

if (len(password) >= 8 and has_upper
        and has_lower and has_number):
    print("Strong Password")
elif (len(password) >= 6 and
      ((has_upper or has_lower) or has_number)):
    print("Moderate Password")
else:
    print("Weak Password")
