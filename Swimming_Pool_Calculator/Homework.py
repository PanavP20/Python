print("--Swimming Pool Entry Checker--")

age = int(input("How old are you?"))
can_swim = input("Can you swim 25 meters?  (yes/no) : ").strip().lower()
adult_here = input("Is an adult here with you   (yes/no?").strip().lower()
print("/n")
print("--Entry Descion--")
print("-" * 32)
if age < 4 :
    print("Age group    : Toddler")
elif age < 12 :
    print("Age group    : Child")
elif age < 18 :
    print("Age group    : Teen")
else :
    print("Age group    : Adult")
if can_swim == "yes" and adult_here == "yes" :
    print("Deep pool     :Allowed - you can swim and an adult is with you.")
if age < 12 or can_swim == "no":
    print("Shallow end : stay in the shallow end today.")
if not (adult_here == "yes"):
    print("Reminder-  No adult with you tell the life-guard")