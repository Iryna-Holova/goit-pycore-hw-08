"""Fields module."""

from datetime import datetime
from typing import Any
import re

PHONE_REGEXP = r'^\d{10}$'


class Field:
    """
    Base class for fields.

    Attributes:
        value (Any): The value of the field.
    """

    def __init__(self, value: Any) -> None:
        """
        Initialize a field.

        Args:
            value (Any): The value of the field.
        """
        self.value = value

    def __str__(self) -> str:
        """
        Return the string representation of the field.

        Returns:
            str: The string representation of the field.
        """
        return str(self.value)


class Name(Field):
    """
    Class representing a name field.
    """

    def __init__(self, contact_name: str) -> None:
        """
        Initialize a name field.

        Args:
            contact_name (str): The name of the contact.

        Raises:
            ValueError: If the contact name is empty.
        """
        if not contact_name.strip():
            raise ValueError("❌ Name cannot be empty")
        super().__init__(contact_name)


class Phone(Field):
    """
    Class representing a phone field.
    """

    def __init__(self, phone: str) -> None:
        """
        Initialize a phone field.

        Args:
            phone (str): The phone number.

        Raises:
            ValueError: If the phone number does not consist of 10 digits.
        """
        if not re.match(PHONE_REGEXP, phone):
            raise ValueError("❌ Phone number must consist of 10 digits")
        super().__init__(phone)

    def __eq__(self, other) -> bool:
        return isinstance(other, Phone) and self.value == other.value


class Birthday(Field):
    """
    Class representing a birthday field.
    """

    def __init__(self, value: str) -> None:
        try:
            birthday = datetime.strptime(value, "%d.%m.%Y").date()
            super().__init__(birthday)
        except ValueError as exc:
            raise ValueError("❌ Invalid date format. Use DD.MM.YYYY") from exc
