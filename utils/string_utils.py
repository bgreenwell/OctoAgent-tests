# utils/string_utils.py

def reverse_string(s):
    """Reverses a given string."""
    return s[::-1]

def capitalize_words(s):
    """Capitalizes each word in a string, handling multiple spaces."""
    # Using split() without arguments to handle multiple spaces and trimming
    words = s.split()
    capitalized_words = [word.capitalize() for word in words]
    return " ".join(capitalized_words)

def is_palindrome(s):
    """
    Checks if a string is a palindrome.
    Ignores spaces and case.
    """
    processed_s = ''.join(s.split()).lower()
    # Check if the processed string is the same forwards and backwards
    return processed_s == processed_s[::-1]