import name_modules
name = input("Enter your name: ")
print(name_modules.ispalindrome(name))
print("No of vowels:", name_modules.count_the_vowels(name))
print("Frequency of letters:")

frequency = name_modules.frequency_of_letters(name)
for letter, count in frequency.items():
    print(f"{letter}-{count}", end=", ")