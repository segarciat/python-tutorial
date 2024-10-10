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
message = "hELLo wOrlD"
print(f"original         : {message}")
print(f"lower()          : {message.lower()}")
print(f"upper()          : {message.upper()}")
print(f"title()          : {message.title()}")
print(f"capitalize()     : {message.capitalize()}")

# Strings are immutable, so message is unchanged by method calls.
print(f"after methods    : {message}")

# We cannot modify the string, so we must create a new one and reassign.
message = message.capitalize()
print(f"after reassigning: {message}")

print()

message = "\t      I like pie!     \n "
print(f"original: *{message}*")
# Remove leading spaces
print(f"lstrip(): *{message.lstrip()}*")
# Remove trailing spaces
print(f"rstrip(): *{message.rstrip()}*")
# Remove both leading and trailing spaces 
print(f"strip() : *{message.strip()}*")
print(f"after   : *{message}*")

# How many characters in the string, including spaces and escape sequences
print(f"The string {message=} has {len(message)} characters")
# Removing spaces
print(f"After removing spaces, it has {len(message.strip())} characters")


