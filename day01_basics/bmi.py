height=float(input("whats your height in cm ?\n"))
weight=float(input("whats your weight ?\n"))

bmi = weight/(height**2)

if bmi<18.5:
    print("underweight")
elif 18.5<=bmi<25:
    print("normal weight")
else:
    print("overweight")