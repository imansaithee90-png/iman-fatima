
# STRINGS: INDEXING AND SLICING

text = "Python Programming"

# 1. Original String
print("Original String:", text)

# 2. Positive Indexing
print("First Character:", text[0])
print("Second Character:", text[1])
print("Sixth Character:", text[5])

# 3. Negative Indexing
print("Last Character:", text[-1])
print("Second Last Character:", text[-2])

# 4. Slicing
print("First Six Characters:", text[0:6])
print("Characters from Index 7:", text[7:17])

# 5. Without Start Index
print("Beginning to Index 6:", text[:6])

# 6. Without End Index
print("Index 7 to End:", text[7:])

# 7. Complete String
print("Complete String:", text[:])

# 8. Slicing with Step
print("Every Second Character:", text[::2])

# 9. Reverse String
print("Reverse String:", text[::-1])

# 10. String Length
print("String Length:", len(text))

# 11. Uppercase
print("Uppercase:", text.upper())

# 12. Lowercase
print("Lowercase:", text.lower())

# 13. Replace
print("Replace:", text.replace("Python", "Java"))

# 14. Find
print("Find Programming:", text.find("Programming"))

# 15. Count
print("Count of m:", text.count("m"))
