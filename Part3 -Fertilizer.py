# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 10:15:10 2023

@author: Armaghan Shalbaf
"""

import matplotlib.pyplot as plt
from typing import List, Dict
from enum import Enum
import unittest

# Define an enumeration for food types
class FoodType(Enum):
    GRAIN = 'grain'
    CORN = 'corn'
    GRASS = 'grass'
    
# Define a class for breed of cows
class Breed:
    def __init__(self, name: str, food_effects: dict):
        self.name = name
        self.food_effects = food_effects

# Return the fertilizer production for a specific food type and breed
    def get_fertilizer_production(self, food: FoodType) -> float:
        return self.food_effects[food].get('fertilizer', 0)

# Define a class for a farm with a list of breeds
class Farm:
    def __init__(self, breeds: List[Breed]):
        self.breeds = breeds

# Calculate the food production for a specific food type and all breeds on the farm
    def calculate_food_production(self, food: FoodType, soil_size: int = 1000) -> dict:
        food_production = {}

        for breed in self.breeds:
            fertilizer = breed.get_fertilizer_production(food)
            food_production[breed.name] = soil_size * fertilizer

        return food_production

# Define a test class for the Farm class
class TestFarm(unittest.TestCase):
    def setUp(self):
        
        # Create some breeds with different fertilizer production rates for different food types
        self.jersey = Breed('Jersey', {
            FoodType.GRAIN: {'fertilizer': 0.008},
            FoodType.CORN: {'fertilizer': 0.011},
            FoodType.GRASS: {'fertilizer': 0.005}
        })

        self.guernsey = Breed('Guernsey', {
            FoodType.GRAIN: {'fertilizer': 0.009},
            FoodType.CORN: {'fertilizer': 0.012},
            FoodType.GRASS: {'fertilizer': 0.006}
        })

        self.holstein = Breed('Holstein', {
            FoodType.GRAIN: {'fertilizer': 0.010},
            FoodType.CORN: {'fertilizer': 0.013},
            FoodType.GRASS: {'fertilizer': 0.007}
        })

        self.ayrshire = Breed('Ayrshire', {
            FoodType.GRAIN: {'fertilizer': 0.011},
            FoodType.CORN: {'fertilizer': 0.014},
            FoodType.GRASS: {'fertilizer': 0.008}
        })

# Create a farm object with the list of breeds
        self.breeds = [self.jersey, self.guernsey, self.holstein, self.ayrshire]
        self.farm = Farm(self.breeds)

# Define a test function for the calculate_food_production method of the Farm class
    def test_calculate_food_production(self):
        expected_result_grain = {'Jersey': 8, 'Guernsey': 9, 'Holstein': 10, 'Ayrshire': 11}
        expected_result_corn = {'Jersey': 11, 'Guernsey': 12, 'Holstein': 13, 'Ayrshire': 14}
        expected_result_grass = {'Jersey': 5, 'Guernsey': 6, 'Holstein': 7, 'Ayrshire': 8}

# Check the calculated food production 
        self.assertEqual(self.farm.calculate_food_production(FoodType.GRAIN), expected_result_grain)
        self.assertEqual(self.farm.calculate_food_production(FoodType.CORN), expected_result_corn)
        self.assertEqual(self.farm.calculate_food_production(FoodType.GRASS), expected_result_grass)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

# Define data for different breeds of animals and their food effects
    breeds_data = [
        ('Jersey', {
            FoodType.GRAIN: {'fertilizer': 0.008},
            FoodType.CORN: {'fertilizer': 0.011},
            FoodType.GRASS: {'fertilizer': 0.005}
        }),
        ('Guernsey', {
            FoodType.GRAIN: {'fertilizer': 0.009},
            FoodType.CORN: {'fertilizer': 0.012},
            FoodType.GRASS: {'fertilizer': 0.006}
        }),
        ('Holstein', {
            FoodType.GRAIN: {'fertilizer': 0.010},
            FoodType.CORN: {'fertilizer': 0.013},
            FoodType.GRASS: {'fertilizer': 0.007}
        }),
        ('Ayrshire', {
            FoodType.GRAIN: {'fertilizer': 0.011},
            FoodType.CORN: {'fertilizer': 0.014},
            FoodType.GRASS: {'fertilizer': 0.008}
        }),
    ]

# Create breeds objects using the Breed class
    breeds = [Breed(name, food_effects) for name, food_effects in breeds_data]
    
    # Create a farm object using the Farm class
    farm = Farm(breeds)

# Print fertilizer production for each breed of animal for each food type
    for breed in breeds:
        print(f'Fertilizer production for {breed.name}:')
        for food in FoodType:
            fertilizer = breed.get_fertilizer_production(food)
            print(f'{food.value}: {fertilizer * 1000} lbs')
        print()

# Print food production for each breed of animal for each food type
    for food in FoodType:
        print(f'Food production for {food.value}:')
        food_production = farm.calculate_food_production(food)
        for breed, production in food_production.items():
            print(f'{breed}: {production} lbs')
        print()


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

    breeds_data = [
        ('Jersey', {
            FoodType.GRAIN: {'fertilizer': 0.008},
            FoodType.CORN: {'fertilizer': 0.011},
            FoodType.GRASS: {'fertilizer': 0.005}
        }),
        ('Guernsey', {
            FoodType.GRAIN: {'fertilizer': 0.009},
            FoodType.CORN: {'fertilizer': 0.012},
            FoodType.GRASS: {'fertilizer': 0.006}
        }),
        ('Holstein', {
            FoodType.GRAIN: {'fertilizer': 0.010},
            FoodType.CORN: {'fertilizer': 0.013},
            FoodType.GRASS: {'fertilizer': 0.007}
        }),
        ('Ayrshire', {
            FoodType.GRAIN: {'fertilizer': 0.011},
            FoodType.CORN: {'fertilizer': 0.014},
            FoodType.GRASS: {'fertilizer': 0.008}
        }),
    ]

    breeds = [Breed(name, food_effects) for name, food_effects in breeds_data]
    farm = Farm(breeds)

# Create bar plots for fertilizer and food production by breed and food type using matplotlib library
    breed_names = [breed.name for breed in breeds]

    # Create bar plots for fertilizer production
    fig, ax = plt.subplots()
    bar_width = 0.25
    index = 0
    for food in FoodType:
        fertilizers = [breed.get_fertilizer_production(food) * 1000 for breed in breeds]
        x_pos = [i + index * bar_width for i, _ in enumerate(breeds)]
        ax.bar(x_pos, fertilizers, width=bar_width, label=food.value)
        index += 1

    ax.set_xticks([i + bar_width for i, _ in enumerate(breeds)])
    ax.set_xticklabels(breed_names)
    ax.set_xlabel("Breeds")
    ax.set_ylabel("Fertilizer Production (lbs)")
    ax.set_title("Fertilizer Production by Breed and Food Type")
    ax.legend()
    plt.show()

    # Create bar plots for food production
    fig, ax = plt.subplots()
    index = 0
    for food in FoodType:
        food_production = farm.calculate_food_production(food)
        productions = list(food_production.values())
        x_pos = [i + index * bar_width for i, _ in enumerate(breeds)]
        ax.bar(x_pos, productions, width=bar_width, label=food.value)
        index += 1

    ax.set_xticks([i + bar_width for i, _ in enumerate(breeds)])
    ax.set_xticklabels(breed_names)
    ax.set_xlabel("Breeds")
    ax.set_ylabel("Food Production (lbs)")
    ax.set_title("Food Production by Breed and Food Type")
    ax.legend()
    plt.show()
