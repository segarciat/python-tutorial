m = 7
divisor = 3
description = "is an integer"

# Statements in body is do not execute because 7 is not divisible by 3
if m % divisor == 0:
    description += f", and it is divisible by {divisor}"
    description += f", fits {m // divisor} times into {divisor}"

# Runs regardless of the outcome if the if statement above
print(f"{m=} {description}")

n = 114
divisor = 3
description = "is an integer"

# Statements in body execute because 114 is divisible by 3
if n % divisor == 0:
    description += f", and it is divisible by {divisor}"
    description += f", fits {n // divisor} times into {divisor}"

# Runs regardless of the outcome if the if statement above
print(f"{n=} {description}")

# Above we set m to 7, so if it still has that value, then only the else branch executes
if m % 2 == 0:
    print(f"{m} is even")
else:
    print(f"{m} is odd")