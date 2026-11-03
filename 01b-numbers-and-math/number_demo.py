# Numbers

print("Number Representations")

# Integers positive or negative whole numbers
my_integer_value = 10 
print(f"{my_integer_value} is an integer")

# Floating point numbers (anything with a decimal point)
my_floating_point_value = 3.141
print(f"{my_floating_point_value} is an floating point number")

# Underscored numbers are supported as separators for large values (like commas)
# e.g 1,500,500,000
my_large_integer = 1_500_500_000
print(f"{my_large_integer} is a big number!")

my_large_float = 2_890_987_453_424.41
print(f"{my_large_float} a big floating point number!")

# Numbers can be represented in scientific notation too
my_sci_int = 1234e50
print(f"Glad I didn't have to type all the zeros in {my_sci_int}")

my_sci_float = 1.2e-5
print(f"I can even represent a floating point number like {my_sci_float} in scientific notation!")


# Mathematical Operations
print("\nMath Operations")

## Addition
# Adding two integers gives you an integer
int_sum_result = 1 + 2 
print(f"1 + 2 = {int_sum_result}")

# Adding a float to an integer or another float results in a floating point result
float_sum_result = 1.4 + 2 
print(f"1.4 + 2 = {float_sum_result}")

# You can also use the addition operator to combine two strings.
#	This operation is called "concatenation".
str1 = "hello"
str2 = "goodbye"
print(f"'hello' + 'goodbye' = {str1 + str2}")

## Multiplication
# Adding two integers gives you an integer
int_product_result = 1 * 2 
print(f"1 * 2 = {int_product_result}")

# Adding a float to an integer or another float results in a floating point result
float_product_result = 1.4 * 2 
print(f"1.4 * 2 = {float_product_result}")

# You can also use the multiplication operator to cause a string to repeat
repeat_count = 3
print(f"{str1 * repeat_count}")

## Subtration
# Subtracting two integers gives you an integer
int_subtract_result = 1 - 2 
print(f"1 - 2 = {int_subtract_result}")

# Subtracting a float to an integer or another float results in a floating point result
float_subtract_result = 2 - 1.4 
print(f"2 - 1.4 = {float_subtract_result}")
# Why does the result above seem a bit off? The book talks about it! :)

## Division
# Dividing two numbers always results in a floating point number
quotient_result = 5 / 2
print(f"5 / 2 = {quotient_result}")

# You can use a special operation (//) to perform integer division
int_quotient_result = 5 // 2
print(f"5 // 2 = {int_quotient_result}")
# Note that this performs the division "correctly" but just drops the result
#	after the decimal point.

# Another operation that is related to division is modulus (%)
#	Modulus division performs division but the result is the remainder of the operation
mod_result = 5 % 2
print(f"5 % 2 = {mod_result}") 
# 5 / 2 does so with a remainder of 1
mod_result = 4 % 2
print(f"4 % 2 = {mod_result}")
# 4 / 2 does not have a remainder as 4 can be divided evenly by two

## Exponents
power_of_5 = 2 ** 5 # Two to the power of 5
print(f"2 ** 5 = {power_of_5}")

print("\nOrder of Operations")

# Python follows the standard order of operations present in mathematics
#	You might know this as the acronym PEMDAS (indented to indicate precidence):
#	P - Parenthesis
#		E - Exponents
#			M - Multiplication
#			D - Division
#				A - Addition
#				S - Subtraction

#	It is worth remembering that Multiplication and Division have the same
#	precedence or priority. This means to can perform either operation as
#	you encounter them when reading an expression from left to right. The
#	PEMDAS ancronym does not imply you have to do all multiplication before
#	division. The same applies with Addition and Subtraction which have like
#	precidence. The PEMDAS has been grouped above to illustrate this concept.

# The only element of an expression that has higher precidence than
#	these mathematical operations is the execution of functions in
#	an expression (we'll see this a lot more often later). This makes
#	sense intuitively, as we would need the output or result of a
#	function before we could perform a mathematical operation on the value.

expression_result = 1 + 2 * 5
print(f"1 + 2 * 5 = {expression_result}")
expression_result = (1 + 2) * 5
print(f"(1 + 2) * 5 = {expression_result}")
# You an use parenthesis to change the order of operations

expression_result = 6 / 3 ** 2 + 1 * 5
print(f"6 / 3 ** 2 + 1 * 5 = {expression_result}")
expression_result = ((6 / (3 ** 2)) + (1 * 5)) # Equivalent to the statement above
print(f"((6 / (3 ** 2)) + (1 * 5)) = {expression_result}")
# You could also use it to visually assist readers for the order of operations.
#	The full parenthesization above is a bit excessive here and only
#	used to demonstrate the point.

expression_result = 6 / 3**2 + 1 * 5
print(f"6 / 3**2 + 1 * 5 = {expression_result}")
# You can also use spacing to help visually identify terms

print("\nMultiple Assignments")

# We have looked at normal assignment of variables like the ones below:
a = 10
b = 11
c = 12
print(f"{a}, {b}, {c}")

# Sometimes we may want to give values to multiple variables
#	in a more compact way
x, y, z = 20, 21, 22
print(f"{x}, {y}, {z}")
# While the result of these two operations have equivalent outcomes
#	(assigning three values to three variables), you can use this to
#	help group and initialize (provide an inital value) your variables
#	for easier reading. You could also use this notation if a function
#	happens to output more than one result. In this case, each variable
#	could reference one piece of output data from the function. This can
#	be very convenient in some circumstances.

# Suppose we want to get numeric data from a user with our input() function.
my_number = input("Enter an integer: ")

# The problem here is that my_number...isn't a number, input only gets string data.
#   To fix this, we will need to convert our string to a numeric value. We can use
#   the int() function to try and convert a string into a number. We say "try" here
#   because if the input cannot be converted to a number, the function will fail.

# For our purposes here, we will reassign the converted number back to our original variable
my_number = int(my_number)

# We call this operation "casting", or converting a value from one type to another

# If our value were a floating point number like 3.141, we need to use the float() function
#   to ensure that we keep the decimal portion of the value.
my_floating_point_number = "Enter a floating point value: "
my_floating_point_number = float(my_floating_point_number)

print(f"My integer is {my_number} and my float value is {my_floating_point_number}")
