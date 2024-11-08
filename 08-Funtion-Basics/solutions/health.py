def calories(fat, carbs, protein) -> float:
    """Computes the amount of calories corresponding to
    the given macronutrients.

    Args:
        fat float: Amount of fat in grams.
        carbs float: Amount of carbohydrates in grams.
        protein float: Amount of protein in grams.

    Returns:
        float: The amount of calories from the given macros.
    """

    fat_calories = 9 * fat
    carb_calories = 4 * carbs
    protein_calories = 4 * protein

    return fat_calories + carb_calories + protein_calories


# Using positional arguments
print(calories(9, 30, 10))

# Using keyword arguments
print(calories(carbs=30, fat=9, protein=10))