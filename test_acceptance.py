from triangle import classify_triangle


def test_acceptance():
    #Criterion 1: Invalid triangles return "Invalid"
    invalid_cases = [
        (1, 2, 3),
        (1, 1, 3),
        (0, 4, 5),
        (-1, 4, 5)
]
    for sides in invalid_cases:
        assert classify_triangle(*sides) == "Invalid"

    # Criterion 2: Valid triangles are classified correctly
    assert classify_triangle(3, 3, 3) == "Equilateral"
    assert classify_triangle(3, 3, 4) == "Isosceles"
    assert classify_triangle(4, 5, 6) == "Scalene"

    # Criterion 3: Right triangles are flagged correctly
    assert classify_triangle(3, 4, 5) == "Right Scalene"
    assert classify_triangle(5, 12, 13) == "Right Scalene"
    assert "Right" not in classify_triangle(4, 5, 6)
