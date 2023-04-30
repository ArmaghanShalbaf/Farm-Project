# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 18:38:00 2023

@author: Sajjad
"""

import typing

# Define cow types and food costs
COW_TYPES = {
    "Holstein": {"Corn": 25, "Grain": 45, "Grass": 30},
    "Jersey": {"Corn": 20, "Grain": 40, "Grass": 35},
    "Guernsey": {"Corn": 22, "Grain": 42, "Grass": 32},
    "Ayrshire": {"Corn": 24, "Grain": 44, "Grass": 28},
}

def calculate_cost_per_week(cow_counts: typing.Dict[str, int]) -> float:
    """
    Calculates the cost per week of feeding the cows based on their breed and food intake.

    Parameters:
        cow_counts (Dict[str, int]): A dictionary where keys are cow breeds (Holstein, Jersey, Guernsey, Ayrshire)
                                     and values are the number of cows of that breed.

    Returns:
        float: The total cost per week of feeding the cows.
    """
    total_cost = 0
    for cow_breed, count in cow_counts.items():
        for food_type, cost in COW_TYPES[cow_breed].items():
            total_cost += cost * count
    return total_cost

if __name__ == "__main__":
    # Define the cow counts for each breed
    cow_counts = {"Holstein": 10, "Jersey": 5, "Guernsey": 3, "Ayrshire": 2}

    # Calculate the cost per week of feeding the cows
    cost_per_week = calculate_cost_per_week(cow_counts)

    # Print the cost per week of feeding the cows
    print(f"The cost per week of feeding the cows is: ${cost_per_week:.2f}")
