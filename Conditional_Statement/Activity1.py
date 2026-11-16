
print("What is the temperature today?")
Temperature=int(input())
if Temperature < 20:
    outfit="Jacket"
    print("It is very cold today")
    print("Wear:",outfit)
else:
    outfit = "T-shirt"
    print("It is hot today")
    print("Wear:",outfit)
is_raining= input("Is it raining today? (yes/no")
if is_raining=="yes":
    print("Bring an umbrella")
wind_speed = int(input("Enter the wind speed in km or h :"))
if wind_speed > 30:
    needs_windbreaker = "yes"
    print("Its wind today")
    print("Wear a windbreaker over your :", outfit)
else:
    needs_windbreaker = "no"
    print("The wind is calm today")
    print("No need to wear a windbreaker over your :", outfit)
has_puddles = input("Are there puddles on the ground")
if has_puddles == "yes":
    print("The ground is wet")