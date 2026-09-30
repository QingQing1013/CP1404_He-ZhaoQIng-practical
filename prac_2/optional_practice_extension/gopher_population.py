"""CP1404 Practical 02 extension - Simulate a gopher population."""

import random

STARTING_POPULATION = 1000
NUMBER_OF_YEARS = 10
MINIMUM_BIRTH_RATE = 0.10
MAXIMUM_BIRTH_RATE = 0.20
MINIMUM_DEATH_RATE = 0.05
MAXIMUM_DEATH_RATE = 0.25


def main():
    """Simulate and display ten years of gopher population changes."""
    population = STARTING_POPULATION
    print("Welcome to the Gopher Population Simulator!")
    print(f"Starting population: {population}")
    for year in range(1, NUMBER_OF_YEARS + 1):
        number_born = int(population * random.uniform(MINIMUM_BIRTH_RATE, MAXIMUM_BIRTH_RATE))
        number_died = int(population * random.uniform(MINIMUM_DEATH_RATE, MAXIMUM_DEATH_RATE))
        population += number_born - number_died
        print(f"Year {year}")
        print(f"{number_born} gophers were born. {number_died} died.")
        print(f"Population: {population}")


main()
