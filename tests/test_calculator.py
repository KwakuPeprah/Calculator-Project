import pytest
# Import all functions from the calculator module (assuming it's in calculator.py)
from calculator import add, subtract, multiply, divide, power

def test_add_integers_and_negatives():
    """Tests basic addition, including zero and negative numbers."""
    assert add(3, 5) == 8
    assert add(-1, 1) == 0
    assert add(0, 100) == 100
    
def test_add_floats():
    """Tests addition with floating point numbers."""
    # Use pytest.approx for float comparisons to account for precision issues
    assert add(0.1, 0.2) == pytest.approx(0.3)
    assert add(5.5, -2.2) == pytest.approx(3.3)


def test_subtract_integers_and_negatives():
    """Tests basic subtraction, including double negatives."""
    assert subtract(10, 3) == 7
    assert subtract(-1, -1) == 0
    assert subtract(5, 10) == -5
    assert subtract(0, 5) == -5

def test_multiply_basics_and_zero():
    """Tests basic multiplication, including negative factors and zero."""
    assert multiply(4, 5) == 20
    assert multiply(-3, 3) == -9
    assert multiply(100, 0) == 0
    assert multiply(2.5, 4) == pytest.approx(10.0)

def test_divide_basics_and_floats():
    """Tests division on integers and floating-point results."""
    assert divide(10, 2) == 5.0
    assert divide(1, 3) == pytest.approx(0.3333333333333333)
    assert divide(10, -5) == -2.0
    
def test_divide_by_zero():
    """Tests that division by zero raises the expected ValueError."""
    # Use pytest.raises context manager for exception testing
    with pytest.raises(ValueError):
        divide(10, 0)
    with pytest.raises(ValueError):
        divide(0, 0)

def test_power_positive_and_fractional():
    """Tests positive and fractional exponents."""
    assert power(2, 3) == 8
    assert power(4, 0.5) == 2.0
    assert power(2, 10) == pytest.approx(1024)

def test_power_negative_and_zero_exponent():
    """Tests negative and zero exponents."""
    assert power(5, 0) == 1
    assert power(2, -1) == pytest.approx(0.5)
