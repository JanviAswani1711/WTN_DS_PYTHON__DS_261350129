#1. Write a program to read the entire content from a text file and display it to the user.

filename = input("Enter file name: ")
file = open(filename, "r")
content = file.read()
print(content)
file.close()

'''Sample Output
Enter file name: sample.txt

Hello Everyone
Welcome to Python
File Handling'''

#2. Write a program to read first n lines from a text file. Get n as user input.

filename = input("Enter file name: ")
n = int(input("Enter number of lines: "))

file = open(filename, "r")
for i in range(n):
    line = file.readline()

    if line == "":
        break

    print(line, end="")

file.close()

'''Sample Output
Enter file name: sample.txt
Enter number of lines: 2

Hello Everyone
Welcome to Python'''


#3. Write a program to accept input from user and append it to a text file.

filename = input("Enter file name: ")
file = open(filename, "a")
text = input("Enter text to append: ")

file.write(text + "\n")
file.close()
print("Data appended successfully.")

'''Sample Output
Enter file name: sample.txt
Enter text to append: This is new line

Data appended successfully.'''


#4. Write a program to read contents from a text file line by line and store each line into a list.

filename = input("Enter file name: ")
file = open(filename, "r")
lines = []

for line in file:
    lines.append(line.strip())

file.close()
print(lines)

'''Sample Output:
If file contains

Python
Java
C++'''


#5. Write a program to find the longest word from the text file contents, assuming that the file will have only one longest word in it.
# Find longest word in a file

filename = input("Enter file name: ")
file = open(filename, "r")

content = file.read()
words = content.split()
longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word

file.close()
print("Longest Word:", longest)

'''Sample Output

File
Python is a powerful programming language'''


#6. Write a program to count the frequency of a user entered word in a text file.
# Count frequency of a word in a file

filename = input("Enter file name: ")
file = open(filename, "r")
content = file.read()

file.close()
word = input("Enter word to search: ")

words = content.split()

count = 0

for w in words:
    if w == word:
        count += 1

print("Frequency =", count)