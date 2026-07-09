#Project 1 : Find the Secret

# Program to find meeting time and meeting place

filename = input("Enter the file name: ")
file = open(filename, "r")
lines = file.readlines()


# Finding Meeting Time

line_count = len(lines)

if line_count == 12:
    meeting_time = "12 PM"
elif line_count > 12:
    meeting_time = str(line_count - 12) + " PM"
else:
    meeting_time = str(line_count) + " AM"


# Finding Meeting Place

word_count = {}
for line in lines:
    words = line.split()
    for word in words:

        word = word.strip(".,!?;:\"'()").lower()

        if word != "":
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

max_word = ""
max_count = 0

for word in word_count:

    if word_count[word] > max_count:
        max_count = word_count[word]
        max_word = word

print("Meeting time:", meeting_time)
print("Meeting place:", max_word.capitalize(), "Street")
file.close()

'''#Sample Output 1
If file has 9 lines and word park occurs maximum times.
Enter the file name: Sample.txt

Meeting time: 9 AM
Meeting place: Park Street

#Sample Output 2
If file has 20 lines and word Apollo occurs maximum times.
Enter the file name: Sample.txt

Meeting time: 8 PM
Meeting place: Apollo Street
'''