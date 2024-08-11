"""Helpers module."""


def parse_input(user_input: str) -> tuple:
    """
    Parses the user input string and returns a tuple containing the command
    and any arguments.

    Args:
        user_input (str): The user input string to be parsed.

    Returns:
        tuple: A tuple containing the command and any arguments. The command
        is a lowercase string without leading or trailing whitespace. The
        arguments are a tuple of strings.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args
