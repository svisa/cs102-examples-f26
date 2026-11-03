# Dictionaries are very powerful datastructures that allow you to
#	store values associated with keys. You use keys to "look-up" the
#	values much like a phone book/address app, or dictionary, which is
#	where the name comes from. This structure may be called a different
#	name in other languages, but they are all based on the idea of a
#	hash table.
#
# Dictionaries are useful as they can help you organize data in a more
#	precise way to help you represent more complex concepts in a program.
#	Additionally, finding data in a dictionary is very fast and instead of
#	needing to remember what position data resides in, as we do  with lists,
#	we can use the keys.

# Create a user account program
print("Creating Dictionaries")
# Empty dictionary
my_empty_dictionary = {}

# Dictionary with Items
user = { 'name': 'Sarah Serene',
         'age': 30,
         'title': 'CEO' }
# Each item in a dictionary is represented by a key:value pair
#	Keys must be unique and can only be immutable types:
#		* strings
#		* numbers
#		* tuples

print(user)

print("\nAccessing Dictionary Values")
# Access item in dictionary
print(f"{user['name']} is the {user['title']}.")

# If you try to access a key that does not exist using the brackets
#	you will get an error!
#
# print(user['social_security_number']) # Will not work!

# The get() method can also use a key to get a value from a dictionary
print(f"{user.get('name')} is {user.get('age')} years old.")

# But it doen't cause an error if the key does not exist
print(f"{user.get('name')}'s social security number is: {user.get('ssn')}")

# Notice the value was None. In Python, None is a constant that indicates
#	there is no value/data associated with what you have tried to access

# You can also allow get() to supply a default value if you choose.
#	This does NOT add anything to the dictionary.
print(f"The social security number is: {user.get('ssn', 'Unavailable')}")

print("\nAdding a key/value pair to a dictionary")
# Add item to dictionary
user['salary'] = 100000

print(user)

# Looping over dictionary

# When looping over a dictionary, the default behavior is to loop
#	over the keys. The order of the keys is usually the order in
#	which they were added, but it is good practice not to assume
#	this as other languages may store keys unordered.
print("\nFor Loop on a Dictionary")
for key in user:
    print(key)

# This behavior is similar to the dictionary keys() method. Which
#	gives you a list of all the keys in a dictionary
print("\nFor Loop using the keys() Dictionary Method")
for key in user.keys():
    print(f"{key}: {user[key]}")

# If you would like to loop over a dictionary much like a list and
#	get both the keys and values, you can use the items() method.
print("\nFor Loop using the items() Dictionary Method")
for key, value in user.items():
    print(f"{key}: {value}")

print("\nFor Loop using the values() Dictionary Method")
for value in user.values():
    print(f"?: {value}")

print("\nLists of dictionaries")
# Looking at our user example what if we wanted to keep track of
#	multiple people?

# We can use a list to hold multiple dictionaries to represent our people
employees = []

# This will add Sarah
employees.append(user)

# We can create another dictionary for Peter
user2 = { 'name': 'Peter Parker', 'age': 21, 'title': 'Photographer', 'salary': 25000 }
employees.append(user2)

# We can also add the dictionary in-place
employees.append({ 'name': 'Ari Appleseed', 'age': 16, 'title': 'Intern'})
#	Notice the dictionaries don't need to have the same keys. Also,
#	interns should be paid...just saying...

# A nested loop here helps us:
#	Access each dictionary in the list with the outer loop
for employee in employees:
    # Acess each key:value pair in the dictionary with the inner loop
    for key, value in employee.items():
        print(f"{key}: {value}")

# Dictionaries with Lists
print("\nDictionaries with Lists")
# Sometimes the values that our keys reference may need to be
#	represented by more than one value. Since keys are unique,
#	we can simply store more than one value using a list.

# Perhaps Sarah and Peter have multiple email addresses
employees[0]['emails'] = ['sserene@gmail.com', 'sarahserene@company.com']
employees[1]['emails'] = ['ppaker@dailybugle.com', 'theavenger@yahoo.com', 'spiderman@shield.com']

for employee in employees:
    for key, value in employee.items():
        if key == 'name':
            print(f"{key}: {value}")
        if key == 'emails':
            for email in value:
                print(f"email address: {email}")

# Dictionaries with Dictionaries
print("\nDictionaries with Dictionaries")

# Much like with lists, dictionary values can be other dictionaries.
# Let's assume everyone has a login that we need to keep track of as
#	well.

# First Sarah
employees[0]['login'] = {'username': 'sserene', 'password': 'serenitynow'}
# Next Peter
employees[1]['login'] = {'username': 'ppaker', 'password': 'friendlyneighborhood'}
# Finally Ari
employees[2]['login'] = {'username': 'aappleseed', 'password': 'anappleaday'}

for employee in employees:
    for key, value in employee.items():
        if key == 'name':
            print(f"name: {value}")
        if key == 'login':
            # The sorting here is so no matter what order the
            #	two keys are in, I'll always print username
            #	then password ('username' comes after 'password'
            #	lexographically).
            for login_data in sorted(value.keys(), reverse=True):
                print(f"{login_data}: {value[login_data]}")
                
# This can get more intense, and most combinations of organization
#	you can think of can be used. Lists, Tuple, Dictionaries, and
#	more can all be used together.