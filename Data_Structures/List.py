#1. Write a program to create a list of 5 integers and display the list items. Access individual elements through index.
numbers = [10, 20, 30, 40, 50]

print("List:", numbers)

print("First element:", numbers[0])
print("Second element:", numbers[1])
print("Third element:", numbers[2])
print("Fourth element:", numbers[3])
print("Fifth element:", numbers[4])

#2. Write a program to append a new item to the end of the list.
fruits=["Apple","Mango","Cherry","Grapes","Pineapple"]
print(fruits)
fruits.append("Strawberry")
print("Updated List:",fruits)

# 3. Write a program to reverse the order of the items in the list.
list=[10,20,30,40,"Apple"]
list.reverse()
print("Updated List: ",list)

#4. Write a program to print the number of occurrences of a specified element in a list.
numbers = [10, 20, 30, 20, 40, 20, 50]
element = int(input("Enter the element to count: "))
count = numbers.count(element)
print("Occurrences:", count)

#5. Write a program to append the items of list1 to list2 in the front.
list1 = [1, 2, 3,8]
list2 = [4, 5, 6]
result = list1 + list2
print("New List:", result)

#Alternative by using extend()
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)

#6. Write a program to insert a new item before the second element in an existing list.
list=[10,20,30,40]
item=int(input("Enter new item: "))
list.insert(1,item)
print("Updated List:", list)


#7. Write a program to remove the item from a specified index in a list.
list=[10,20,30,"Apple","Banana"]
list.remove(1)
print(list)

#8. Write a program to remove the first occurrence of a specified element from a list.
numbers = [10, 20, 30, 20, 40, 20]
element = int(input("Enter element to remove: "))

if element in numbers:
    numbers.remove(element)
    print("Updated List:", numbers)
else:
    print("Element not found")