import math
from triangle import classify_triangle, is_valid_triangle
def test_equilateral():
    assert classify_triangle(1, 1, 1) == "Equilateral"
    assert classify_triangle(2, 2, 2) == "Equilateral"
    assert classify_triangle(0.5, 0.5, 0.5) == "Equilateral"

def test_isosceles():
    assert classify_triangle(2, 2, 3) == "Isosceles"
    assert classify_triangle(3, 2, 2) == "Isosceles"
    assert classify_triangle(2, 3, 2) == "Isosceles"

def test_scalene():
    assert classify_triangle(4, 5, 6) == "Scalene"
    assert classify_triangle(6, 4, 5) == "Scalene"
    assert classify_triangle(5, 6, 4) == "Scalene"

def test_right_scalene():
    assert classify_triangle(3, 4, 5) == "Right Scalene"
    assert classify_triangle(5, 3, 4) == "Right Scalene"
    assert classify_triangle(4, 5, 3) == "Right Scalene"

def test_right_isosceles():
    assert classify_triangle(1, 1, math.sqrt(2)) == "Right Isosceles"
    assert classify_triangle(math.sqrt(2), 1, 1) == "Right Isosceles"
    assert classify_triangle(1, math.sqrt(2), 1) == "Right Isosceles"

def test_invalid_nonpositive():
    assert classify_triangle(0, 1, 1) == "Invalid"
    assert classify_triangle(-1, 1, 1) == "Invalid"
    assert classify_triangle(1, -1, 1) == "Invalid"
    assert classify_triangle(1, 1, -1) == "Invalid"

def test_invalid_inequality():
    assert classify_triangle(1, 2, 10) == "Invalid"
    assert classify_triangle(10, 1, 2) == "Invalid"
    assert classify_triangle(2, 10, 1) == "Invalid"

def test_degenerate():
    assert classify_triangle(1, 2, 3) == "Invalid"
    assert classify_triangle(2, 3, 5) == "Invalid"
    assert classify_triangle(5, 1, 4) == "Invalid"