 # for loop--------------------------------------------

# for i in range(1,21,1):
#     print(i)

# 1. lets print a table of 5

# for i in range(5,51,5):
#     print(i);

# by taking user input---------
# num=int(input("Enter your number: "))
# for i in range(num,num*10+1,num):
#     print(i);


# for loops for strings---------

# 1st method- by using index
# a=input("Enter your word: ")
# for i in range(len(a)):
#     print(a[i]);


# 2nd method- direct method
# b = input("Enter your word: ")
# for i in b:
#     print(i);



# break statement

# for i in range(1,21):
#     if(i==16):
#         break;
#     else:
#         print(i);

# continue statement

# for i in range(1,21):
#     if(i==13):
#         continue;
#     else:
#         print(i);


# else statement

# for i in range(1,21):
#     if(i==44):
#         print("break statement is executed")
#         break;
# else:
#     print("break statement is not executed")


# WHILE LOOP------------------------------------------------

  



# for loop Practice questions-------------------------------------------------

# 1. accept an integer and print hello world n times

# num1= int(input("Enter the integer: "))
# for i in range(num1):
#     print("Hello World")

# 2. Print natural number upto n

# num2= int(input("Enter you number: "))
# for i in range(1,num2+1):
#     print(i);

# 3. Reverse for loop . print n to 1

# num3 = int(input("ENter your number: "))
# for i in range(num3,0,-1):
#     print(i);


# 4. Take a number as a input and print its table

# num4= int(input("Enter you table number: "))
# for i in range(num4,num4*10+1,num4):
#      print(i)


# 5. sum upto n terms

# num5=int(input("Enter your number: "))
# sum = 0;
# for i in range(1,num5+1):
#     sum+=i;
# print(f"Your sum is {sum}")


# 6. factorial of a number
# n=int(input("enter your number: "))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(f"Your factorial is {fact}")


# 7. print the sum of all even & odd numbers in a range separately

# n= int(input("Enter your number: "))
# sum1=0
# sum2=0

# for i in range(1,n+1):
#     if(i%2==0):
#         sum1=sum1+i   
#     else:
#         sum2=sum2+i
       
# print(f"Sum of even numbers are {sum1}")
# print(f"Sum of odd numbers are {sum2}")


# 8. Print all the factors of a number

# n=int(input("Enter your number: "))
# for i in range(1,n+1):
#     if(n%i==0):
#         print(i)


# 9. Accept a number and check if it a perfect number or not. A number whoes sum of factors is equal to the number itself
# n=int(input("Enter your number: "))
# sum=0
# for i in range(1,n):
#     if(n%i==0):
#         sum=sum+i;
# if(n==sum):
#     print(f"{n} is a perfect number")
# else:
#     print(f"{n} is not a perfect number")



# 10. check whether the number is prime or not
# n=int(input("Enter your number: "))

# count=0
# for i in range(1,n+1):
#     if(n%i==0):
#         count=count+1
# if(count==2):
#     print(f"{n} is a prime number")
# else:
#     print(f"{n} is not a prime number")



# 11. reverse a string without using the in build function

# n=input("Enter you word: ")
# for i in range(len(n)-1,-1,-1):
#     print(n[i])


# 12. check string is palindrome or not

# n=input("Enter your word: ")
# b=""
# for i in range(len(n)-1,-1,-1):
#     b=b+n[i]
# if(b==n):
#     print("Number is palindrome")
# else:
#     print("Number is not palindrome")


# 13. check all letter , digits and special symbols from a given string

# n=input("Enter your string: ")
# letter=0
# digit=0
# symbols=0

# for i in n:
#     if(i.isdigit()):
#         digit+=1
#     elif(i.isalpha()):
#         letter+=1
#     else:
#         symbols+=1
# print(f"your digits are {digit}\n your letters are {letter}\n your symbols are {symbols}")



# WHILE LOOP PRACTICE QUESTIONS------------------------------------------------------------------------

#1. separate each digit of a number and print it on a new line

# n=int(input("Enter your number: "))
# while n>0:
#     print(n%10)
#     n= n//10


# 2. Accept a number and print its reverse

# n=int(input("Enter your number: "))
# rev=0
# while n>0:
#     a=n%10
#     rev=rev*10+a
#     n=n//10
# print(rev)


# 3. Accept a number and check if it is a pallindromic number (if number and its reverse are equal)
# n=int(input("Enter your number: "))
# copy=n
# rev=0
# while n>0:
#     a=n%10
#     rev=rev*10+a
#     n=n//10
# if(copy==rev):
#     print(f"{copy} is palindromic")
# else:
#     print(f"{copy} is not palindromic")




    