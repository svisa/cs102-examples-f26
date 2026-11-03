import os

# The open function provided by Python works similarly to the Path class.
# You'll probably see this form of file operations most often in examples
#	online or other textbooks.

# We can open a file
my_file = open('text.txt', 'r')
print(my_file.readline())
my_file.close()

# You'll notice some difference above. We not only take the file path, but also
#	a mode. Some common modes are:
#		* 'r' is read only
#		* 'w' is write only
#		* 'a' is append only
#	Write mode works like the Path class. We overwrite the file with new data if it
#	already exists. Append however, will start writing after existing content if
#	a file exists already. We also need to make sure that we close the file when we are
#	done using it.

# With open() we can also write multiple times to a file that is open.
my_new_file_path = 'new_data.txt'
my_file = open(my_new_file_path, 'w')
my_file.write("One\n")
my_file.write("Two\n")
my_file.write("Three\n")
my_file.close() # Must remember to close or we won't see the data in the file

# Let's see the results
with open(my_new_file_path, 'r') as my_data:
    for line in my_data:
        print(line.rstrip())
        

# Let's add more data to the file
with open(my_new_file_path, 'a') as my_data:
    my_data.write("Four\n")
    my_data.write("Five\n")

# Notice that the "with" automatically closes the file, so we don't have to worry about doing
#	it manually.

with open(my_new_file_path, 'r') as my_data:
    for line in my_data:
        print(line.rstrip())

# There is a caveat to open vs Path, and that open needs a little help with handling both Windows and macOS paths.
#	We can look to the os module and use path.join to help with this.
path = os.path.join('data', 'rr.txt')
# This will give us a relative path to the data folder and the rr.txt file correctly (regardless of Windows or macOS).

with open(path) as my_data: # If you don't provide a mode, Python assumes read mode ('r')
    for line in my_data:
        print(line.strip()) # strip() removes both leading and trailing whitespace
