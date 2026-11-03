# List are an ordered collection of data and can:
#	* Hold mulitple types of data
#	* Be modified (are mutable) unlike strings, integers, etc.

# Lists are one of the most important data structures provided
#	by Python. You will use these relatively often. Make sure
#	you get comfortable with them.

print("Creating Lists")

# Empty list
my_empty_list = []
print(f"An empty list: {my_empty_list}")

# A list that is initialized (assigned values for the first time) with
#	some data
my_integer_list = [1, 2, 3, 4]
print(f"List of numbers: {my_integer_list}")

my_string_list = ['Hi', 'Hola', 'Salut', 'Guten Tag', 'Nei Ho']
print(f"List of strings: {my_string_list}")

mixed_data_list = [1, 'hi', 2, 'hola']
print(f"Mixed data list: {mixed_data_list}")

print("\nAccessing Items in Lists")

# When accessing items in a list, we can do so by an index.
#	This index is the item's position in the list. The VERY
#	IMPORTANT THING TO REMEMBER is that item indexes START
#	AT 0, NOT 1.

# Add the first item from two different lists and a
#	float value
my_sample_list = [my_integer_list[0], my_string_list[0], 1.5]
print(f"Example List Contents: {my_sample_list}")
print(f"The second item in the list is {my_sample_list[1]} at index 1")

# Python has a weird feature that also allows you to use
#	negative indices to access items as well. This means
#	that the index -1 is always the last item in the list.
print(f"Last item in the list is: {my_sample_list[-1]}")

# This little diagram can help you remember index positions
#	Assume a list that is arbitrarily long.
#	 --------------------------------------------
#	| Positive Indices:  |  0  |  1  |  2  |  3  | 
#	 --------------------------------------------
#	|            Items:  | 'a' | 'c' | 'd' | 'e' |
#	 --------------------------------------------
#	| Negative Indices:  | -4  | -3  | -2  | -1  |
#	 --------------------------------------------

# Things to remember:
#	* When using positive integers, the beginning of the list
#	  is always 0 and the end is always the list length - 1
#	* When using negative integers, the end is always -1 and
#	  the beginning of the list is always the list length * -1
#	  or simply -length.

# If you request a positive index that is too large, or a negative
#	index that is too small, your program with crash with an error
#	that the list index you have asked for is out of range. This is
#	commonly referred to as going "out of bounds".

# Example out of bounds negative and positive
#	my_sample_list[3]
#	my_sample_list[-4]

# If you ever need to know how many items are in a list, you can use
#	the len() function
sample_list_length = len(my_sample_list)
print(f"my_sample_list has {sample_list_length} items")

print("\n Adding, Modifying, and Removing Elements")

my_list_method_example = []
print(f"Example List: {my_list_method_example}")

# You can add items to the list using the append() method.
#	This function always adds the item to the end of the list.
my_list_method_example.append("First Item")
my_list_method_example.append("Second Item")
print(f"Example List: {my_list_method_example}")

# If you need to add an item at a specific location in a list
#	you can use the insert() method.
my_list_method_example.insert(0, "Third Item")
print(f"Example List: {my_list_method_example}")
my_list_method_example.insert(1, "Fourth Item")
print(f"Example List: {my_list_method_example}")

# There are a few ways to remove items from a list. Each approach
#	has it's own benefits

# If you want to remove something and you know its index, you can
#	use the del (or delete) keyword. This keyword seems to break our
#	rule that actions like functions and methods need parenthesis.
#	The del keyword however is a special case. It is important to
#	remember that when you use del, the item is simply gone.
del my_list_method_example[0]
print(f"Example List: {my_list_method_example}")

# If you'd like to remove an item from a list, but wish to still
#	use the value for a later purpose, you can use the pop() method.
#	When pop() is used without any arguments (data in between the
#	parenthesis) it automatically removes the last item in the list.
removed_item = my_list_method_example.pop()
print(f"I removed {removed_item}")
print(f"Example List: {my_list_method_example}")

# If you use an index value with pop(), it will remove the item at that
#	posistion in the list.
removed_item = my_list_method_example.pop(0)
print(f"I removed {removed_item}")
print(f"Example List: {my_list_method_example}")

# Last but not least, you can remove an item based on it's value using
#	the remove() method. This method checks the list for the item value
#	you provide and removes THE FIRST OCCURANCE ONLY.
my_list_method_example.remove('First Item')
print(f"Example List: {my_list_method_example}")

print("\nList Sorting and Rearranging")

# Sometimes you have a list and it's important to have the items in
#	a particular order that might not be the same order in which the
#	items were initially added. For example, lets assume we have a list
#	of textbook prices (criminally high, I know...)
textbook_prices = [800, 200, 80, 1500, 70, 123, 55]

# Perhaps it would be beneficial to see the textbook prices sorted.
#	By default, our sorting approaches will sort ascending
#	(small value to big or a-z alphabetical order). We have a few
#	ways we can do this.

# The first option is to sort the list temporarily using the sorted() function.
#	This leaves the original list in place and creates a brand new list in sorted
#	order.
print(f"Textbook Prices: {textbook_prices}")
print(f"Sorted Textbook Prices: {sorted(textbook_prices)}")
print(f"Proof that the original list is still unsorted: {textbook_prices}")

# The second option is to sort the list in-place with the sort() method
# 	which will change the order of the items in the original list.
print(f"Textbook Prices: {textbook_prices}")
textbook_prices.sort()
print(f"Textbook Prices (same list): {textbook_prices}")

# sorted() and sort() can both be given an additional argument to reverse
#	sorting order. This means highest to lowest values or z-a alphabetical order
print(f"Textbook Prices Decending Order: {sorted(textbook_prices, reverse=True)}")

# What the heck is reverse=True?! In Python, sometimes we have named arguements. This
#	just says to the function/method "Please set the reverse option during the sort to True".
textbook_prices.sort(reverse=True)
print(f"Textbook Prices Decending Order: {textbook_prices}")

# Last, but not least, what if we wanted to simply reverse the order of a list? Python
#	has a list method called reverse() that will permanently order the list backwards.
#	Note, this has nothing to do with sorting. The list is simply inverted.
reverse_list = ["hello", "everyone", "how", "are", "you?"]
print(f"{reverse_list}")
reverse_list.reverse()
print(f"{reverse_list}")

print("\nThe List and String Connection...")

# Remember how we said that a string is a collection of characters?
#	Well as it turns out, some of the same things that we can do with lists, we
#	can also do with strings.
my_string = "foobar"
print(f"My string: {my_string}")

# We can get the length
print(f"{my_string} is {len(my_string)} characters long")

# Access a specific character
print(f"The third character is: {my_string[2]}")

# However, you cannot do this:
#	my_string[2] = 'a'
# Remember, strings are immutable...can't be changed in place.

# Sort it, but only with the sorted function. The sort function
#	doesn't work because...again, strings are immutable
print(f"The leters in alphabetical order are: {sorted(my_string)}")
# NOTE that the result of the string being sorted does NOT produce
#	a string, but instead a list of characters...this is an important
#	distinction to make, but this can be a useful operation.

# There is another very useful string and list connection, and that is
#	the string split() method.
my_long_string = "The split function is a very cool method"
print(my_long_string)

# The split() method will divide a string by a specific character
#	and place each part of the string it splits up in a list. By
#	default, split() does so based on a space character ' '.
string_parts = my_long_string.split()
print(string_parts)

# You can split on any character or string
print(f"Split on 'e': {my_long_string.split('e')}")
print(f"Split on 'o': {my_long_string.split('o')}")
print(f"Split on 'is': {my_long_string.split('is')}")

