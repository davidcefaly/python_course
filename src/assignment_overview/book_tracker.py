def dashboard():
    """Prints
    40 '='
        YOUR LIBRARY
    40 '='
    """
    print("=" * 40)
    print("  📚   YOUR LIBRARY")
    print("=" * 40)


def estimate_reading_time(pages):
    """Return estimated reading time in hours, assuming 40 pages/hour.
    This number should be rounded to 1 decimal place"""
    return round(pages / 40, 1)


def show_menu():
    """Prints the menu options, asks the user for a choice,
    and returns what they typed (stripped and lowercase)"""
    print()
    print("  What would you like to do?")
    print()
    print("  1) View books")
    print("  2) Add a book")
    print()
    print("  q) Quit")
    print()
    choice = input("> ")
    return choice.strip().lower()


def add_book(library):
    """
    This function takes in user input for title, author, and page count.
    Create a variable called hours that calls the function estimate_reading_time.
    Stores the book as a dictionary and adds it to the library list.
    """
    title = input("Book title: ").title()
    author = input("Author: ")
    pages = int(input("Page count: "))
    hours = estimate_reading_time(pages)

    book = {
        "title": title,
        "author": author,
        "pages": pages,
        "hours": hours,
    }
    library.append(book)

    print()
    print("Book added:")
    print()
    print(f"  '{title}' by {author} -- approx. {hours} hours to read")


def view_books(library):
    """Prints every book in the library with a number in front,
    or a message if the library is empty"""
    if len(library) == 0:
        print("Your library is empty. Add a book first!")
    else:
        for i in range(len(library)):
            book = library[i]
            print(f"{i + 1}. '{book['title']}' - {book['author']} ({book['pages']} pages - approx. {book['hours']} hours to read)")


def main():
    library = []
    dashboard()

    while True:
        choice = show_menu()

        if choice == "1":
            view_books(library)
        elif choice == "2":
            add_book(library)
        elif choice == "q" or choice == "quit" or choice == "exit":
            print("Goodbye!")
            break
        else:
            print("Sorry, that option isn't available.")


if __name__ == "__main__":
    main()