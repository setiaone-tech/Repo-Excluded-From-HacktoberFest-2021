Height=float(input())
Weight=float(input())

BMI = Height/Weight ** 2

if BMI<18.5:
 print("Underweight") 
elif BMI>=30:
 print("Obesity")
elif BMI>=18 and BMI<25: 
 print("Normal") 
elif BMI<=25 and BMI<30:
 print("Overweight")
