# Conditional Statements in Python

# if statement
a=13
if(a>10):
    print("a is greater than 10")

# if-else statement
b=5 
if(b>10):
    print("b is greater than 10")
else:
    print("b is not greater than 10")

# if-elif-else statement
c=15

if(c>20):
    print("c is greater than 20")
elif(c>10):
    print("c is greater than 10 but less than or equal to 20")
else:
    print("c is less than or equal to 10")


# practice questions

# 1. accept two numbers and print the greatest between them
# num1=int(input("Enter first number: "))
# num2=int(input("Enter second number: "))

# if(num1>num2):
#     print(f"{num1} is greater than {num2}")
# elif(num2>num1):
#     print(f"{num2} is greater than {num1}")
# else:
#     print(f"{num1} and {num2} is same")




# 2. accept the gender from the user as char and print the respective greeting message

# gender=input("Enter your gender as character (male or female): ")

# if(gender=="male"):
#     print("Good morning Sir")
# elif(geder=="female")
#     print("Good morning mam")
# else:
#     print("Unidentified gender")



# 3. accept an integer and check whether it is an even number not 

# input1= int(input("Enter your number: "))

# if(input1%2==0):
#     print(f"{input1} is an even number")
# else:
#     print(f"{input1} is not an even number")




# 4. accept name and age from the user . check if the user is valid voter or not
# name1= input("Enter your name: ")
# age= int(input("Enter you age: "))

# if(age<18):
#     print(f"hello {name1} you are not a valid voter")
# else:
#     print(f"hello {name1} you are a valid voter")



# 5. accept a year and check if it a leap year or not 
# year=int(input("Enter the year: "))

# if((year%4==0 and year%100!=0) or year%400 == 0):
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")


# 
# t=int(input("Tell your temperature: "))
# if(t<0):
#     print("freezing cold")
# elif(t>=0 and t<10):
#     print("very cold")
# elif(t>=10 and t<20):
#     print("cold")
# elif(t>=20 and 30):
#     print("Pleasant")
# elif(t>=30 and t<40):
#     print("Hot")
# else:
#     print("vey hot")