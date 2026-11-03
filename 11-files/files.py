from pathlib import Path

# While a program is running, our data may be located in RAM or computer
#	memory. While this storage location is relatively fast, it is volatile.
#	If we lose power or shut off the computer the contents of RAM can be
#	considered lost. Files are an integral method of storing data long-term on your
#	computer using other storage methods. Devices like Hard Drives (mechanical
#	or solid state), USB Drives, Optical media (like DVD/Blu-ray), etc. can hold
#	our data persistently. Being able to access data contained in files is an important
#	part of writing computer programs.

# The location of a file on your computer is called a "path". Using this location we
#	can open, read, and write contents to a file. There are two types of file paths:
#		1.) Relative paths
#		2.) Absolute paths

# A relative path is based on the location of the program you are running. For example,
#	in the directory that contains this code file, we have a file called 'text.txt'.
#	Using a path that is relative to this program to access text.txt would look like this:
text_file = Path('text.txt')

# Notice how this path is simply the name of the file. That is because when we run files.py,
#	the program assumes since we didn't provide any other directory information (folders) that
#	the data is located in the same folder as the text. Let's see if we can display it.
contents = text_file.read_text()
print(contents)

# Good, it works! We should see that text content from the file. If this file were not in the same location
#	as the python script, we would need to provide more info. Let's try to find a text file in the subfolder
#	named data
text_file = Path('data/file-in-a-folder.txt')

# Notice how we included the name of the folder "data" then a forward slash. That indicates that there is a
#	folder named data, and we need to go into that folder to find our file 'file-in-a-folder.txt'. Let's try
#	to display the content again.
contents = text_file.read_text()
print(contents)

# Nice! These paths are relative. They are based on where (what folder) the program is being run. You'll notice
#	that no matter where you have stored this example on your computer, this program will work correctly (as long
#	as the folder structure for the example is maintained.

# An absolute path, is a different story. Absolute paths are unique, no two files can have the same absolute path.
#	The reason we call them absolute paths is because the are the complete path to the file, so no matter where you
#	run your program the absolute path can be used to find the file. Let's use a bit of code that's not in the book
#	to find our 'text.txt' file's absolute path.
text_file = Path('text.txt')
print(text_file.resolve())

# If you compare the result of the code above with a friend, you'll notice the paths are different. You'll also notice
#	that on MacOS (or Linux) the path starts with / and on Windows it might start with a letter like C:\. This starting
#	character devices the "root" of the file system where you document is located. From the root, every directory leading
#	to your file will be displayed following by a slash until we reach 'text.txt'. Absolute paths are great, because they
#	are guaranteed to work...but only on a computer with the same file system. For example, my result from the code above
#	says my path is: /Users/dguarnera/Repos/cs102-examples-f23/11-files/text.txt The problem is that path isn't on your
#	computer, it's special to me, and anyone who has there computer setup exactly like me (username and all). If you are
#	using windows, you might even have different slashes than I do (that's a difference between Mac and Windows). Path will
#	handle them correctly regardless as long as you use forward slashes in your code.

# Hopefully, this helps explain relative and absolute file paths a bit better! Let's look at a new way of using the Path
#	class!

# The book shows you how to open and write to files using Path, but what if the file is big....like really big. Some files
#	might be too large to efficiently read all of the content into memory. To work around this, we can read a file
#	line by line. In our data directly, we have a log file from a webserver that has 10,000 lines of data. We could
#	likely fit that all in memory, but that's a bit inefficient. Let's try a different approach.
server_log = Path('data/apache_logs.txt')
with server_log.open() as server_data:
    print(server_data.readline())
    
# This code has read just the first line of the file, but let's unpack what is happening here. When you open a file in
#	Python, you need to make sure you close it. If you don't close a file (especially with writing) you might not
#	get the data in your file or other unexpected behavior. Our with keyword followed by calling open() on our Path object
#	helps Python to automatically close the file for us after all the code indented within the "with" structure is done.
#	This way, we don't have to remember to run close(). The "as" keyword helps us give a name to the content of the file
#	when we say open. The readline() method will copy one line of text (ending with a newline) and give it to Python.
#	Subsequent calls to readline() will give us the next line in the file. What if we wanted to do something for every line
#	in the file? We'll first...let's try a smaller file...10,000 lines takes a little while to print.

text_file = Path('data/rr.txt')
with text_file.open() as data:
    for line in data:
        print(line.rstrip()) # Strip off the newline from the right end of the text line
        
# From the output below, you can see that we read each line from the file ;)

# The Path class does have some limitations in that it doesn't support certain file modes like being able to append
#	content to an existing file (Path will just overwrite it). In the other example file, we'll look at a slightly
#	different option.
