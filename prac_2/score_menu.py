"""CP1404 Practical 02 - Use a menu to work with a valid score."""

MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASSABLE_THRESHOLD = 50

MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    """Run the score menu until the user chooses to quit."""
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(determine_score_result(score))
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell.")


def get_valid_score():
    """Get and return a score from 0 to 100 inclusive."""
    score = int(input("Enter score: "))
    while score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score


def determine_score_result(score):
    """Return the result category for a valid score."""
    if score >= EXCELLENT_THRESHOLD:
        return "Excellent"
    if score >= PASSABLE_THRESHOLD:
        return "Passable"
    return "Bad"


def print_stars(score):
    """Print as many stars as the score."""
    print("*" * score)


main()
