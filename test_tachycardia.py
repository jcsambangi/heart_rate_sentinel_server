"""Tests functions in module tachycardia.py
"""

import pytest

testData = [
        0, 10, "Cannot evaluate at this age.",
        15, 101, "No.",
        10, 145, "Yes.",
        2/12, 182, "Yes.",
        30, 150, "Yes.",
        50, 86, "No.",
]


@pytest.mark.parametrize("age, HR, result", testData)
def test_tachycardia(age, HR, result)
    from tachycardia import is_tachycardic
    assert is_tachycardic(age, HR) == result
