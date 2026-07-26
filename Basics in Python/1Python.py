print("Hello world");

# 1. Comments in Python- 
# Comments are something that are ignored by the python interpreter
# We have to use for writing a comment in python
#  Multiline comments are not available in python but we can achieve it by using Doc String """ multiline comment """

# 2. Variables in Python-
# In python Variables are used as a storage to store things in python (we will see later what we have to store)
# You can write anything as a variable name.

# name="Ani"
# age=

# Don’t use these
# 1. You can not use numbers at variable start
# 2. You can not use spaces in variables.
# 3. You should not use special characters in variables.

# Naming Conventions
# You can write variables in python using 3 ways
# Camel case - sheryiansSchool
# Pascal case -SheryiansSchool
# Snake case- sheryians_school  


# 3. What are Data Types
# Data types are the things we store in Variables and it defines what data type variables are.
# Python has built-in data types for different kinds of data.

# Numbers
# 1. Integer- It is a whole number without a decimal point. Example- 1, 2, 3, -4, 0
age = 10 
a1 = -34

# 2. Float- It is a number that has a decimal point. Example- 3.14, -0.5, 0.0
b1=56.8
c1=12/2

# 3. complex - It is a number that has a real part and an imaginary part. Example- 2 + 3j, -1 - 4j
d1= 2+3j
e1=6j

# String- It is a sequence of characters. and used to store anything in python, Example- "Hello", 'Python', "123"
name="Ani"
print(type(name));

# Boolean- It is a data type that can only have two values: True or False. Example- True, False
is_student = True
is_teacher = False


# 4. Strings and type convertions

a2="A";
print(ord(a2)); # ord() function is used to get the ASCII value of a character 

print(chr(65)); # chr() function is used to get the character of an ASCII value
 
# 5. String indexing 
a3="Sheryians"
print(a3[1]); # it will print the character at index 1 which is 'h'
print(a3[-1]); # it will print the last character of the string which is 's'
print(a3[5]); # it will print the character at index 5 which is 'i'

# 6. String slicing
a4="Sheryians"
print(a4[0:5]); # it will print the characters from index 0 to 4 which is 'Shery'
print(a4[5:]); # it will print the characters from index 5 to the end which is 'ians'
print(a4[:5]); # it will print the characters from the beginning to index 4 which


# 7. Type conversions - used to convert one data type to another data type
a5=10
b5 = float(a5) # it will convert the integer 10 to float 10.0
print(b5);

c5=0;
print(bool(c5)); # it will convert the integer 0 to boolean False



# 8 Input and Output in Python
# Output-
# There is no other functions to provide the result on the terminal we just have to use print() function
name = input("Enter your name: ") # it will take input from the user and store it in the variable name
print(f"Hello {name}"); # it will print the value of name variable in the output( i am using formatted string to print the value of name variable)

age = int(input("Enter your age: ")) # it will take input from the user and convert it to integer and store it in the variable age
print(f"You are {age} years old"); # it will print the value of age variable in the output
