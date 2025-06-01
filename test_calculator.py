# test_calculator.py
import pytest
from calculator import exponentiate

def test_exponentiate():
    assert exponentiate(2, 3) == 8
    assert exponentiate(5, 0) == 1
    assert exponentiate(7, 1) == 7
    assert exponentiate(2, -2) == 0.25