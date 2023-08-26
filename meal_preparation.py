import numpy as np
import random
import itertools

def is_magic(square):
    """Check if the provided square is a magic square."""
    s = np.sum(square[0])
    return all(np.sum(square[i]) == s for i in range(square.shape[0])) and \
           all(np.sum(square[:, i]) == s for i in range(square.shape[1])) and \
           np.sum(square.diagonal()) == s and \
           np.sum(np.fliplr(square).diagonal()) == s

def all_permutations(n):
    """Generate all permutations of numbers from 1 to n^2."""
    return list(itertools.permutations(range(1, n*n+1)))

def generate_magic_square(n):
    """Generate a random n x n magic square for odd values of n."""
    if n % 2 == 0:
        raise ValueError("Function currently supports only odd-sized grids.")
    
    # Pre-generate all permutations
    permutations = all_permutations(n)
    
    # Randomly shuffle the list of permutations
    random.shuffle(permutations)
    
    for perm in permutations:
        square = np.array(perm).reshape(n, n)
        if is_magic(square):
            return square
    return None  # Return None if no magic square is found

# Generate the 5x5 magic square using the function from the previous article
magic_square = generate_magic_square(5)

# Define the sample meals for each category based on caloric distribution
sample_meals = {
    "Breakfast": [
        "Oatmeal with berries and almonds",
        "Whole grain toast with avocado and eggs",
        "Smoothie with spinach, banana, and protein powder",
        "Greek yogurt with honey and granola",
        "Pancakes with maple syrup and fruit"
    ],
    "Morning Snack": [
        "Apple with peanut butter",
        "Handful of mixed nuts",
        "Granola bar",
        "Fruit salad",
        "Cottage cheese with pineapple"
    ],
    "Lunch": [
        "Grilled chicken salad with vinaigrette",
        "Quinoa and vegetable stir-fry",
        "Turkey and cheese sandwich with lettuce and tomato",
        "Pasta with tomato sauce and parmesan",
        "Lentil soup with whole grain roll"
    ],
    "Afternoon Snack": [
        "Carrots and hummus",
        "Small cheese and whole grain crackers",
        "A banana and a few almonds",
        "Dried fruit mix",
        "Yogurt drink"
    ],
    "Dinner": [
        "Baked salmon with steamed broccoli",
        "Beef stir-fry with bell peppers and rice",
        "Vegetarian pizza slice",
        "Tofu curry with basmati rice",
        "Spaghetti with garlic, olive oil, and chili flakes"
    ]
}

# Loop through each day, represented by each row in the magic square
for day_index, daily_numbers in enumerate(magic_square):
    
    # Initialize an empty list to hold the daily meal plan
    daily_meal_plan = []
    
    # Loop through each number in the row, each representing a meal category
    for meal_index, meal_number in enumerate(daily_numbers):
        
        # Use modulo operation to map the magic square number to a meal choice
        meal_choice_index = meal_number % 5  # We have 5 sample meals per category
        
        # Retrieve the meal for the current category and add it to the daily plan
        meal_category = list(sample_meals.keys())[meal_index]
        chosen_meal = sample_meals[meal_category][meal_choice_index]
        daily_meal_plan.append(chosen_meal)
    
    # Display the daily meal plan
    print(f"Day {day_index + 1}: {daily_meal_plan}")
