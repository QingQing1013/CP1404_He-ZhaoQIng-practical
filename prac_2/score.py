"""CP1404 Practical 02 - Determine results for user and random scores."""

import random

MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASSABLE_THRESHOLD = 50


def main():
    """Display results for a user-entered score and a random score."""
    score = float(input("Enter score: "))
    result = determine_score_result(score)
    print(f"User score {score} is {result}")
    if result == "Excellent":
        print("You get a prize!")

    random_score = random.randint(MINIMUM_SCORE, MAXIMUM_SCORE)
    random_result = determine_score_result(random_score)
    print(f"Random: {random_score} = {random_result}")


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
