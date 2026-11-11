
def is_palindrome(text: str) -> bool:
    """Return whether text reads the same forward and backward."""
    normalized = "".join(char.lower() for char in text if char.isalnum())
    return bool(normalized) and normalized == normalized[::-1]


print(is_palindrome("racecar"))  # True (word)
print(is_palindrome("A man, a plan, a canal: Panama"))  # True (sentence)
print(is_palindrome("This is not one"))  # False