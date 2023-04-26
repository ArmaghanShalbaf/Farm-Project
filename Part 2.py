# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 10:02:00 2023

@author: Armaghan Shalbaf
"""

from typing import Dict, List
import unittest

class Cow:
    def __init__(self, breed: str, feed_type: str, milk_yield: int):
        self.breed = breed
        self.feed_type = feed_type
        self.milk_yield = milk_yield

class Farm:
    def __init__(self, cows: List[Cow]):
        self.cows = cows

# Initialize a dictionary to keep track of the total milk yield for each feed type
def calculate_milk_yield_by_breed_and_feed_type(farm: Farm) -> Dict[str, Dict[str, int]]:
    total_milk_yield_by_feed_type: Dict[str, int] = {"Corn": 0, "Grass": 0, "Grain": 0}

# Calculate the total milk yield for each feed type by iterating through each cow on the farm
    for cow in farm.cows:
        total_milk_yield_by_feed_type[cow.feed_type] += cow.milk_yield

# Initialize a dictionary to keep track of the milk yield for each breed and feed type
    milk_yield_by_breed_and_feed_type: Dict[str, Dict[str, int]] = {}

# Calculate the milk yield for each breed and feed type by iterating through each cow on the farm
    for cow in farm.cows:
        breed = cow.breed
        feed_type = cow.feed_type
        milk_yield = cow.milk_yield
        if breed not in milk_yield_by_breed_and_feed_type:
            milk_yield_by_breed_and_feed_type[breed] = {"Corn": 0, "Grass": 0, "Grain": 0}
        milk_yield_by_breed_and_feed_type[breed][feed_type] += milk_yield

# Print out the milk yield for each breed and feed type
    for breed in milk_yield_by_breed_and_feed_type:
        print(f"{breed} cows:")
        for feed_type in milk_yield_by_breed_and_feed_type[breed]:
            milk_yield = milk_yield_by_breed_and_feed_type[breed][feed_type]
            total_milk_yield_for_feed_type = total_milk_yield_by_feed_type[feed_type]
            percent_of_total_milk_yield = (milk_yield / total_milk_yield_for_feed_type) * 100
            print(f"    {feed_type} feed: {milk_yield} gallons of milk ({percent_of_total_milk_yield:.2f}% of total)")

    return milk_yield_by_breed_and_feed_type

class TestCalculateMilkYieldByBreedAndFeedType(unittest.TestCase):
    
    # Define a unit test for the calculate_milk_yield_by_breed_and_feed_type function
    def test_calculate_milk_yield_by_breed_and_feed_type(self):
        
        # Create a list of cows with different breeds, feed types, and milk yields
        cows = [
            Cow("Holstein", "Corn", 20),
            Cow("Jersey", "Grass", 10),
            Cow("Holstein", "Grain", 15),
            Cow("Jersey", "Corn", 5),
        ]
        
        # Create a farm object with the list of cows
        farm = Farm(cows)
        
        # Calculate the milk yield by breed and feed type using the function being tested
        result = calculate_milk_yield_by_breed_and_feed_type(farm)
        
        # Define the expected milk yield by breed and feed type
        expected_result = {
            "Holstein": {"Corn": 20, "Grass": 0, "Grain": 15},
            "Jersey": {"Corn": 5, "Grass": 10, "Grain": 0},
        }
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

    cows = [
        Cow("Holstein", "Corn", 20),
        Cow("Jersey", "Grass", 10),
        Cow("Holstein", "Grain", 15),
        Cow("Jersey", "Corn", 5),
    ]
    farm = Farm(cows)
    calculate_milk_yield_by_breed_and_feed_type(farm)
