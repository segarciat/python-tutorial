# The built-in type() function determines the type of its argument expression.
# Knowing the data type helps Python know what operations are valid involving that expression.

# These expressions are of class (data type) 'int', short for integer
print(type(0))
print(type(-52))
print(type(1 + 17))
print(type(102 - 255))
print(type(38 * (-48)))

# The result is of class 'float' (data type), short for floating point number
# The float data type is used to (approximately) represent real numbers with fractional parts.
# Unfortunately computers cannot precisely represent fractions.
print(type(5.2 / 3.1))

# Data type (class) is 'complex'.
# The j is the square root of -1. In algebra, you'd likely use the letter i.
print(type(4 + 8j))

# Data type (class) is 'str', short for string. Used for textual data.
print(type("hello"))

# Data type (class) is 'bool', short for boolean. Used for True/False values.
print(type(False))

# Data type (class) is 'list', used for collections of values.
print(type([5, 7, 0, -2, 23]))