# 1. Arithmatic Operators:
a=30
b=5

print("a+b=", a+b) # Addition
print("a-b=", a-b) # Subtraction    
print("a*b=", a*b) # Multiplication
print("a/b=", a/b) # Division 
print("a//b=", a//b) # Floor Division - returns the quotient in integer form
print("a%b=", a%b) # Modulus - returns the remainder after division
print("2**3=", 2**3) # Exponentiation - returns the value of 2 raised to the power of 3

# 2. Assignment Operators: 
a= 20;

# compound assignment operators are used to assign values to variables with an operation.
a += 5 # a = a + 5
print("a after addition:", a)

a +=20;
a +=40;
a +=60;
print("a after multiple additions:", a)

a -= 10 # a = a - 10
print("a after subtraction:", a)

a *= 2 # a = a * 2
print("a after multiplication:", a)

a /= 4 # a = a / 4
print("a after division:", a)

# 3. Comparison Operators:

x=100;
y=200;

print("x == y:", x == y) # Equal to
print("x != y:", x != y) # Not equal to
print("x > y:", x > y) # Greater than
print("x < y:", x < y) # Less than
print("x >= y:", x >= y) # Greater than or equal to
print("x <= y:", x <= y) # Less than or equal to

# comparison operators also work on strings, by using ASCII values of characters.
str1 = "A"
str2 = "B"
print(ord(str1), ord(str2)) # ASCII values of 'A' and 'B
print("str1 == str2:", str1 == str2) # Equal to
print("str1 != str2:", str1 != str2) # Not equal to


# 4. Logical Operators:

print(123>100 and 50<100) # Logical AND - returns True if both conditions are true
print(123>100 or 50>100) # Logical OR - returns True if at

# least one condition is true
print(not(123>100)) # Logical NOT - returns True if the condition is false
