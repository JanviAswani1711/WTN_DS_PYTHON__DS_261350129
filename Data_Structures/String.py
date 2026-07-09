#1.  Write a program to count the number of upper and lower case letters in a string.
s = input("Enter a string: ")
upper = 0
lower = 0
for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)


#2. Write a program that will check whether a given string is palindrome or not.
s = input("Enter a string: ")
if s == s[::-1]:
    print("String is Palindrome")
else:
    print("S tring is Not Palindrome")


#3. Given a string, return a new string made of n copies of the first 2 characters of the original string where n is the length of the string. The string length will be >= 2.
s = input("Enter a string: ")
first_two = s[:2]
result = first_two * len(s)
print(result)


#4. Given a string, if the first or last character is 'x', return the string without those 'x' characters, else return the string unchanged.
s = input("Enter a string: ")

if s.startswith("x"):
    s = s[1:]

if s.endswith("x"):
    s = s[:-1]
print(s)


#5. Given a string and an integer n, return a string made of n repetitions of the last n characters of the string.
s = input("Enter a string: ")
n = int(input("Enter n: "))
last = s[-n:]
result = last * n
print(result)