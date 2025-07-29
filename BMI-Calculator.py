#Simple BMI Calculator

weight = float(input("Enter weight in kg:"))
height = float(input("Enter height in metres:"))

bmi = weight / (height ** 2)
print("Your BMI is:",round(bmi,2))

if bmi < 18:
    print("Underweight")
    
elif bmi < 24:
    print("Normal")
    
elif bmi < 29:
    print("Overweight")
    
else:
    print("Obese")
