# calculator.py

def add(x, y):
    """Adds two numbers."""
    return x + y

def subtract(x, y):
    """Subtracts second number from the first."""
    return x - y

def multiply(x, y):
    """Multiplies two numbers."""
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
    """Calculates base raised to the power of exponent.
    
    Parameters:
        base (float): The base number.
        exponent (float): The exponent number.
    
    Returns:
        float: The result of base ** exponent.
    
    Raises:
        TypeError: If base or exponent is not a number.
    """
    if not isinstance(base, (int, float)) or not isinstance(exponent, (int, float)):
        raise TypeError("Both base and exponent must be numbers.")
    return base ** exponent