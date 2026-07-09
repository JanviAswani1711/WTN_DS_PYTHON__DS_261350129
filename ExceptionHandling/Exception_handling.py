#1. Write a program to accept two numbers from the user and perform division. 
#If any exception occurs, print an error message; otherwise, print the result.

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2

except Exception as e:
    print("Error:", e)

else:
    print("Result =", result)

#2. Write a program to accept a number from the user and check whether it is prime or not. If the user enters anything other than a number, handle the exception and print an error message.

try:
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
            print("Prime Number")
        else:
            print("Not Prime")
except ValueError:
    print("Error: Please enter a valid number.")


#3. Write a program to accept the file name to be opened from the user. If the file exists, print the contents of the file in title case; otherwise, handle the exception and print an error message.
try:
    filename = input("Enter file name: ")
    file = open(filename, "r")
    content = file.read()
    print(content.title())
    file.close()

except FileNotFoundError:
    print("Error: File not found.")


#4. Declare a list with 10 integers and ask the user to enter an index. Check whether the number at that index is positive or negative. If any invalid index is entered, handle the exception and print an error message.

numbers = [12, -5, 8, -10, 15, -3, 20, -7, 9, -1]
try:
    index = int(input("Enter index (0-9): "))
    if numbers[index] >= 0:
        print("Positive Number")
    else:
        print("Negative Number")

except IndexError:
    print("Error: Invalid index.")

except ValueError:
    print("Error: Please enter a valid integer.")