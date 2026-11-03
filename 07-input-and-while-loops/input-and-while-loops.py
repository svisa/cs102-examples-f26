print("User Input Examples")

# You can get data from the user with the input() function.
#	A user can type in any text they'd like and press ENTER
#	to submit the text to your program.

data = input() # Type something in and press enter
print(f"You randomly typed: {data}")

# Optionally, the input() function can take an argument which
#	is a string prompt requesting what information the user
#	needs to enter for the program. While this is optional,
#	it's highly recommended so people using your program understand
#	what to do.

age = input("Enter your age in years: ")
print(f"You are {age} years old")

# It is important to note that the data you receive from the
#	input() function is always a string representing the
#	content the user typed in before the enter key was pressed.

# If you needed a person to enter some data that needs to
#	NOT be treated as a string (eg. a number), you can convert
#	that data from a string to a number using int() or float()
if int(age) < 18:
    print("You can't vote yet!")
    
print("\nWhile Loops")

# While loops are another type of loop. The difference between a
#	for and a while loop is that for loops have a fixed boundary
#	with respect to the number of times they run (based on the
#	container (string, list, dictionary, etc) or a range of values
#	using the range() function.
for character in 'hello world':
    print(character)
    
for number in range(5):
    print(number)
    
# While loops on the other hand run as long as the condition they check
#	is true. This could mean the run forever (an infinite loop). Using
#	while loop, you can recreate any for loop.
count = 0
while count <= 4:
    print(count)
    count += 1
    
# What if we accidentally did.
# count = 0
# while count <= 4:
#     print(count)

# Uh oh...that's always true...This would be an infinite loop and
#	the program will continue to execute the loop forever. You can
#	press the STOP sign button in Thonny to terminate the program.

# Suppose we wanted to let a user type in the names of all their friends
#	We don't know how many friends that person has...

friends = []

friend = ''
while friend.lower() != 'quit':
    friend = input("Enter a friend's name or quit to stop: ")
    if friend and friend.lower() != 'quit':
        friends.append(friend)

print(f"My friends are:")
for friend in friends:
    print(friend)
    
# There are plenty of other ways to write this loop so it behaves
#	the same. Can you write the same loop using a flag instead
#	(see the book section "using a flag" in Chapter 7)?

# Sometimes there are situations where we might want to leave a
#	loop early or skip an iteration (one execution of the loop).
#	Python provides the keywords break and continue to do those
#	actions respectively.

items = ['bread', 'milk', 'eggs']

for item in items:
    print(f"item: {item}")
    if item == 'milk':
        break # When we execute this statement, the loop ends

# Notice how we did not finish looping over the list of items
#	to print 'eggs'. The break caused us to quit or "break" out
#	of the loop.

for item in items:
    print(f"item: {item}")
    for char in item:
        print(f"character: {char}")
        if char == 'i':
            break

# Notice what happened here in the nested loops? The break only quit
#	the inner loop when we found the letter "i". So it printed part of
#	"milk", quit the inner loop, and then resumed the outer loop. Breaks
#	only jump out of the loop they belong to.

# Breaks are very common with for loops since we have less control over
#	them once they start (they simply loop over the range of data provided
#	and then stop), but we can use them in while loops too.

my_string = "frobarf"
start_index = 0
end_index = len(my_string) - 1

while start_index <= end_index:
    if my_string[start_index] != my_string[end_index]:
        print("NO MATCH")
        break
    
    print(f"{my_string[start_index]} == {my_string[end_index]}")
    start_index += 1
    end_index -= 1

# Last, lets look at the "continue" statment. As with break, it can
#	be used in a while or for loop. But it's job is to skip an iteration
#	of the loop and move to the next one. For example, lets say we
#	wanted to only print all even numbers in a given range.

for number in range(1, 11): #range of numbers from 1 - 10
    if number % 2 != 0:
        continue
    print(number)
    
# Weird huh? The loop printed every even number...but why only those?
#	That's where the condition with the "continue" comes in. The if
#	statement checks if a number % 2 is not equal to 0. That means the
#	number will have a remainder when divided by two, and thus cannot be
#	an even number. When this condition is True, the continue statement
#	is executed. This basically says to the loop "hey, skip everything
#	after this line and move on to the next iteration (in our case, the
#	next value in range).

# Same thing can be done in a while loop. Let's make a loop that reads
#	user input but if they forget to type anything (just hit enter),
#	the loop with continue and they can try again.

input_data = ''

while input_data.lower() != 'quit':
    input_data = input("Enter some text or quit to stop: ")
    
    if not input_data:
        continue

    print(input_data)
    
# REMEMBER that continue works like break in that it only affects the
#	loop that it belongs to.

strings = ["hello", "students", "how", "are", "you"]
vowels = 'aeiouy'
for string in strings:
    for letter in string:
        if letter in vowels:
            continue
        print(letter, end='')
    print() # This will just print a new line

# The continue here only skips the vowels, and not the entire words
#	as getting those is the job of the outer loop. NOTE: the word
#	"you" doesn't print at all because it is comprised only of vowels.