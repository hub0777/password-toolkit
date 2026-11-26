"""Ciphers for encoding and decoding text.

Cipher is the base (parent) class. CaesarCipher inherits from it.
"""


class Cipher:
    """Base class for every cipher. Stores the shift and describes the cipher."""

    def __init__(self, shift):
        """Save the shift (how many places each character moves)."""
        self.shift = shift

    def describe(self):
        """Return a short description. Child classes inherit this as it is."""
        return type(self).__name__ + " with shift " + str(self.shift)

    def encode(self, text):
        """Encode text. Each child class must write its own version."""
        raise NotImplementedError("Subclasses must implement encode()")

    def decode(self, text):
        """Decode text. Each child class must write its own version."""
        raise NotImplementedError("Subclasses must implement decode()")


class CaesarCipher(Cipher):
    """Caesar cipher: moves each letter and digit forward by the shift."""

    def shift_character(self, char, amount):
        """Move one character by `amount` places, wrapping around at the end."""
        if char.isupper():
            base = ord("A")
            size = 26
        elif char.islower():
            base = ord("a")
            size = 26
        elif char.isdigit():
            base = ord("0")
            size = 10
        else:
            # Spaces and symbols stay the same
            return char

        position = ord(char) - base
        new_position = (position + amount) % size
        return chr(new_position + base)

    def shift_text(self, text, amount):
        """Shift every character in the text and return the new text."""
        result = []
        for char in text:
            new_char = self.shift_character(char, amount)
            result.append(new_char)
        return "".join(result)

    def encode(self, text):
        """Encode by shifting forward."""
        return self.shift_text(text, self.shift)

    def decode(self, text):
        """Decode by shifting backward (the opposite direction)."""
        return self.shift_text(text, -self.shift)
