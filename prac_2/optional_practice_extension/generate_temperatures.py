"""CP1404 Practical 02 extension - Generate random Fahrenheit values."""

import random

NUMBER_OF_TEMPERATURES = 15
MINIMUM_TEMPERATURE = -200
MAXIMUM_TEMPERATURE = 200
OUTPUT_FILENAME = "temps_input.txt"


def main():
    """Write random temperature values to the input file."""
    with open(OUTPUT_FILENAME, "w", encoding="utf-8") as output_file:
        for _ in range(NUMBER_OF_TEMPERATURES):
            temperature = random.uniform(MINIMUM_TEMPERATURE, MAXIMUM_TEMPERATURE)
            print(temperature, file=output_file)
    print(f"Generated {NUMBER_OF_TEMPERATURES} values in {OUTPUT_FILENAME}")


main()
