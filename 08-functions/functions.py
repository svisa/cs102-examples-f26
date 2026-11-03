# Functions are a very important part of writing programs.
#	They allow for:
#		* Better code organization and management
#		* Code reuse
#		* Allows for the abstraction of complex functionality


# Currently we have been writing our code in a procedural fashion.
#	Each line of code is executed sequentally from the top down
#	in our python code files.

print("First statement")
print("Second statement")

# To create a function, we first must "define" it. Conceptually this is
#	similar to when we define our variables, but with a bit more syntax.

print("\nFunction Definitions and Function Calls")

def my_cool_function():
    """This function prints out some text"""
    print("I'm running my cool function!")
    
# The keyword "def", meaning define, starts a function declaration.
#	The name that follows is the name you will use when you want to
#	"call" or run our function when you choose to use it. The name
#	of the function above is "my_cool_function". The parenthesis
#	indicate the parameter list. This can hold data that the function
#	needs in order to run. Our function does not require any parameters
#	so the parenthesis are empty. While it is not required, it is good
#	practice to include a "docstring". This is a triple quote (multi-line)
#	string that discusses the purpose of the function. This is a bit different
#	from normal comments and is an appropriate alternate use for a triple
#	quote (multi-line) string. What follows is all of the code necessary
#	to perform the function indented at least one level in the function.

# This is a function call. Notice how it uses the name of the function
#	followed by parenthesis.
my_cool_function()

# Note that my function prints text to the screen. What would happen if
# I wrapped my function call in a print() function?

print(my_cool_function())

# Huh, why did we get "None"? The simple answer is that my function does
#	not return any data after it is called. Dispite seeing the print statement
#	on the screen A PRINT IN NOT A RETURN. "Return" means that a result
#	is sent back to the code that called the function. Print only displays
#	content on the screen. THIS IS NOT THE SAME BEHAVIOR. Let's prove this
#	with a different version of our function.

print("\nReturning Data From a Function")

def my_cool_function_that_returns_data():
    return "I'm returning this string!"

# Notice the use of the keyword "return". This means take whatever
#	result or data that is on the right hand side of the return, stop
#	this fucntion, and send that data back to where it was requested
#	(meaning where the function was called).

my_string_result = my_cool_function_that_returns_data()
print(my_string_result)

# Now, our print works as expected. IT IS VERY VERY IMPORTANT TO NOT
#	CONFUSE PRINT OUTPUT WITH RETURNING DATA FROM A FUNCTION.

# Functions can be declared may places in your code, but this can affect
#	their visibility to other statements. For example, you cannot call
#	a function before it has been defined.

# This WILL NOT WORK because the definition of the function comes AFTER
#	the call to the function.
# print(f"Hello, {display_my_name().title()}!")

def display_my_name():
    return input("What is your name: ")

# For now, always make sure that a function is defined before it
#	is called (top-down in the file). We will talk about a better
#	and flexible approach to this later.
print(f"Hello, {display_my_name().title()}!")

# Previously, we have been defining and calling functions that do
#	not take any input(s). Input to a function is called a parameter.

print("\nFunction Parameters")

def generate_greeting_string(salutation, name, message):
    return f"{salutation} {name}! {message}"

# In the example above, this function has three variables that
#	are the "parameters" or expected input to the function. In the body
#	of our function, we can use these variables like any other
#	variable we have see so far.

sal = "Welcome to CS102"
message = "You are using positional arguments."
my_greeting = generate_greeting_string(sal, "Drew", message)
print(my_greeting)

# When we call the function, we provide "arguments" the actual values to
#	be transferred to the function. In our case, our function provides
#	the arguments sal, "Drew", and message which correspond to the parameters
#	salutation, name, and message. These are "positional" arguments, so
#	THE ORDER MATTERS! The function returns the string it creates and that
#	is stored in my_greeting and subsequently printed.

# Let's say, that we didn't know the order of the function's parameters,
#	but we knew the name of the parameters. Python will allow you to assign
#	an argument to a parameter variable, but the variable name must be
#	EXACTLY the same. This is called a "keyword" argument.

print("\nKeyword Arguments")

message = "You are using keyword arguments."
my_greeting = generate_greeting_string(name="Drew", message=message, salutation=sal)
print(my_greeting)

# Note that although the arguments are not in the same order as the parameters
#	because we used the name of the parameter and assigned the value to it
#	in the function call, Python put the data into the correct parameter variable.

# An inportant thing to remember about functions is that the names
#	need to be unique. If we were to uncomment the code below, we
#	would get an error. Python would not intelligently select the
#	function with the correct number of arguments and call it. Instead
#	our new defintion of the generate_greeting_string completely
#	overwrites the old one. BE CAREFUL TO KEEP FUNCTION NAMES UNIQUE
#	and avoid creating functions that overlap with Python's function
#	like len(), max(), etc.
# def generate_greeting_string():
#     pass
# print(generate_greeting_string("This", "Doesn't", "Work"))

print("\nUnique Function Names")

def len(string):
    print("NOPE!")

# I just broke the len function for this program...
#	don't be like me :)
len("hello")

# Since we can't have functions that are named the same thing
#	with different parameters (some languages support this as
#	a feature called function overloading), Python provides some
#	creative ways to make parameters more flexible.

print("\nDefault Parameter Values")

def my_function_with_a_default_value(greeting, name="User"):
    return f"{greeting} {name}. Pleased to meet you!"

# The function above provides a default value assigned to the
#	"name" parameter, this means if we provide a value for
#	"name", that value will be used. If we omit that data,
#	we will always get "User". It is important to note that
#	all keyword parameters must come after positional parameters
#	(notice how "greeting" comes first) in the parameter list.

# Using the default value
print(my_function_with_a_default_value("Hello"))
# Replacing the default value (with positional arguments)
print(my_function_with_a_default_value("Greetings", "Earthling"))
# Replacing the default value (with keyword arguments)
print(my_function_with_a_default_value(name="Earthling", greeting="Greetings"))

# What if we don't know how many arguments we will need? Python allows
#	for an arbitrary number of arguments.

print("\nArbitrary Arguments: Tuple")

def greeting_many_people(greeting, *people):
    people_string = ""
    for person in people:
        people_string += person + ", "
    
    # Cut off the trailing ", "
    people_string = people_string[:-2]
    
    return f"{greeting} {people_string}!"

# The single "*" for the "*people" parameter says whatever positional argument
#	data we get that doesn't belong in our other parameters will get
#	placed in a tuple of values. This arbitrary parameter must appear
#	last in the list of parameters.
my_arbitrary_greeting = greeting_many_people("hello", "dan", "sarah", "jill", "pete")
print(my_arbitrary_greeting)

# You cannot mix the ordering of positional, keyword, and arbitrary parameters.
#my_arbitrary_greeting = greeting_many_people("dan", greeting="hello", "sarah", "jill", "pete")

# This is not allowed and confuses Python.

# We do have one last option for our arbitrary parameters, and that is to pass
#	an arbitrary number of named arguments to the function.

print("\nArbitrary Arguments: Dictionary")

def personel_details(company_name, address='remote', **employee_data):
    details_string = f"{company_name} ({address})"
    
    for key, value in employee_data.items():
        details_string += f"\n{key}: {value}"
    
    return details_string

# This works similar to the arbitrary parameter that creates a tuple
#	except it uses the double star "**" to say the data should be stored
#	in a dictionary instead of a tuple.

personel = personel_details("Coffee Bytes",
                            name="Paula Peretti", title="CFO", salary=200000)

print(personel)

print("\nFunctions and Lists")

# As we should know, lists are mutable. When we send a list to a function
#	we need to be careful as that list is NOT a copy, but is the original
#	list and its contents.

my_list = ['1', '2', '3']
print(f"Before: {my_list}")

def my_list_modifier(data_list):
    # Change first position
    data_list[0] = "CHANGED"
    data_list[-1] = "DATA"

my_list_modifier(my_list)

print(f"After: {my_list}")

# Notice how the contents of the original list have changed AND
#	out function did not return anything at all. The same thing
#	can happen with dictionaries. If you want to ensure that your
#	original list or dictionary will not be modified, you need to
#	send a copy (you can use the copy() method of a list and dictionary.

print("\nFunctions and Dictionaries")

my_dictionary = {"name":"Pluto", "planet_status":False, "radius":715}
print(f"Before: {my_dictionary}")

def dictionary_modifier(planet_dictionary):
    if "radius" in planet_dictionary:
        # You can remove an dictionary entry and save it's value with pop
        value = planet_dictionary.pop("radius")
        planet_dictionary['diameter'] = value * 2
    
    if "planet_status" in planet_dictionary and not planet_dictionary["planet_status"]:
            # You can remove a dictionary entry and not save anything with del
            del planet_dictionary["planet_status"]

dictionary_modifier(my_dictionary)
print(f"After: {my_dictionary}")

# Sometimes you may want to create a collection of data using a function
#	This can be handy when getting input from a user or other external
#	resource/media so you can manipulate/analyze the data.

string_data = 'aaaabccdddeefggghh'

print("\nReturning a List From a Function")
def generate_char_counts_list(string_input):
    LETTERS = 'abcdefghijklmnopqrstuvwxyz'
    counts = [0 for _ in range(26)]

    for index in range(26):
        counts[index] = string_input.count(LETTERS[index])
    
    return counts

print(generate_char_counts_list(string_data))

print("\nReturning a Dictionary From a Function")
def generate_char_counts_dict(string_input):
    count_dict = {}
    for char in string_input:
        if char not in count_dict:
            count_dict[char] = 1
        else:
            count_dict[char] += 1

    return count_dict

print(generate_char_counts_dict(string_data))
        
print("\nReturning Multiple Values From a Function")

# In addition to returning a dictionary or a list, we can also
#	return multiple individual values. Python takes each of the
#	values, packages them into a tuple and returns that data to
#	the calling code.

def string_statistics(input_string):
    # We can call functions from within function! AWESOME!
    #	Don't rewrite code you've already written.
    string_counts = generate_char_counts_dict(input_string)
    largest_occurrence = None
    for item in string_counts.items():
        if not largest_occurrence:
            largest_occurrence = item
            continue
        
        # Remember "item" is a tuple from the dictionary
        #	position 0 is the key and 1 is the value
        if largest_occurrence[1] < item[1]:
            largest_occurrence = item

    return list(string_counts.keys()), largest_occurrence[0], largest_occurrence[1], 

# We can assign each result in a new variable
unique_letters, most_frequent_letter, frequent_letter_count = string_statistics(string_data)

print(unique_letters)
print(f"{most_frequent_letter}: {frequent_letter_count}")