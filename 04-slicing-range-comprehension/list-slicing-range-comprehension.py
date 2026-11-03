print("Slicing Lists")

# List slicing can be very useful in Python to create a new list
#	with a subset of items from am orginal list. Let's assume we
#	have a list of scores on an exam.

exam_scores = [50, 15, 100, 75, 40, 88, 99, 87, 66, 78, 89]

# Suppose we wanted the top N scores. We could first sort the list,
#	and then create a slice with the just the highest N scores in it.

exam_scores.sort(reverse=True)
# Remember, this sorts in place modifying the orignal list. Reverse allows
#	the sort to be decending (High to low values "left" to "right")

# Let's take the top 5
top_five = exam_scores[0:5]
print(f"The top five scores are: {top_five}")

# Notice that we used our notation to access positions in the list using
#	square brackets "[]", but now we have two index values separated by a
#	colon ":". This basically means, [start index : end index]. IT IS IMPORTANT
#	TO NOTE THAT start_index **IS** INCLUSIVE while "end_index" IS **NOT** INCLUSIVE.
#	We ended with the index value 5, but our last value is actually at index 4.

# Let's try and get the five lowest scores from our list
lowest_five = exam_scores[-6:-1]
print(f"The lowset five scores are: {lowest_five}")

# So we can also use negative values as well to slice the list from the end
#	or "right" most values. DON'T MIX POSTIVE AND NEGATIVE INDICES FOR START
#	AND END. It will confuse Python.

# Slicing also supports a "step" or skip value as well. For example, let's
#	assume we wanted every other exam score (not sure why, but let's do it).
every_other = exam_scores[0:len(exam_scores):2]
print(f"Every other exam score: {every_other}")

# We start at the beginning of the list (0), and define we will slice to the
#	length of the array (11, remembering that the end is not inclusive). We
#	grab our first item at index 0, and then finally with a step of 2, the
#	slice skips to index 2, then 4, 6, etc. So, now our complete slicing
#	capabilities are denoted as [start index: end index: step value]. Note
#	that the step value is always optional, and the default step is 1.

# Last but not least, slicing allows us to omit some of the index values for
#	convenience. Let's grab out top five scores again, but in a slightly
#	different way.

top_five_again = exam_scores[:5]
print(f"The top five scores again are: {top_five_again}")

# Notice how we omitted the starting index. The slice assumes that if we omit
#	that value that we want index 0. We can do the same for the end index

low_five_again = exam_scores[-5:]
print(f"The lowest five scores again are: {low_five_again}")

# Since we omitted the ending index, the slice assumes we want to to go
#	to the end of the list. Actually...all the values are optional!

copy_exam_scores = exam_scores[:]
print(f"This is a copy of exam_scores: {copy_exam_scores}")

# If we omit all the values, we actaully can make the slice copy our list
#	for us. Let's prove that it's an independent copy by sorting the copy
#	in ascending order (low to high).

copy_exam_scores.sort()
print(f"The original exam list: {exam_scores}")
print(f"The copy exam list: {copy_exam_scores}")

# One last thing to note is about slicing is that the order of the start and
#	end does matter. For example, if we slice our copy of exam list backwards
#	what might happen?

print(f"Copy exam list from: {copy_exam_scores[-1:-6:-1]}")

# It makes a new list with the last 5 values in reverse order.

# Everything we have done so far on lists with slicing also works on strings!
string_to_slice = "hello world"
print(f"Sliced string: {string_to_slice[6:]}")

print("\nRange")

# The range function in Python helps you to create a collection of numbers in
#	in a range of values. Range, like slicing, use a start value, end value, and
#	a step value. Range gets used often with for loops to control as a way to
#	create a loop that runs a fixed number of times.

for i in range(10):
    print(i)

print() # Output a new line

# With only one argument (the 10 in our case above), range assumes we want the
#	values starting with 0 and ending with 9. Like slicing, the end value is not
#	inclusive.

for i in range(1, 5):
    print(i)

print()

# Two values provides a start value (inclusive) and the end (exclusive).

for i in range(1, 10, 2):
    print(i)

# Three values indicates your starting value, ending value, and the step or
#	increment value. So here, we start at one so we get all odd numbers.

# It is worth noting that the result of the range function isn't quite a
#	normal list. See what happend when we print it.
print(f"Range 0-10: {range(11)}")

# So we can't exactly do all the fun stuff that we did with lists using range
#	like this. However, we can "cast" the result to a list. When you cast data
#	you are telling Python that you want to convert something from one type of
#	data to another. Python provides common casting to some types with the functions:
#		* int()
#		* float()
#		* str()
#		* list()
#		* etc. (we may look at more later)

my_range_list = list(range(11))
print(f"Range 0-10: {my_range_list}")

# The code above converts the range data into a list type data.

print("\nList Comprehensions")

# List comprehensions can be a bit challenging to grasp. Python provides this
#	as a way to generate lists that already contains some values in a compact
#	and convenient way. Let's make a list of 10 zeros.

ten_zeros = [0 for _ in range(10)]
print(f"List of zeros: {ten_zeros}")

# A few things are going on in the code above, so let's pick it apart. First off
#	we have our brackets [] to signal that we want a list. Inside the brakets, we
#	have what looks like a for loop...but there is no body or indented code in it.
#	What a list comprehension does is actally evaluated the statement before the for
#	loop each time the loop would run. In our case, the loop would run 10 times and
#	the statement before the for loop is simply the literal value 0. So our list
#	becomes populated with ten zeros. The underscore "_" used for the variable part
#	of the for loop is a way of indicating in python that you don't intend to use the
#	value. Since I want all zeros I don't want any of the values the range function
#	will produce. But what if I did?

zero_to_nine = [num for num in range(10)]
print(f"List from 0-9: {zero_to_nine}")

# This might illustrate better what is happening. The for loop is running for
#	each value in range. Num is assigned one of the values and then num is used
#	in the statement before the for loop. This repeats for each value in range
#	and because we have placed this in a list [] we get each value as a list item.

# One more time to illustrate this...it is kind of a weird thing to look at,
#	but is very powerful once you grasp it.

one_to_ten = [num + 1 for num in range(10)]
print(f"List from 1-10: {one_to_ten}")

# You can now see how num gets its value AFTER each loop or iteration of the
#	for loop, and the value is then incremented by one as the statement num + 1
#	is computed.

# List comprehensions are not super easy to think about. I encourage you to play
#	with them a bit until you feel more comfortable with the syntax and results
#	they produce.

print("\nTuples")

# Tuples are a lot like lists. They can hold multiple types of data,
#   can have their values accessed by position index, but there are a few key differences.

# Declaring a Tuple requires the use of parenthesis and commas to separate values.
my_tuple = (1, "little", "tuple")
print(f"Data in my_tuple: {my_tuple}")
print(f"The second element in the tuple is: {my_tuple[1]}")

# It looks a bit like a function, but there is no name associated with the values
#   contained within the parenthesis. An oddity with tuples is declaring a tuple
#   with one value.
only_one_value = (1,)
print(f"The tuple has one value: {only_one_value}")

# That looks a  bit weird to have the trailing comma, but it's the only way
#   Python knows that you want that to be a tuple with one value an not just
#   the value one in parenthesis (1). Just a little quirk to keep in mind.

# Unlike lists, tuples are immutable (cannot be changed). So the following isn't allowed:
#   my_tuple[0] = 10 # CANNOT CHANGE THE TUPLE
# There is also no way to add or remove values from the tuple like you can with lists.

# You can loop over tuple values
for data in my_tuple:
    print(data)

# You can also sort a tuple with the sorted() function
my_number_tuple = (45, 6, 32, 8, 11, 6)
print(sorted(my_number_tuple))
