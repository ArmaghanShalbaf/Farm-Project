# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 09:37:46 2023

@author: Armaghan Shalbaf
"""
# Import necessary modules
from typing import Dict, List
import unittest
import pandas as pd
import matplotlib.pyplot as plt

# Define the Cow class
class Cow:
    
    # Initialize the Cow object with its breed, feed type, and milk yield
    def __init__(self, breed: str, feed_type: str, milk_yield: int):
        self.breed = breed
        self.feed_type = feed_type
        self.milk_yield = milk_yield
        
# Define the Farm class
class Farm:
    
    # Initialize the Farm object with a list of cows
    def __init__(self, cows: List[Cow]):
        self.cows = cows

# Define the calculate_milk_yield_by_breed_and_feed_type function
def calculate_milk_yield_by_breed_and_feed_type(farm: Farm) -> Dict[str, Dict[str, int]]:
    # Create a dictionary to hold the total milk yield by feed type
    total_milk_yield_by_feed_type: Dict[str, int] = {"Corn": 0, "Grass": 0, "Grain": 0}

# Calculate the total milk yield by feed type
    for cow in farm.cows:
        total_milk_yield_by_feed_type[cow.feed_type] += cow.milk_yield

# Create a dictionary to hold the milk yield by breed and feed type
    milk_yield_by_breed_and_feed_type: Dict[str, Dict[str, int]] = {}

# Calculate the milk yield by breed and feed type
    for cow in farm.cows:
        breed = cow.breed
        feed_type = cow.feed_type
        milk_yield = cow.milk_yield
        if breed not in milk_yield_by_breed_and_feed_type:
            milk_yield_by_breed_and_feed_type[breed] = {"Corn": 0, "Grass": 0, "Grain": 0}
        milk_yield_by_breed_and_feed_type[breed][feed_type] += milk_yield

    # Create a pandas DataFrame for the table
    milk_yield_df = pd.DataFrame(milk_yield_by_breed_and_feed_type).transpose()
    milk_yield_df['Total'] = milk_yield_df.sum(axis=1)
    print(milk_yield_df)

    # Create plots
    milk_yield_df.drop(columns='Total').plot(kind='bar', stacked=True)
    plt.title('Milk Yield by Breed and Feed Type')
    plt.ylabel('Milk Yield (Gallons)')
    plt.show()

    milk_yield_df['Total'].plot(kind='bar')
    plt.title('Total Milk Yield by Breed')
    plt.ylabel('Milk Yield (Gallons)')
    plt.show()

# Return the milk yield by breed and feed type dictionary
    return milk_yield_by_breed_and_feed_type


# Define the unit test for the calculate_milk_yield_by_breed_and_feed_type function
class TestCalculateMilkYieldByBreedAndFeedType(unittest.TestCase):
    
    # Test that the function produces the expected output for a specific set of inputs
    def test_calculate_milk_yield_by_breed_and_feed_type(self):
        cows = [
            Cow("Holstein", "Corn", 20),
            Cow("Jersey", "Grass", 10),
            Cow("Holstein", "Grain", 15),
            Cow("Jersey", "Corn", 5),
        ]
        farm = Farm(cows)
        result = calculate_milk_yield_by_breed_and_feed_type(farm)
        expected_result = {
            "Holstein": {"Corn": 20, "Grass": 0, "Grain": 15},
            "Jersey": {"Corn": 5, "Grass": 10, "Grain": 0},
        }
        # Assert that the actual result matches the expected result
        self.assertEqual(result, expected_result)

# Run the unit test if this script is being run directly
if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

# Create a list of cows to test the function with
    cows = [
        Cow("Holstein", "Corn", 20),
        Cow("Jersey", "Grass", 10),
        Cow("Holstein", "Grain", 15),
        Cow("Jersey", "Corn", 5),
    ]
    
    # Create a farm object with the list of cows
    farm = Farm(cows)
    
    # Calculate the milk yield by breed and feed type
    milk_yield_by_breed_and_feed_type = calculate_milk_yield_by_breed_and_feed_type(farm)

  # Create a bar chart to visualize the milk yield by breed and feed type
    milk_yield_df = pd.DataFrame(milk_yield_by_breed_and_feed_type).transpose()
    milk_yield_df.plot(kind='bar', stacked=True)
    plt.title('Milk Yield by Breed and Feed Type')
    plt.xlabel('Breed')
    plt.ylabel('Milk Yield (Gallons)')
    plt.xticks(rotation=0)
    plt.legend(title='Feed Type')
    plt.show()

    # Create a pie chart to visualize the total milk yield by breed
    total_milk_yield = milk_yield_df.sum(axis=1)
    plt.pie(total_milk_yield, labels=total_milk_yield.index, autopct='%.1f%%', startangle=90)
    plt.title('Total Milk Yield by Breed')
    plt.axis('equal')
    plt.show()
