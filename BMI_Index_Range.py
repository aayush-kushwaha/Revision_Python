print("Welcome to BMI Range Calculator:")
height = input("Enter Height in meter: ")
weight = input("Enter weight in kg: ")
BMI = float(weight)/float(height) ** 2
if BMI < 18.5:
    print(f"You are Underweight! and your BMI is {BMI}")
elif BMI > 18.5 and BMI < 24.9:
    print(f"You are in Healthy Weight.. and your BMI is {BMI}")
elif BMI > 25 and BMI < 29.9:
    print(f"You are Overweight!! and your BMI is {BMI}")
else:
    print(f"You are Obese and your BMI is {BMI}")

 