# utils/string_utils.py

def reverse_string(s):
    """Reverses a given string."""
    return s[::-1]

def capitalize_words(s):
    """Capitalizes each word in a string."""
    # Potential bug: does not handle multiple spaces between words well
    # or leading/trailing spaces.
    words = s.split(' ') 
    capitalized_words = [word.capitalize() for word in words]
    return " ".join(capitalized_words)

def is_palindrome(s):
    """
    Checks if a string is a palindrome.
    Ignores spaces and case.
    """
    processed_s = ''.join(s.split()).lower()
    # Bug: Does not actually check if it's a palindrome
    return True # This is a bug
