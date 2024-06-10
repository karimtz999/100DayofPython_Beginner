height = float(input("enter your height in m :"))
weight = float(input("enter your wieght in kg :"))
# bmi = round(weight / height ** 2
bmi = 25
if bmi < 18.5 :
    print (f"your bmi is {bmi},underweight.")
elif bmi < 25:
        print(f"your bmi is {bmi}, you have normal bmi.")
elif bmi < 30:
            print(f"your bmi is {bmi},you are overwieght.")
elif bmi < 35:
                print(f"your bmi is {bmi}, you areclinically obese") 

