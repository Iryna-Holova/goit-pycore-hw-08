"""Actions module."""

from decorators import input_error
from address_book import AddressBook
from record import Record


@input_error
def add_contact(args: list, book: AddressBook) -> str:
    """
    Adds a new contact to the `book` if the name is not already in the
    `book` or adds the phone number to an existing contact.

    Args:
        args (list): A list containing the name and phone number of the
        contact.
        book (AddressBook): An instance of the `AddressBook` class.

    Returns:
        str: A message indicating whether the contact was added or updated, or
        if the input is invalid.
    """
    if len(args) < 2:
        raise ValueError("❌ Invalid input. Provide name and phone number.")
    name, phone = args

    record = book.find(name)
    if record:
        record.add_phone(phone)
        return "✅ Contact updated."
    new_record = Record(name)
    new_record.add_phone(phone)
    book.add_record(new_record)
    return "✅ Contact added."


@input_error
def change_contact(args: list, book: AddressBook) -> str:
    """
    Changes an existing contact's phone number in the address book.

    Args:
        args (list): A list containing the name, old phone number, and new
        phone number of the contact.
        book (AddressBook): An instance of the AddressBook class.

    Returns:
        str: A message indicating whether the contact was updated or if the
        input is invalid.
    """
    if len(args) < 3:
        raise ValueError(
            "❌ Invalid input. Provide name, old phone and new phone.")
    name, old_phone, new_phone = args

    record = book.find(name)
    if not record:
        return "❌ Contact not found."
    record.edit_phone(old_phone, new_phone)
    return "✅ Contact updated."


@input_error
def get_phones(args: list, book: AddressBook) -> str:
    """
    Returns a string containing the phone numbers of the contact with the
    given name in the `book`.

    Args:
        args (list): A list containing the name of the contact.
        book (AddressBook): An instance of the `AddressBook` class.

    Returns:
        str: A string containing the phone numbers of the contact with the
        given name. If the contact is not found, a message indicating that
        the contact is not found is returned.
    """
    if len(args) < 1:
        raise ValueError("❌ Invalid input. Provide name.")
    name = args[0]

    record = book.find(name)
    if not record:
        return "❌ Contact not found."
    print(record)


def get_contacts(book: AddressBook) -> str:
    """
    Returns a string containing the names and phone numbers of all contacts
    in the `book`.

    Args:
        book (AddressBook): An instance of the `AddressBook` class.

    Returns:
        str: A string containing the names and phone numbers of all contacts
        in the `book`.
    """
    if not book.data:
        return "❗ There are no contacts."

    contacts = book.data
    return "\n".join([str(record) for record in contacts.values()])


@input_error
def add_birthday(args: list, book: AddressBook) -> str:
    """
    Adds a birthday to the contact with the given name in the `book`.

    Args:
        args (list): A list containing the name and birthday of the contact.
        book (AddressBook): An instance of the `AddressBook` class.

    Returns:
        str: A message indicating whether the birthday was added or if the
        input is invalid.
    """
    if len(args) < 2:
        raise ValueError("❌ Invalid input. Provide name and birthday.")
    name, birthday = args

    record = book.find(name)
    if not record:
        return "❌ Contact not found."
    record.add_birthday(birthday)
    return "✅ Birthday added."


@input_error
def show_birthday(args: list, book: AddressBook) -> str:
    """
    Shows the birthday of the contact with the given name in the `book`.

    Args:
        args (list): A list containing the name of the contact.
        book (AddressBook): An instance of the `AddressBook` class.

    Returns:
        str: A string containing the birthday of the contact with the given
        name. If the contact is not found, a message indicating that the
        contact is not found is returned.
    """
    if len(args) < 1:
        raise ValueError("❌ Invalid input. Provide name.")
    name = args[0]

    record = book.find(name)
    if not record:
        return "❌ Contact not found."
    return f"🎂 Birthday: {record.birthday}"


@input_error
def birthdays(book: AddressBook) -> str:
    """
    Returns a string containing the names and congratulation dates of all
    contacts in the `book` who have a birthday within the next 7 days.

    Args:
        book (AddressBook): An instance of the `AddressBook` class.

    Returns:
        str: A string containing the names and congratulation dates of all
        contacts in the `book` who have a birthday within the next 7 days.
    """
    return "\n".join([str(record) for record in book.get_upcoming_birthdays()])
