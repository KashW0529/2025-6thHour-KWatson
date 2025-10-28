#Name: Kash
#Class: 6th Hour
#Assignment: SC2


#A local health clinic is looking to add a quick BMI calculator to their website so that their
#patients can quickly input their height and weight and be given a number as well as their
#classification. The classifications are as follows:

# - Underweight: Less than 18.5 BMI
# - Normal Weight: 18.5 to 24.9 BMI
# - Overweight: 25 to 29.9 BMI
# - Obese: 30 or more BMI

#It is up to you to figure out the calculation for an accurate BMI reading and tying it to
#the right classification

#Code Here

Weight = int(input("Enter your weight in Pounds: "))
print(Weight)
Height = int(input("Enter your height in Inches: "))
print(Height)

BMI = (Weight/(int(Height)** 2 ))*703
print(round(BMI,1))


if BMI < 18.5:
    print('You are under weight')
elif BMI > 19 and BMI < 25:
    print('You are normal weight')
elif BMI >= 25 and BMI < 30:
    print('You are over weight')
elif BMI >= 30 and BMI < 35:
    print('You are abeast')
