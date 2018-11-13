"""Unit tests for validate.py module.
"""

import pytest

testData = [
        1,
        {"attending_email": "suyash.kumar@duke.edu", "user_age": 50},
        {"patient_id": 1, "attending_email": "suyash.kumar@duke.edu",
            "user_age": 50},
        {"patient_id": "1", "user_age": 50},
        {"patient_id": "1", "attending_email": 3, "user_age": 50},
        {"patient_id": "1", "attending_email": "suyash.kumar@duke.edu"},
        {"patient_id": "1", "attending_email": "suyash.kuamr@duke.edu",
            "user_age": "50"}
]


@pytest.mark.parametrize("new_patient_data", testData)
def test_validate_new_patient_bad(new_patient_data):
    from validate import validate_new_patient
    assert validate_new_patient(new_patient_data) is None
