print("Enter marks obtained in all 5 tests")
markOne= int(input())
markTwo= int(input())
markThree= int(input())
markFour= int(input())
markFive= int(input())
tot= markOne + markTwo + markThree + markFour + markFive
average= int(tot/5)
valid_range = (0,101)
print("Average",average)
if average in range(91,101):
    print("Your grade is A1")
elif average in range(81,91):
    print("Your grade is A2")
elif average in range(71,81):
    print("Your grade is B1")
elif average in range(61,71):
    print("Your grade is B2")
elif average in range(51,61):
    print("Your grade is C1")
elif average in range(41,51):
    print("Your grade is C2")
elif average in range(33,41):
    print("Your grade is D")
elif average in range(21,33):
    print("Your grade is E")
elif average in range(0,21):
    print("Your grade is F")