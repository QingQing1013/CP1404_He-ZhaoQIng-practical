"""CP1404 Practical 02 extension - Convert file temperatures to Celsius."""

INPUT_FILENAME = "temps_input.txt"
OUTPUT_FILENAME = "temps_output.txt"


def main():
    """Convert Fahrenheit values from the input file and write Celsius values."""
    with open(INPUT_FILENAME, "r", encoding="utf-8") as input_file:
        with open(OUTPUT_FILENAME, "w", encoding="utf-8") as output_file:
            for line in input_file:
                fahrenheit = float(line)
                celsius = convert_fahrenheit_to_celsius(fahrenheit)
                print(celsius, file=output_file)
    print(f"Converted temperatures written to {OUTPUT_FILENAME}")


def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert a Fahrenheit temperature to Celsius."""
    return 5 / 9 * (fahrenheit - 32)


main()
