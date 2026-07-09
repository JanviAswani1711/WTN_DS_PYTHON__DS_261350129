#1. Write a program to print the 4th element from first and 4th element from last in a tuple.
t = (10, 20, 30, 40, 50, 60, 70, 80)
print("4th element from first:", t[3])
print("4th element from last:", t[-4])


#2. Write a program to check whether an element exists in a tuple or not.
t = (10, 20, 30, 40, 50)
element = int(input("Enter element: "))
if element in t:
    print("Element exists.")
else:
    print("Element does not exist.")
  
#3. Write a program to convert a list into a tuple.
lst = [10, 20, 30, 40, 50]
t = tuple(lst)
print("Tuple:", t)


#4. Write a program to find the index of an item in a tuple.
t = (10, 20, 30, 40, 50)
item = int(input("Enter item: "))
if item in t:
    print("Index:", t.index(item))
else:
    print("Item not found.")
  
#5. Write a program to replace the last value of tuples in a list with 100.
lst = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
new_list = []

for t in lst:
    new_tuple = t[:-1] + (100,)
    new_list.append(new_tuple)

print(new_list)