from utils.dec_truncate import truncate
#Input from user
weight = float(input("Enter your weight in (kg):"))
height = float(input("Enter your height in (cm):"))
height_m = height / 100
bmi = weight / (height_m ** 2)

print(f"\nBMI: {(truncate(bmi))}")
if bmi <= 18.5:
    print("Under-weight")
elif 18.5 <= bmi <= 24.9:
    print("Normal-weight")
elif 25.0 <= bmi <= 29.9:
    print("Over-weight")
else :
    print("Obese")