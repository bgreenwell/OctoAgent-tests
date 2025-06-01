# calculator.py

def add(x, y):
    """Adds two numbers."""
    return x + y

def subtract(x, y):
    """Subtracts second number from the first."""
    return x - y

def multiply(x, y):
    """Multiplies two numbers."""
    # Intentionally simple, could be a place for a bug (e.g., if it returned x + y)
    return x * y

def divide(x, y):
    """Divides first number by the second.
    
    Raises:
        ValueError: if y is zero.
    """
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def exponentiate(base, exponent):
    """Calculates the exponentiation of base raised to the power of exponent."""
    return base ** exponent