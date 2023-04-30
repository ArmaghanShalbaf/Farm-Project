"""
part_2.py
=========

This module contains classes for simulating a special kind of farm with cows.  
It includes the following classes:

- :class:`~farming.part2.Cow`: A class representing a *cow* with its **breed**, **feed type**, **milk yield** attributes. 
- :class:`~farming.part2.Farm`: A class representing a *farm* with a list of **cows**. 

This module also includes a test suite. 
"""

__author__ = "Armaghan"

from typing import Dict, List
import unittest

class Cow:
    """This class represents 
    a *cow* with its :attr:`breed`, :attr:`feed_type`, and :attr:`milk_yield` attributes.

    """
    def __init__(self, breed: str, feed_type: str, milk_yield: int):
        """Creates instances of the class :class:`~farming.part2.Cow`.

        :param str breed: The breed of the cow.
        :param str feed_type: The type of feed given to the cow.
        :param int milk_yield: The milk yield of the cow in gallons per day.
        """
        self.breed: str = breed  #: The breed of the cow. 
        self.feed_type: str = feed_type  #: The type of feed given to the cow.
        self.milk_yield: float = milk_yield  #: The milk yield of the cow in gallons per day.

class Farm:
    """This class represents a *farm* with a list of :attr:`cows`.
    """
    def __init__(self, cows: List[Cow]):
        """
        Initialize a new Farm object with empty lists for cows and pens.

        :param (List[Cow]) cows: A list holding cows.
        """
        self.cows: List[Cow] = cows  #: A list holding cows.

def calculate_milk_yield_by_breed_and_feed_type(farm: Farm) -> Dict[str, Dict[str, int]]:
    """Initialize a dictionary to keep track of the total milk yield for each feed type"""
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
    """The test class to calculate milk yield by breed and feed type. 
    """
    def test_calculate_milk_yield_by_breed_and_feed_type(self):
        """Define a unit test for the :func:`~farming.part2.calculate_milk_yield_by_breed_and_feed_type` function."""
        
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
