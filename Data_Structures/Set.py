#1. Write a program to remove a given item from the set.
s = {10, 20, 30, 40, 50}
print("Original Set:", s)
item = int(input("Enter the item to remove: "))
if item in s:
    s.remove(item)
    print("Updated Set:", s)
else:
    print("Item not found in the set.")


#2. Write a program to create an intersection of sets.
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

result = (set1&set2)
print("Intersection of sets:", result)


#3. Write a program to create a union of sets.
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

result = (set1|set2)
print("Union of sets:", result)


#4. Write a program to find the maximum and minimum value in a set.
s = {45, 12, 89, 23, 67}
maximum = max(s)
minimum = min(s)
print("Maximum value:", maximum)
print("Minimum value:", minimum)