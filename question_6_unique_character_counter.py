
sentence = input("Enter a long sentence: ")

# Convert sentence into a set
unique_characters = set(sentence.replace(" ", ""))

print("Unique Characters:", unique_characters)
print("Total Unique Characters:", len(unique_characters))
