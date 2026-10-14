
full_name = input("Enter your full name: ")

# Remove extra spaces
full_name = full_name.strip()

# Split name into separate words
names = full_name.split()

if len(names) == 0:
    print("Please enter a valid name.")
else:
    # Initials
    initials = ""
    for name in names:
        initials += name[0].upper() + ". "

    print("Initials:", initials.strip())

    # Entire name in uppercase
    print("Uppercase Name:", full_name.upper())

    # Entire name reversed
    print("Reversed Name:", full_name[::-1])
