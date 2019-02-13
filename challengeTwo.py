current_year = 2019

result = int(input("Enter your year of Birth: "))

age = (current_year - result)

if age < 18:
    print("you are a Minor!")
elif age == 18 or age <= 36:
    print("Your are a Youth")
else:
    print("You are an Elder")
