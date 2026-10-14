
# 1. LIST
# List mein multiple values store hoti hain.
# List change ho sakti hai.

my_list = [10, 20, 30, 40, 50]

print("Original List:", my_list)
print("First Element:", my_list[0])

my_list.append(60)
print("After Append:", my_list)

my_list.remove(30)
print("After Remove:", my_list)

my_list[0] = 100
print("After Update:", my_list)

print("List Length:", len(my_list))


# 2. TUPLE
# Tuple mein values store hoti hain.
# Tuple ko directly change nahi kar sakte.

my_tuple = (10, 20, 30, 40, 50)

print("\nOriginal Tuple:", my_tuple)
print("First Element:", my_tuple[0])
print("Tuple Length:", len(my_tuple))


# 3. SET
# Set unique values store karta hai.
# Duplicate values automatically remove ho jati hain.

my_set = {10, 20, 30, 20, 40, 10}

print("\nOriginal Set:", my_set)

my_set.add(50)
print("After Add:", my_set)

my_set.discard(20)
print("After Discard:", my_set)

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference:", set_a - set_b)


# 4. DICTIONARY
# Dictionary data ko key-value pairs mein store karta hai.

my_dict = {
    "name": "Ali",
    "age": 20,
    "city": "Lahore"
}

print("\nOriginal Dictionary:", my_dict)
print("Name:", my_dict["name"])

my_dict["age"] = 21
print("After Update:", my_dict)

my_dict["course"] = "Python"
print("After Adding Key:", my_dict)

my_dict.pop("city")
print("After Removing City:", my_dict)

print("All Keys:", my_dict.keys())
print("All Values:", my_dict.values())

for key, value in my_dict.items():
    print(key, ":", value)
