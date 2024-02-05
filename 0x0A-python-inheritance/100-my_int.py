#!/usr/bin/python3
"""Class MyInt that inherit from int."""


class MyInt(int):
    """Define MyInt."""

    def __eq__(self, value):
        """Override '==' by '!='."""
        return self.real != value

    def __ne__(self, value):
        """Override '!=' by '=='."""
        return self.real == value
