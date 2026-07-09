#Project 1 (Ride on Miles)
distance = float(input("Enter the distance to travel (in miles): "))

if distance < 3:
    print("I suggest you ride a Bicycle.")
elif distance >= 3 and distance < 300:
    print("I suggest you ride a Motor-Cycle.")
else:
    print("I suggest you drive a Super-Car.")


#Project 2

cost_per_hour = 0.51
cost_per_day = cost_per_hour * 24
cost_per_week = cost_per_day * 7
cost_per_month = cost_per_day * 30

budget = 918
days = budget / cost_per_day

print(f"Cost to operate one server per day: ${cost_per_day:.2f}")
print(f"Cost to operate one server per week: ${cost_per_week:.2f}")
print(f"Cost to operate one server per month: ${cost_per_month:.2f}")
print(f"One server can operate for {days:.0f} days with ${budget}.")