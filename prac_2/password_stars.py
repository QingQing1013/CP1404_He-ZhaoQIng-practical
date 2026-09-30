"""CP1404 Practical 02 - Validate a password and display stars."""

MINIMUM_PASSWORD_LENGTH = 8


def main():
    """Get a valid password and display one star for each character."""
    password = get_password()
    print_password_stars(password)


def get_password():
    """Get and return a password that meets the minimum length."""
    password = input("Enter password: ")
    while len(password) < MINIMUM_PASSWORD_LENGTH:
        print(f"Password must be at least {MINIMUM_PASSWORD_LENGTH} characters long")
        password = input("Enter password: ")
    return password


def print_password_stars(password):
    """Print one star for each character in the supplied password."""
    print("*" * len(password))


main()
