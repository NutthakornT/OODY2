hw = input("Enter your High and Weight : ")
hw = hw.split(" ")
height = float(hw[0])
weight = int(hw[1])
# print(height)
bmi = weight / (height**2)
if bmi >= 30:
    print("Fat")
elif bmi >= 25:
    print("Getting Fat")
elif bmi >= 23:
    print("More than Normal Weight")
elif bmi >= 18.50:
    print("Normal Weight")
elif bmi < 18.50:
    print("Less Weight")
