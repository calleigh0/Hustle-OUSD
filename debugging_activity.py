# Debugging Activity Calleigh Tanaka

# Code Snippet 1: 
print("Code Snippet 1: ")
# Incorrect: encountered a divisionbyzero came up as an attempt to divide by 0, fixed by dividing by 5
x = 10
y = 5
result = x / y
print("Result:", result)

#Code Snippet 2:
# Incorrect: encountered a listindexoutofrange, fixed by changing 1 to a 0
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
   print(numbers[i+0])

#Code Snippet 3:
# Incorrect: encountered syntaxerror, fixed by adding ":"
def calculate_area(radius):
   area = 3.14 * radius ** 2
   return area
 
radius = 5
print(calculate_area(radius))

#Code Snippet 4:
# Incorrect: encountered syntaxerror, fixed by adding ":"
def is_even(number):
   if number % 2 == 0:
       return True
   else:
       return False
 
print(is_even(4))
print(is_even(7))

#Code Snippet 5:
# Incorrect: encountered syntaxerror, fixed by adding ":"
for i in range(5):
   print(i)

#Code Snippet 6:
# Incorrect: encountered sytaxerror, fixed by adding "+"
def greet(name):
   return "Hello, " + name
 
print(greet("Alice"))

#Code Snippet 7:
# Incorrect: encountered indentationerror, fixed by indenting
numbers = [1, 2, 3, 4, 5]
sum = 0
for number in numbers:
    sum += number
print("Sum of numbers:", sum)

#Code Snippet 8:
# Incorrect: encountered recursionerror, fixed by changing "+" for "-"
def factorial(n):
   if n == 0:
       return 1
   else:
       return n * factorial(n-1)

print(factorial(5))

#Code Snippet 9:
# Incorrect: encountered technical error, fixed by adding "()"
name = input("Enter your name: ")
if name == ("Alice" or "Bob"):
   print("Hello, " + name)
else:
   print("Hello, stranger!")

#Code Snippet 10:
# Incorrect: encountered zerodivisionerror, fixed by changing 0 for 2
def divide_numbers(x, y):
   result = x / y
   return result
 
num1 = 10
num2 = 2
print(divide_numbers(num1, num2))
