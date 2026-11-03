# Conditional Logic and If Statements

# We often need to have our computers make decisions based
#	on the results of a calculation, input, etc. Without this
#	functionality, most of our programs would be pretty limited.

# We have a few standard operators that help us perform conditional
#	tests. The results of these tests are boolean values (True or False)

print("EQUALITY AND COMPARISON OPERATORS")
x = 10
y = 3

print(f"{x} is equal to 10: {x == 10}")
print(f"{x} is not equal to 10: {x != 10}")
print(f"{x} is less than {y}: {x < y}")
print(f"{y} is less than or equal to {x}: {y <= x}")
print(f"{y} is greater than {x}: {y > x}")
print(f"{x} is greater than or equal to {y}: {x >= y}")

string1 = "apple"
string2 = "beta"

print(f"{string1} == apple: {string1 == 'apple'}")
print(f"{string1} != apple: {string1 != 'apple'}")
print(f"{string1} < {string2}: {string1 < string2}")
print(f"{string1} <= {string2}: {string1 <= string2}")
print(f"{string1} > {string2}: {string1 > string2}")
print(f"{string1} >= {string2}: {string1 >= string2}")

# You can also use the same comparison operators on strings. While
#	== and != are straightforward for strings, the comparisons are
#	a little strange at first. When you use <, >, <=, or >= on a string
#	you are comparing the text lexigraphically. The easy way to think
#	of this is if given word would come before another in the dictionary,
#	it is smaller than the other word. If a word would come after
#	another word in the dictionary it is larger than the other word.
# ASK YOURSELF A QUESTION...HOW DOES THE COMPUTER KNOW A IS BEFORE B?!

# These comparisons can be useful on there own, but their true power
#	comes from being used within conditional structures like if statements

print("\nIF STATEMENTS")
exam_score = 85

if exam_score > 50:
    print("You passed the exam!")
else:
    print("You did not pass the exam!")

# If statements can execute any code that is nested beneath them if
#	the result of their conditional test(s) will be True. If you change
#	exam score to 50 or lower the conditional test will be False and the
#	else clause of the if statement will execute. In english we could word
#	an if statement as:
#
#	if this is true, do this, else do that.

if exam_score > 89:
    print("A")
elif exam_score > 79:
    print("B")
elif exam_score > 69:
    print("C")
elif exam_score > 50:
    print("D")
else:
    print("F")

# Sometimes we need to perform multiple checks to determine a single
#	correct outcome. In the case above, each time our condition is False
#	we check a new condition as an else clause using elif (else if).
#	IT IS VERY IMPORTANT TO NOTE A FEW THINGS:
#		* IF YOU HAVE AN ELSE, ONE OF YOUR CONDITIONS WILL ALWAYS OCCUR
#		* IF YOU HAVE AN ELIF, AT MOST, ONE OF YOUR CONDITIONS WILL EXECUTE
#
#	From our example above, we can only receive one possible letter grade.
#	If any of those checks are True, we have our result and we are done.
#	If all the check happen to be False, we logically only have one
#	option left, the "F" case.

age = 21

if age >= 18:
    print("You can vote")
if age >= 21:
    print("You can enjoy an adult beverage")
if age >= 67:
    print("Congratulations you can retire!")
if age > 100:
    print("How are you doing this?!")
    
# Sometimes our decisions are not mutually exclusive. Consider the previous
#	example, where we can give people messages based on their age. These options
#	are related, but not exclusive. A person who is 21 can still vote and enjoy
#	any beverage of their liking. A person who is 80 can do all of those things
#	and retire. In these cases, a series of independent if statements can be useful
#	and prevent unnecssarily complicated logic.
#
# Also take note from this example that the ELSE CLAUSE IS ALWAYS OPTIONAL. If any
#	of our if statements above regarding our age are False, we simply do nothing.

print("\nLIST CONDITIONS AND LOGICAL OPERATORS")

valid_hotdog_toppings = ['hotsauce', 'sawdust', 'ketchup', 'mayo', 'mustard', 'chili', 'honey', 'relish']
likes_spicy_food = False

for topping in valid_hotdog_toppings:
    if topping == 'ketchup' or topping == 'mustard' or topping == 'relish':
        print(f"{topping}, a classic choice.")
    elif (topping == 'chili' or topping == 'hotsauce') and likes_spicy_food:
        print(f"Mmmm {topping}, enjoy the heat!")
    else:
        print(f"{topping} is an interesting choice")
        
# Sometimes we can combine our conditional tests in one statement.
#	With the keywords "and" along with "or" we can make more complex
#	decisions based on multiple decisions.

# When dealing with and/or in conditional tests it is important to
#	remember a few things:
#		* The "and" conditional test has a higher precidence than "or"
#		* A conditional test with "and" is True if and only if both statments are True
#		* A conditional test with "or" is False if and only if both statements are False

# In our example above, notice how we use parenthesis to change the order
#	of precedence for the and and or statement. We want to make sure that
#	if a hotdog topping is chili or hotsauce, we then check to make sure
#	our person like spicy food.

# Consider the following: What would the output be without the parenthesis? Why?

completed_chores = ['dishes', 'walk dog', 'homework']

if 'homework' in completed_chores:
    print("Nice! Play some video games!") 
if 'mow lawn' not in completed_chores:
    print("Don't forgot to mow the lawn!")
    
# When working with lists, we often want to know if something is, or is
#	not in a list. Python makes this easy with the "in" keyword. This will
#	will perform a check of all the items in the list to see if a value
#	is present in the list.
#
# You may also have noticed that the example uses the keyword "not". When you
#	using in, you can also check to see if something does not exist in the list.

#	"not" can also be used to negate a condition
print(f"Negating the results of 7 == 7 results in {not 7 == 7}")
# Negating the result of a condition results in "flipping the result"
#	In our case above 7 == 7 is true, but "not" makes our result the
#	opposite and we get False. If we did: not 7 != 7, we would end up
#	getting True instead of False. Note that the "not" keyword has higher
#	precidence then the "and" and "or" keywords.

confused = True
print(f"I hope you are {not confused} :)")
if confused:
    print(f"Don't worry, you can always ask questions!")