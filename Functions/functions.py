#1. Write a function to return the sum of all numbers in a list.
def sum_list(numbers):
    total = 0

    for i in numbers:
        total = total + i

    return total
numbers = [8, 2, 3, 0, 7]
print(sum_list(numbers))

#2. Write a function to return the reverse of a string.
def reverse_string(text):
    return text[::-1]

string = "1234abcd"
print(reverse_string(string))

#3. Write a function to calculate and return the factorial of a number (a non-negative integer).
def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i

    return fact

number = int(input("Enter a number: "))
print(factorial(number))


#4. Write a function that accepts a string and prints the number of upper case letters and lower case letters in it.
def count_case(text):
    upper = 0
    lower = 0
    for ch in text:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1

    print("Uppercase letters:", upper)
    print("Lowercase letters:", lower)

string = input("Enter a string: ")
count_case(string)

#5. Write a function to print the even numbers from a given list. The list is passed to the function as an argument.
def print_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(num)

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print_even(list1)

#6. Write a function that takes a number as a parameter and checks whether the number is prime or not.
def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True
number = int(input("Enter a number: "))

if is_prime(number):
    print("Prime Number")
else:
    print("Not a Prime Number")



