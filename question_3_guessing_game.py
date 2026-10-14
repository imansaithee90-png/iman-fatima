
secret_number = 42
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    guess = int(input("Guess a number (1-100): "))

    if guess < 1 or guess > 100:
        print("Invalid number! Enter between 1 and 100.")
        continue

    attempts += 1

    if guess == secret_number:
        print("Congratulations! Correct guess.")
        break
    else:
        print("Wrong guess! Attempts used:", attempts)

else:
    print("Game Over! You lost.")
