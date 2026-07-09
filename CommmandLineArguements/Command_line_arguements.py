#1. Write a program to accept two numbers as command line arguments and display their sum.

import sys
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
print("Sum =", num1 + num2)

#Run Command:
python program.py 10 20

#2. Write a program to accept a welcome message through command line arguments and display the file name along with the welcome message.

import sys
print("File Name :", sys.argv[0])
print("Welcome Message :", sys.argv[1])

#Run Command:
python program.py Welcome

#3. Write a program to accept 10 numbers through command line arguments and calculate the sum of prime numbers among them.

import sys
sum_prime = 0
for i in range(1, 11):
    num = int(sys.argv[i])

    if num > 1:
        is_prime = True

        for j in range(2, num):
            if num % j == 0:
                is_prime = False
                break

        if is_prime:
            sum_prime += num
print("Sum of Prime Numbers =", sum_prime)

#Run Command
python program.py 2 3 4 5 6 7 8 9 10 11
