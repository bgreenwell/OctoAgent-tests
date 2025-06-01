# greeter.py

def greet(name):
    """Generates a simple greeting."""
    if not name:
        return "Hello, World!" # Changed from "Hello, Anonymous!" to "Hello, World!"
    return f"Hello, {name}!"

def farewell(name="there"):
    """Generates a farewell message."""
    # Potential improvement: Make the default more generic or allow no name.
    return f"Goodbye, {name}."

def good_morning():
    """Returns a good morning greeting."""
    return "Good morning!"