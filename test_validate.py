"""Unit tests for validate.py module.
"""

import pytest
from datetime import datetime

badNewData = [
        1,
        {"attending_email": "suyash.kumar@duke.edu", "user_age": 50},
        {"patient_id": 1, "attending_email": "suyash.kumar@duke.edu",
            "user_age": 50},
        {"patient_id": "1", "user_age": 50},
        {"patient_id": "1", "attending_email": 3, "user_age": 50},
        {"patient_id": "1", "attending_email": "suyash.kumar@duke.edu"},
        {"patient_id": "1", "attending_email": "suyash.kuamr@duke.edu",
            "user_age": "50"},
        {"patient_id": "1", "attending_email": "suyash.kuamr@duke.edu",
            "user_age": -1},
]
goodNewData = {
    "patient_id": "1",
    "attending_email": "suyash.kumar@duke.edu", 
    "user_age": 50
}
badHRData = [
        "hello",
        {"heart_rate": 100},
        {"patient_id": 100, "heart_rate": 100},
        {"patient_id": "test"},
        {"patient_id": "test", "heart_rate": "hello"},
        {"patient_id": "test", "heart_rate": -5},
]
goodHRData = {
    "patient_id": "1",
    "heart_rate": 100
}
badIntervalData = [
        "really bad",
        {"heart_rate_average_since": "2018-03-09 11:00:36.372339"},
        {"patient_id": 1,
         "heart_rate_average_since": "2018-03-09 11:00:36.372339"},
        {"patient_id": "1"},
        {"patient_id": 1, "heart_rate_average_since": 2018},
        {"patient_id": 1, "heart_rate_average_since": "2018-03-09"},
]
goodInterval = {
    "patient_id": "1",
    "heart_rate_average_since": "2018-03-09 11:00:36.372339"
}


@pytest.mark.parametrize("new_patient_data", badNewData)
def test_validate_new_patient_bad(new_patient_data):
    from validate import validate_new_patient
    with pytest.raises((TypeError, ValueError)):
        validate_new_patient(new_patient_data)


def test_validate_new_patient_good():
    from validate import validate_new_patient
    assert validate_new_patient(goodNewData) == goodNewData


@pytest.mark.parametrize("new_HR_data", badHRData)
def test_validate_new_HR_bad(new_HR_data):
    from validate import validate_new_HR
    with pytest.raises((TypeError, ValueError)):
        validate_new_HR(new_HR_data)


def test_validate_new_HR_good():
    from validate import validate_new_HR
    assert validate_new_HR(goodHRData) == goodHRData


def test_check_patient_id_bad():
    from validate import check_patient_id
    with pytest.raises(TypeError):
        check_patient_id(345)


def test_check_patient_id_good():
    from validate import check_patient_id
    assert check_patient_id("Example") == "Example"


@pytest.mark.parametrize("bad_interval_data", badIntervalData)
def test_validate_query_interval_average_bad(bad_interval_data):
    from validate import validate_query_interval_average
    with pytest.raises((TypeError, ValueError)):
        validate_query_interval_average(bad_interval_data)


def test_validate_query_interval_good():
    dateObj = datetime(2018, 3, 9, 11, 0, 36, 372339)
    preppedInterval = goodInterval.copy()
    preppedInterval["heart_rate_average_since"] = dateObj
    from validate import validate_query_interval_average
    assert validate_query_interval_average(goodInterval) == preppedInterval
