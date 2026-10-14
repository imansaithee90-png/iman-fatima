# Program 6: Loops in Python

# For Loop
print("For Loop:")
for i in range(1, 6):
    print(i)

# While Loop
print("While Loop:")
i = 1
while i <= 5:
    print(i)
    i += 1

# Break Statement
print("Break Example:")
for i in range(1, 6):
    if i == 4:
        break
    print(i)

# Continue Statement
print("Continue Example:")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# Loop Else
print("Loop Else Example:")
for i in range(1, 4):
    print(i)
else:
    print("Loop completed!")