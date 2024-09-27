# A string delimited by double quotes.
print("Hello, world!")

# The type of a string
print(type("Hello, world!"))

# A string deliminted by double quotes that uses a single quote in its message.
print("That is Jane's bag.")

# A string delimited by single quotes that uses a double quote in its message.
print('They said it was "inappropriate", but I will take that as a suggestion.')

# A string using an escape sequence \"" to insert a double quote in its message.
print("They said \"wait a second, that's not yours!\" when it had my name on it.")

# A strig using the escape sequences \n and \t for newlines and tabs, respectively.
print("Dear Professor,\n\n\tI'm excited to \"ace\" this class.\n\nSincerely,\nStudent")

print("""Dear Professor,
      
    I'm excited to "ace" this class.
      
Sincerely,
Student""")

# Calculate the area of a rectangle of known dimensions.
width = 8
height = 15
area = width * height

# Create a message using a format string.
print(f"A rectangle of width {width} and height {height} has area {area}.")

# A shortcut when you want the variable name in the message
print(f"A rectangle of {width=} and {height=} has {area=}.")

# String methods
message = "   Hello, world    "
print(message)
print(message.lower())
print(message.upper())
print(message.title())
print(message.capitalize())

# Remove spaces at the end of the string
print(message.rstrip())
# Remove space at the beginning of the string
print(message.lstrip())
# Remove spaces on either side of the string (but not within the string)
print(message.strip())

HOME_PAGE = "https://www.linkedin.com/in/sergio-garcia-tapia/"
print(HOME_PAGE.removeprefix("https://"))

# The string methods do not change the string because strings are "immutable".
print(f"Values at the end: {message=}, and {HOME_PAGE=}")

# The len() built-in function yields the number of characters in a string.
print(f"The string {message=} has {len(message)} characters")
print(f"The string {HOME_PAGE=} has {len(HOME_PAGE)} characters")
