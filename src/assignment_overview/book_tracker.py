def dashboard():
    """Prints
    40 '='
        YOUR LIBRARY
    40 '='
    """
    print("=" * 40)
    print("    YOUR LIBRARY")
    print("=" * 40)


def estimate_reading_time(pages):
    """Return estimated reading time in hours, assuming 40 pages/hour.
    This number should be rounded to 1 decimal place"""
    return round(pages / 40, 1)


def add_book():
    """
    This function takes in user input for title, author, and page count.
    Create a variable called hours that calls the function estimate_reading_time
    """
    title = input("Book title: ").title()
    author = input("Author: ")
    pages = int(input("Page count: "))
    hours = estimate_reading_time(pages)
    print(f"'{title}' by {author} -- approx. {hours} hours to read")


def main():
    dashboard()
    add_book()


if __name__ == "__main__":
    main()