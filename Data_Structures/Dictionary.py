#1. Write a program to add a key and value to a dictionary.
dict1:{0:10,1:20}
dict1[2]=30
print(dict1)

#2. Write a program to concatenate the following dictionaries to create a new one.
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}
new_dict={}
new_dict.update(dic1)
new_dict.update(dic2)
new_dict.update(dic3)
print(new_dict)

#3. Write a program to check if a given key already exists in a dictionary.
student={
  "Name":"Neha"
  "Age":21
  "Roll_No":51
}
key=input("Enter the key: ")
if key in student:
  print("Key exists.")
else:
  print("Key does not exist.")


#4. Write a program to iterate over a dictionary using a for loop and print:
-->Keys alone
-->Values alone
-->Both keys and values
student = {
    "Name": "Neha",
    "Age": 20,
    "City": "Indore"
}
print("Keys:")
for key in student:
    print(key)

print("\nValues:")
for value in student.values():
    print(value)

print("\nKeys and Values:")
for key, value in student.items():
    print(key, ":", value)


#5. Write a program to prepare a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the squares of the keys.
square = {}
for i in range(1, 16):
    square[i] = i * i
print(square)

#6. Write a program to sum all the values in a dictionary, considering the values are of int type.
marks = {
    "Math": 90,
    "Science": 85,
    "English": 80
}
total = sum(marks.values())
print("Sum =", total)