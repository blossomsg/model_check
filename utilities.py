"""Modules for utilities"""
from typing import List


def joinmylist(value: List[str]) -> str:
    """This function is to return items of list as strings.

    Args:
        value (List(str)): List of string items.

    Returns:
        Comma separated Strings.

    """
    return ", ".join(value) if value else ""
