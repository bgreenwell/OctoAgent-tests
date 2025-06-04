# math_ops.py

"""
This module provides a collection of mathematical operations.
"""

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
    """Calculates the base raised to the power of exponent.
    
    Args:
        base (float): the base number.
        exponent (int): the exponent number. 
        
    Returns:
        float: result of base raised to the power of exponent.
        
    Note:
        Handles negative exponents and zero appropriately.
    """
    return base ** exponent