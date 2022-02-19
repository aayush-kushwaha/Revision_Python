# Tip Calculator
# 7 people splitting
# 15% service tax
print("Hello!! Welcome to Tip Calculator")
bill = input("Enter total bill:")
num = input("Enter number of people:")
split_amount = int(bill)/int(num)
service_tax = input("Enter the amount of service tax:")
final_bill = int(split_amount)+int(service_tax)
print("The final bill is:", final_bill)