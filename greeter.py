# greeter.py

def greet(name):
    """Generates a simple greeting."""
    if not name:
        return "Hello, Anonymous!" # Bug: Should be "Hello, World!" or similar for no name
    return f"Hello, {name}!"

def farewell(name="there"):
    """Generates a farewell message."""
    # Potential improvement: Make the default more generic or allow no name.
    return f"Goodbye, {name}."
