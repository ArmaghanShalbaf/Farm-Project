# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 08:45:25 2023

@author: Armaghan Shalbaf
"""

import matplotlib.pyplot as plt
from typing import List, Tuple

class Cow:
    def __init__(self, breed: str, feed_type: str, milk_yield: float, ghg_emission: float):
        # Initialize Cow object with its breed, feed type, milk yield and greenhouse gas emission
        self.breed = breed
        self.feed_type = feed_type
        self.milk_yield = milk_yield
        self.ghg_emission = ghg_emission


class Pen:
    def __init__(self, breed: str, cow_count: int):
        # Initialize Pen object with its breed and cow count
        self.breed = breed
        self.cow_count = cow_count


class Farm:
    def __init__(self):
        # Initialize Farm object with empty lists for cows and pens
        self.cows: List[Cow] = []
        self.pens: List[Pen] = []

    def add_cow(self, cow: Cow) -> None:
        # Add a cow to the list of cows on the farm
        self.cows.append(cow)

    def add_pen(self, pen: Pen) -> None:
        # Add a pen to the list of pens on the farm
        self.pens.append(pen)

    def get_pen_allocation(self) -> None:
        # Print the number of cows in each pen on the farm
        for pen in self.pens:
            print(f"{pen.cow_count} {pen.breed} cows in this pen")

    def get_milk_yield(self) -> None:
        # Calculate and print the expected milk yield on the farm
        total_yield = 0.0
        for cow in self.cows:
            total_yield += cow.milk_yield
        print(f"Expected milk yield: {total_yield} gallons per day")

    def get_ghg_emissions(self) -> None:
        # Calculate and print the expected greenhouse gas emissions on the farm
        total_emissions = 0.0
        feed_emissions = {"Corn": 5.0, "Grass": 3.0, "Grain": 6.0}
        for cow in self.cows:
            emissions = cow.ghg_emission + feed_emissions[cow.feed_type]
            print(f"{cow.breed} cows fed with {cow.feed_type} will produce {emissions} kg of greenhouse gas emissions per day")
            total_emissions += emissions
        print(f"Total expected greenhouse gas emissions: {total_emissions} kg per day")

    def get_cost_estimation(self) -> None:
        # Calculate and print the estimated cost on the farm
        feed_costs = {"Corn": 3.5, "Grass": 2.5, "Grain": 4.0}
        total_cost = 0.0
        for cow in self.cows:
            feed_cost = feed_costs[cow.feed_type]
            total_cost += feed_cost
        print(f"Estimated cost: ${total_cost:.2f} per day")

# Create a Farm object

farm = Farm()
# Create Cow objects with their respective attributes
cow1 = Cow("Holstein", "Corn", 10.0, 5.0)
cow2 = Cow("Jersey", "Grass", 7.0, 4.0)
cow3 = Cow("Guernsey", "Grain", 8.0, 4.5)
cow4 = Cow("Ayrshire", "Grass", 6.0, 3.5)
# Create Pen objects with their respective attributes
pen1 = Pen("Holstein", 3)
pen2 = Pen("Jersey", 2)
pen3 = Pen("Guernsey", 4)
pen4 = Pen("Ayrshire", 5)

farm.add_cow(cow1) # Add cow1 to the farm
farm.add_cow(cow2) # Add cow2 to the farm
farm.add_cow(cow3) # Add cow3 to the farm
farm.add_cow(cow4) # Add cow4 to the farm

farm.add_pen(pen1) # Add pen1 to the farm
farm.add_pen(pen2) # Add pen2 to the farm
farm.add_pen(pen3) # Add pen3 to the farm
farm.add_pen(pen4) # Add pen4 to the farm

farm.get_pen_allocation()    # Print the number of cows in each pen
farm.get_milk_yield()        # Print the total milk yield from all cows
farm.get_ghg_emissions()     # Print the total greenhouse gas emissions from all cows
farm.get_cost_estimation()   # Print the estimated cost of feeding all cows

# Import the unittest module

import unittest
import io
from contextlib import redirect_stdout

class TestFarm(unittest.TestCase):
    def setUp(self):
        self.farm = Farm()

        self.cow1 = Cow("Holstein", "Corn", 10.0, 5.0)
        self.cow2 = Cow("Jersey", "Grass", 7.0, 4.0)
        self.cow3 = Cow("Guernsey", "Grain", 8.0, 4.5)
        self.cow4 = Cow("Ayrshire", "Grass", 6.0, 3.5)

        self.pen1 = Pen("Holstein", 3)
        self.pen2 = Pen("Jersey", 2)
        self.pen3 = Pen("Guernsey", 4)
        self.pen4 = Pen("Ayrshire", 5)

    def test_add_pen(self):
        self.farm.add_pen(self.pen1)
        self.assertEqual(len(self.farm.pens), 1)

        self.farm.add_pen(self.pen2)
        self.assertEqual(len(self.farm.pens), 2)

        self.farm.add_pen(self.pen3)
        self.assertEqual(len(self.farm.pens), 3)

        self.farm.add_pen(self.pen4)
        self.assertEqual(len(self.farm.pens), 4)

    def test_add_cow(self):
        self.farm.add_cow(self.cow1)
        self.assertEqual(len(self.farm.cows), 1)

        self.farm.add_cow(self.cow2)
        self.assertEqual(len(self.farm.cows), 2)

        self.farm.add_cow(self.cow3)
        self.assertEqual(len(self.farm.cows), 3)

        self.farm.add_cow(self.cow4)
        self.assertEqual(len(self.farm.cows), 4)

    def test_get_pen_allocation(self):
        self.farm.add_pen(self.pen1)
        self.farm.add_pen(self.pen2)
        self.farm.add_pen(self.pen3)
        self.farm.add_pen(self.pen4)

        expected_output = "3 Holstein cows in this pen\n2 Jersey cows in this pen\n4 Guernsey cows in this pen\n5 Ayrshire cows in this pen\n"
        with io.StringIO() as buf, redirect_stdout(buf):
            self.farm.get_pen_allocation()
            self.assertEqual(buf.getvalue(), expected_output)

    def test_get_milk_yield(self):
        self.farm.add_cow(self.cow1)
        self.farm.add_cow(self.cow2)
        self.farm.add_cow(self.cow3)
        self.farm.add_cow(self.cow4)

        expected_output = "Expected milk yield: 31.0 gallons per day\n"
        with io.StringIO() as buf, redirect_stdout(buf):
            self.farm.get_milk_yield()
            self.assertEqual(buf.getvalue(), expected_output)

    def test_get_ghg_emissions(self):
        self.farm.add_cow(self.cow1)
        self.farm.add_cow(self.cow2)
        self.farm.add_cow(self.cow3)
        self.farm.add_cow(self.cow4)
expected_output = "Holstein cows fed with Corn will produce 10.0 kg of greenhouse gas emissions per day\nJersey cows fed with Grass will produce 7.0 kg of greenhouse gas emissions per day\nGuernsey cows fed with Grain will produce 12.5 kg of greenhouse gas emissions per day\nAyrshire cows fed with Grass will produce 9.5 kg of greenhouse gas emissions per day\nTotal expected greenhouse gas emissions: 31.0 kg per day"
if __name__ == '__main__':
    unittest.main()


if __name__ == '__main__':
    farm.add_cow(cow1)
    farm.add_cow(cow2)
    farm.add_cow(cow3)
    farm.add_cow(cow4)

    farm.add_pen(pen1)
    farm.add_pen(pen2)
    farm.add_pen(pen3)
    farm.add_pen(pen4)

    breeds = ["Holstein", "Jersey", "Guernsey", "Ayrshire"]
    milk_yields = [cow1.milk_yield, cow2.milk_yield, cow3.milk_yield, cow4.milk_yield]
    ghg_emissions = [cow1.ghg_emission + 5, cow2.ghg_emission + 3, cow3.ghg_emission + 6, cow4.ghg_emission + 3]


    # Create pie chart for milk yield
    fig, ax = plt.subplots()
    ax.pie(milk_yields, labels=breeds, autopct="%1.1f%%", startangle=90)
    ax.axis("equal")
    ax.set_title("Milk Yield by Breed")
    plt.show()

    # Create pie chart for greenhouse gas emissionsclass TestFarm(unittest.TestCase):
    def setUp(self):
        self.farm = Farm()

        self.cow1 = Cow("Holstein", "Corn", 10.0, 5.0)
        self.cow2 = Cow("Jersey", "Grass", 7.0, 4.0)
        self.cow3 = Cow("Guernsey", "Grain", 8.0, 4.5)
        self.cow4 = Cow("Ayrshire", "Grass", 6.0, 3.5)

        self.pen1 = Pen("Holstein", 3)
        self.pen2 = Pen("Jersey", 2)
        self.pen3 = Pen("Guernsey", 4)
        self.pen4 = Pen("Ayrshire", 5)
        
# Test the add_pen method of the Farm class
    def test_add_pen(self):
        self.farm.add_pen(self.pen1)
        self.assertEqual(len(self.farm.pens), 1)

        self.farm.add_pen(self.pen2)
        self.assertEqual(len(self.farm.pens), 2)

        self.farm.add_pen(self.pen3)
        self.assertEqual(len(self.farm.pens), 3)

        self.farm.add_pen(self.pen4)
        self.assertEqual(len(self.farm.pens), 4)
        
# Test the add_cow method of the Farm class
    def test_add_cow(self):
        self.farm.add_cow(self.cow1)
        self.assertEqual(len(self.farm.cows), 1)

        self.farm.add_cow(self.cow2)
        self.assertEqual(len(self.farm.cows), 2)

        self.farm.add_cow(self.cow3)
        self.assertEqual(len(self.farm.cows), 3)

        self.farm.add_cow(self.cow4)
        self.assertEqual(len(self.farm.cows), 4)
        
# Test the get_pen_allocation method of the Farm class
    def test_get_pen_allocation(self):
        self.farm.add_pen(self.pen1)
        self.farm.add_pen(self.pen2)
        self.farm.add_pen(self.pen3)
        self.farm.add_pen(self.pen4)

        expected_output = "3 Holstein cows in this pen\n2 Jersey cows in this pen\n4 Guernsey cows in this pen\n5 Ayrshire cows in this pen\n"
        with io.StringIO() as buf, redirect_stdout(buf):
            self.farm.get_pen_allocation()
            self.assertEqual(buf.getvalue(), expected_output)
            
# Test the get_milk_yield method of the Farm class
    def test_get_milk_yield(self):
        self.farm.add_cow(self.cow1)
        self.farm.add_cow(self.cow2)
        self.farm.add_cow(self.cow3)
        self.farm.add_cow(self.cow4)

        expected_output = "Expected milk yield: 31.0 gallons per day\n"
        with io.StringIO() as buf, redirect_stdout(buf):
            self.farm.get_milk_yield()
            self.assertEqual(buf.getvalue(), expected_output)
            
# Test the get_ghg_emissions method of the Farm class
    def test_get_ghg_emissions(self):
        self.farm.add_cow(self.cow1)
        self.farm.add_cow(self.cow2)
        self.farm.add_cow(self.cow3)
        self.farm.add_cow(self.cow4)
expected_output = "Holstein cows fed with Corn will produce 10.0 kg of greenhouse gas emissions per day\nJersey cows fed with Grass will produce 7.0 kg of greenhouse gas emissions per day\nGuernsey cows fed with Grain will produce 12.5 kg of greenhouse gas emissions per day\nAyrshire cows fed with Grass will produce 9.5 kg of greenhouse gas emissions per day\nTotal expected greenhouse gas emissions: 31.0 kg per day"
if __name__ == '__main__':
    unittest.main()


if __name__ == '__main__':
    farm.add_cow(cow1)
    farm.add_cow(cow2)
    farm.add_cow(cow3)
    farm.add_cow(cow4)

    farm.add_pen(pen1)
    farm.add_pen(pen2)
    farm.add_pen(pen3)
    farm.add_pen(pen4)

    breeds = ["Holstein", "Jersey", "Guernsey", "Ayrshire"]
    milk_yields = [cow1.milk_yield, cow2.milk_yield, cow3.milk_yield, cow4.milk_yield]
    ghg_emissions = [cow1.ghg_emission + 5, cow2.ghg_emission + 3, cow3.ghg_emission + 6, cow4.ghg_emission + 3]

    fig, ax = plt.subplots()
    ax.pie(ghg_emissions, labels=breeds, autopct="%1.1f%%", startangle=90)
    ax.axis("equal")
    ax.set_title("Greenhouse Gas Emissions by Breed")
    plt.show()
