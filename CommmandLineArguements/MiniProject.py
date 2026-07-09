#Project 1 Happiness
import sys

# Take command line arguments
string1 = sys.argv[1].split("-")
string2 = sys.argv[2].split("-")
string3 = sys.argv[3].split("-")

happiness = 0

for num in string3:
    if num in string1:
        happiness += 1
    elif num in string2:
        happiness -= 1

print("Final Happiness =", happiness)


'''#How to Run
Example 1
python program.py 3-1 5-7 1-5-3-8

Output

Final Happiness = 1
Example 2
python program.py 60-77-34-5-2 44-11-99-3 77-15-13-2-34-3

Output

Final Happiness = 2
'''