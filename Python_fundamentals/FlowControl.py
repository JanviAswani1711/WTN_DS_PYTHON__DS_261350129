# 1. Write a program to check if a given number is Positive, Negative, or Zero.

num = int(input("Enter a number: "))
if num > 0:
    print("The number is Positive")
elif num < 0:
    print("The number is Negative")
else:
    print("The number is Zero")

# 2. Write a program to check if a given number is odd or even.

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")
    

''' 3. Given two non-negative values, print true if they have the same last digit (for example, 27 and 57 have the same last digit).
Examples:
lastDigit(7, 17) → true
lastDigit(6, 17) → false
lastDigit(3, 113) → true'''

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 % 10 == num2 % 10:
    print(True)
else:
    print(False)


# 4. Write a program to print numbers from 1 to 10 in a single row with one tab space between each number.
for i in range(1, 11):
    print(i, end="\t")

# 5. Write a program to print even numbers between 23 and 57. Each number should be printed on a separate line.
for i in range(23, 58):
    if i % 2 == 0:
        print(i)
        
# 6. Write a program to check if a given number is prime or not.
num = int(input("Enter a number: "))
if num <= 1:
    print("Not Prime")
else:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime")
    else:
        print("Not Prime")
        
# 7. Write a program to print all prime numbers between 10 and 99.
for num in range(10, 100):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)
        
        
''' 8.Write a program to print the sum of all the digits of a given number.
Example:
Input: 1234
Output: 10'''

num = int(input("Enter a number: "))
sum = 0
while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10
print("Sum of digits =", sum)

'''9.Write a program to reverse a given number and print it.
Example 1:
Input: 1234
Output: 4321

Example 2:
Input: 1004
Output: 4001'''

num = int(input("Enter a number: "))
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed number =", reverse)



'''10.Write a program to find whether the given number is a palindrome or not.
Example 1:
Input: 110011
Output: 110011 is a palindrome.

Example 2:
Input: 1234
Output: 1234 is not a palindrome.'''

num = int(input("Enter a number: "))
original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print(original, "is a palindrome.")
else:
    print(original, "is not a palindrome.")