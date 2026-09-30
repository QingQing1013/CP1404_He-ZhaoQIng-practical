"""CP1404 Practical 02 practice - Write random score results to a file."""

import random

MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASSABLE_THRESHOLD = 50
OUTPUT_FILENAME = "results.txt"


def main():
    """Generate random scores and write their results to a file."""
    number_of_scores = int(input("Number of scores: "))
    with open(OUTPUT_FILENAME, "w", encoding="utf-8") as output_file:
        for _ in range(number_of_scores):
            score = random.randint(MINIMUM_SCORE, MAXIMUM_SCORE)
            result = determine_score_result(score)
            print(f"{score} is {result}", file=output_file)
    print(f"Results written to {OUTPUT_FILENAME}")


def determine_score_result(score):
    """Return the result category for a score."""
    if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        return "Invalid score"
    if score >= EXCELLENT_THRESHOLD:
        return "Excellent"
    if score >= PASSABLE_THRESHOLD:
        return "Passable"
    return "Bad"


main()
