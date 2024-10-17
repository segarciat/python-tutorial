import random

def flip_coin():
    """Simulates flipping a coin. Returns "Head" or "Tails" with equal probability.

    Returns:
        str: "Heads" or "Tails"
    """
    if random.random() < 0.5:
        return "Heads"
    else:
        return "Tails"

print(flip_coin())
print(flip_coin())
print(flip_coin())
