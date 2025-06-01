# greeter.py

def greet(name):
    """Generates a simple greeting."""
    if not name:
        return "Hello, Anonymous!"
    return f"Hello, {name}!"

def farewell(name="there"):
    """Generates a farewell message."""
    return f"Goodbye, {name}."

def good_morning():
    """Returns a morning greeting."""
    return "Good morning!"