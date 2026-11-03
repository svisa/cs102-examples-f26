print("For Loops")

# When we write code, sometimes we want a set of intructions to happen
#	multiple times. Rather type the same code repeatedly we tell the
#	computer to just repeat it some number of times. This is called
#	looping. Each time we run a loop in our code, we call that an
#	"iteration" of the loop. We will start with for loops.

# In Python, for loops can be thought of as "for each loops".
#	Let's assume we have a list of numbers

number_example = [1, 2, 3, 4, 5]

# If we wanted to perform a task that processes each number
#	individually, we could use a for loop. The format of a
#	for loop is:

for item in number_example:
    print(item)
    
# This could be read in english as "for each item in number_example,
#	do the following steps". In our case, we print out each number
#	on a separate line.

# It is important to note that "item" is just a variable that you can
#	use within the loop to access the current value in the list. That
#	name is not special in any way. For example:

for unicorn in number_example:
    print(unicorn)
    
# While the variable name is non-sensical, this illustates that the name
#	is whatever you'd like it to be.

# Statements that occur as part of the for loop are indented beneath it.

for number in number_example:
    print(number) # This first instruction of the for loop
    print(f"{len(number_example) - number} more to go!") # This is the second
    
    print("Loop number {number}!") # This is the third, (regardless of the new line above)

print("All Done!") # This does not belong in the for loop

# BE CAREFUL WITH INDENTATION!

# You can also loop over strings. Remember, a collection of characters...
for character in "HelloWorld!":
    print(character)

print("\n Nested Lists")

# Sometimes, we would like to be able to store data in more complex ways.
#	Let's pretend we are making the puzzle game minesweeper and we need to
#	store what the puzzle looks like. Perhaps something like this: 

#		b b 2
#		3 b 2
#		1 1 1

#	'b's are bombs

# This grid type of data layout can be handled with nested lists
#	(or multi-dimensional lists). This means we have a list, that
#	holds lists as it's elements/items. Let's see how this works.

minesweeper = [ ['b', 'b', 2], # Nested List 1
                [3, 'b', 2],   # Nested List 2
                [1, 1, 1] ]    # Nested List 3

# Lets loop over minesweeper to see what we have.

for cell in minesweeper:
    print(cell)
    
# Ah! We have our three rows of values. But how might we access each item...
#	Essentially our "outer" list (the one that holds the others) contains
#	our rows while each "inner" list is a colum. This is kind of like a
#	spreadsheet in Excel or Numbers.

row_position = 0
for row in minesweeper:
    column_position = 0
    for cell in row:
        print(f"{cell} is at ({row_position}, {column_position})")
        column_position += 1
    row_position += 1 # This takes the current value of row_postion and increases it by one

# The code above features nested looping. This means that for each occurrence of the
#	"outer" loop (row in minesweeper), the "inner" loop occurs. Notice from this example
#	the indentation. Make sure you understand which loop each line of code belongs to.
#	In this nested loop, the inner loop runs 9 times. Once for each row (3) and once for each
#	item in each row (3). We can calculate this by multiplying the number of outer and inner loop
#	iterations (3 * 3 = 9).

# From our output, we can see that each item in the multi-dimensional list has
#	two indices. One for the row, and one for the column. Let's access the first
#	row, second item.
print(minesweeper[0][1])

# This technique of multidimensional lists can be used for:
#	* Matrices
#	* Game levels or board states
#	* Images
#	* Graphs/Trees (a type of advanced data structure)
#	* etc.

