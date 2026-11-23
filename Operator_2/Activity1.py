print("Smart School Day Planner")
Weather=input("How is the Weather like(Sunny/Cloudy/Rainy)?").capitalize()
Homework=input("Have you completed your Homework? (yes/no)").capitalize()
day=input("What Day is it today(Monday to Saturday)?").capitalize()

print()
print(f"==Your Plan For{day}")
print("-"*35)
if day in ("Saturday", "Sunday"):
    print("Day time  enjoy your free time!")
elif day==("Monday"):
    print(" Day type:  First day of the week get ready for school!")
elif day==("Friday"):
    print("Day type:  Last day of school you need  to return books")
elif day in ("Tuesday","Wednesday","Thursday"):
    print("Midday of the week ")