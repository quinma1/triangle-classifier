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
There has been AI use in this project Claude helped explain the assigment better, Copilot suggested most of the code and if there was any problems i corrected them. 
How to Run the Tests
1. Install dependencies: `python -m pip install -r requirements.txt`
2. Run all tests: `python -m pytest -v`

Equivalence classes are groups of inputs the code treats the same way. Any one example from a group should behave like all the others. That’s the list of six.
Boundaries are the edges between groups where bugs usually hide side exactly 0 the degenerate 1 + 2 = 3 case and float rounding on right triangles.