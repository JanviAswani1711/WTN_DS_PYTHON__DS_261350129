# Program to calculate purchase details from a file

try:
    filename = input("Enter the file name: ")
    file = open(filename, "r")
  
    item_count = 0
    free_count = 0
    total_amount = 0
    discount = 0

    for line in file:
        line = line.strip()

        if line == "":
            continue
        data = line.split()
        item = data[0]
        price = data[1]

        if item.lower() == "discount":
            discount = int(price)

        elif price.lower() == "free":
            free_count += 1

        else:
            item_count += 1
            total_amount += int(price)

    final_amount = total_amount - discount

    print("No of items purchased:", item_count)
    print("No of free items:", free_count)
    print("Amount to pay:", total_amount)
    print("Discount given:", discount)
    print("Final amount paid:", final_amount)

    file.close()

except FileNotFoundError:
    print("Error: File not found.")

except Exception as e:
    print("Error:", e)