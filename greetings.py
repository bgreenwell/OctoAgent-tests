# greetings.py

"""
This module provides various greeting operations.
"""

def greet(name):
    """Generates a simple greeting.
    
    Args:
        name (str): The name to greet. 
    
    Returns:
        str: A personalized greeting message.
    """
    if not name:
        return "Hello, World!"
    return f"Hello, {name}!"

def farewell(name="there"):
    """Generates a farewell message.
    
    Args:
        name (str, optional): The name to bid farewell. Defaults to 'there'.
    
    Returns:
        str: A personalized farewell message.
    """
    return f"Goodbye, {name}."

def good_morning():
    """Generates a good morning message.
    
    Returns:
        str: A good morning greeting.
        
    Note:
        In future, consider adding parameterization for internationalization.
    """
    return "Good Morning!"