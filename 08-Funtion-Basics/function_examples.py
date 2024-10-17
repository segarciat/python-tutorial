# Define a function
def reciprocal(n):
    """Computes the reciprocal of the input."""
    return 1 / n

# This will hold the value of our sum
result = 0

minimum = 1
maximum = 10

for k in range(minimum, maximum + 1):
    result = result + reciprocal(k)
    print(f"{k}th value is {result}")

print(result)

minimum = 0
maximum = 5

geometric_sum = 0
for k in range(minimum, maximum + 1):
    geometric_sum += pow(2, k) # 2 ** k
    print(f"{k}th value is {geometric_sum}")