"""Main module."""

from serialize import save_data, load_data
from helpers import parse_input
from actions import (
    add_contact,
    change_contact,
    get_phones,
    get_contacts,
    add_birthday,
    show_birthday,
    birthdays,
)


def main():
    """
    The main function that serves as the entry point for the application.
    """
    book = load_data()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            save_data(book)
            break

        if command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(get_phones(args, book))

        elif command == "all":
            print(get_contacts(book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(book))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
