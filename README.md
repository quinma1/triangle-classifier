Matthew Quintanilla
Part 1
All three angles in a equilateral triangle are 60 degrees so none of them can be 90 degrees meaning it'll never be right.

Part 2

## Copilot Review Log

| Test | Copilot-suggested? | Kept / edited / rejected | Why |
| test_equilateral |yes            |kept| equal sides expects "Equilateral" matches spec.|
| test_isosceles |yes              |kept| exactly two equal sides valid not right.|
| test_scalene |yes                |edited| copilot used 3, 4, 5, a right triangle that should be "Right Scalene" changed to 4, 5, 6.|
| test_right_scalene|yes            |edited| moved opilot's 3, 4, 5 cases here with the correct "Right Scalene" result.|
| test_right_isosceles |yes        |kept|square root of 2 sides a == comparison in the code would fail confirming the tolerance works.|
| test_invalid_nonpositive |yes    |kept| every case has a side <= 0 and expects "Invalid". |
| test_invalid_inequality |yes     |edited| copilot used 1, 2, 3, which is degenerate, not a strict inequality failure; changed to 1, 2, 10.|
| test_degenerate |yes             |rejected| copilot expected “Scalene” for (1, 2, 3); the spec says a degenerate case is “Invalid”. rewrote the test.|

Part 3 Acceptance Criteria
Criteria 1: If the user inputs values not associated with the spec it will return "Invalid". (Ex (1,2,3) = "Invalid", (1,1,3) == "Invalid").
Criteria 2: When the user inputs values that associate with a corresponding triangle it names it as that triangle. (Ex (3,3,3) == "Equilateral", (3,3,4) == "Isosceles", (4,5,6) == "Scalene").
Criteria 3: When sides are a right triangle it labels the triangle as the corresponding triangle. (Ex (3,4,5) == "Right Scalene").

Part 4
There has been AI use in this project Claude helped explain the assigment better, Copilot suggested most of the code and if there was any problems i corrected them. Claude also helped out when i was having trouble uploading to github. 
How to Run the Tests
1. Install dependencies: `python -m pip install -r requirements.txt`
2. Run all tests: `python -m pytest -v`

## Equivalence Classes and Boundaries

Equivalence classes:
1. Invalid: any side <= 0
2. Invalid: triangle inequality fails (two sides sum to less than the third)
3. Equilateral: all sides equal
4. Isosceles: exactly two sides equal
5. Scalene: all sides different
6. Right triangles: Right Isosceles or Right Scalene (a² + b² = c² within a tolerance)

Boundaries:
1. Side exactly 0 (invalid) vs. just above 0
2. Degenerate case: two sides sum exactly to the third, such as (1, 2, 3), which is invalid
3. Non-integer right triangles such as (1, 1, √2), where float rounding means == fails and a tolerance is needed
