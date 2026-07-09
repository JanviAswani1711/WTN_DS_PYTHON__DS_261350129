#Project 1: People and facts
# Dictionary containing people and their interesting facts

people = {
    "Jeff": "Is afraid of Dogs.",
    "David": "Plays the piano.",
    "Jason": "Can fly an airplane."
}

# Display original dictionary
print("Original Dictionary:\n")

for name, fact in people.items():
    print(name + ":", fact)

# Change Jeff's fact
people["Jeff"] = "Is afraid of heights."

# Add a new person
people["Jill"] = "Can hula dance."

# Display updated dictionary
print("\nUpdated Dictionary:\n")

for name, fact in people.items():
    print(name + ":", fact)


#Output
Original Dictionary:

Jeff: Is afraid of Dogs.
David: Plays the piano.
Jason: Can fly an airplane.

Updated Dictionary:

Jeff: Is afraid of heights.
David: Plays the piano.
Jason: Can fly an airplane.
Jill: Can hula dance.

#Project 2: Find the Runner_up score 
# Program to find runner-up score

scores = list(map(int, input("Enter the scores separated by space: ").split()))
scores = list(set(scores))
scores.sort()
print("Runner-up score:", scores[-2])

#Project 3: Find the Percentage
# Program to find average marks

students = {
    "Krishna": [67, 68, 69],
    "Arjun": [70, 98, 63],
    "Malika": [52, 56, 60]
}

name = input("Enter a name: ")
marks = students[name]
total = 0

for mark in marks:
    total = total + mark

average = total / len(marks)
print("Average percentage mark:", average)

#Project 4: FInd the name
# Program to count the number of times "Alex" appears in a string

text = input("Enter a string: ")
words = text.split()
count = 0

for word in words:
    if "Alex" in word:
        count = count + 1

print("Number of times Alex appears:", count)