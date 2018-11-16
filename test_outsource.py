"""Unit tests for outsource.py module
"""

import pytest
from datetime import datetime, timedelta

new_patient_data = {
        "patient_id": "1",
        "attending_email": "suyash.kumar@duke.edu",
        "user_age": 50
}
patientRecord = {
        "2": ["suyash.kumar@duke.edu", 50, [[100], [datetime(2018, 10, 14)]]],
        "tester": ["jaydeep.sambangi@duke.edu", 22,
                   [[60, 75, 110],
                    [datetime(2018, 1, 5), datetime(2018, 10, 15),
                     datetime(2018, 11, 14)]]]
}
patientRecord2 = {
        "2": ["suyash.kumar@duke.edu", 50, [[100], [datetime(2018, 10, 14)]]],
        "tester": ["jaydeep.sambangi@duke.edu", 22,
                   [[60, 75, 110],
                    [datetime(2018, 1, 5), datetime(2018, 10, 15),
                     datetime(2018, 11, 14)]]]
}
checkUpdatedPatientRecord = {
        "1": ["suyash.kumar@duke.edu", 50, [[], []]],
        "2": ["suyash.kumar@duke.edu", 50, [[100], [datetime(2018, 10, 14)]]],
        "tester": ["jaydeep.sambangi@duke.edu", 22,
                   [[60, 75, 110],
                    [datetime(2018, 1, 5), datetime(2018, 10, 15),
                     datetime(2018, 11, 14)]]]
}
goodHRdata = {
    "patient_id": "2",
    "heart_rate": 101
}
checkHRPatientRecord = {
        "2": ["suyash.kumar@duke.edu", 50, [[100, 101],
              [datetime(2018, 10, 14), datetime.now()]]],
        "tester": ["jaydeep.sambangi@duke.edu", 22,
                   [[60, 75, 110],
                    [datetime(2018, 1, 5), datetime(2018, 10, 15),
                     datetime(2018, 11, 14)]]]
}
goodPatientID = "2"
goodIntervalAverageRequest = {
    "patient_id": "tester",
    "heart_rate_average_since": "2018-03-09 11:00:36.372339"
}
badIntervalAverageRequest = {
    "patient_id": "probably_not_here",
    "heart_rate_average_since": "2018-03-09 11:00:36.372339"
}
noDataAverageRequest = {
    "patient_id": "tester",
    "heart_rate_average_since": "2018-12-09 11:00:36.372339"
}
deadRequest = {
    "patient_id": "1",
    "heart_rate_average_since": "2018-12-09 11:00:36.372339"
}


def test_add_new_patient():
    from outsource import add_new_patient
    updatedPatientRecord = add_new_patient(new_patient_data, patientRecord)
    assert updatedPatientRecord == checkUpdatedPatientRecord


def test_add_heart_rate_good():
    from outsource import add_heart_rate
    newPatientRecord = add_heart_rate(goodHRdata, patientRecord2)
    dt = newPatientRecord["2"][2][1][1]-checkHRPatientRecord["2"][2][1][1]
    if dt < timedelta(hours=1):
        newPatientRecord["2"][2][1][1] = checkHRPatientRecord["2"][2][1][1]
    assert newPatientRecord == checkHRPatientRecord


def test_add_heart_rate_bad():
    from outsource import add_heart_rate
    with pytest.raises(ValueError):
        add_heart_rate({"patient_id": "probably_not_here", "heart_rate": 115},
                       patientRecord)


def test_get_heart_rates_good():
    from outsource import get_heart_rates
    assert get_heart_rates("tester", patientRecord) == [60, 75, 110]


def test_get_heart_rates_bad():
    from outsource import get_heart_rates
    with pytest.raises(ValueError):
        get_heart_rates("probably_not_here", patientRecord)


def test_get_status_good():
    from outsource import get_status
    status = get_status("tester", patientRecord)
    timeShouldBe = "2018-11-14 00:00:00.000000"
    assert status == {"Is tester tachycardic?": "Yes.",
                      "Time of latest heart rate measurement": timeShouldBe}


def test_get_status_bad():
    from outsource import get_status
    with pytest.raises(ValueError):
        get_status("probably_not_here", patientRecord)


def test_get_status_noData():
    from outsource import get_status
    with pytest.raises(ValueError):
        get_status("1", checkUpdatedPatientRecord)


def test_get_average_good():
    from outsource import get_average
    assert get_average("tester", patientRecord) == round((60+75+110)/3)


def test_get_average_bad():
    from outsource import get_average
    with pytest.raises(ValueError):
        get_average("probably_not_here", patientRecord)


def test_get_average_noData():
    from outsource import get_average
    with pytest.raises(ValueError):
        get_average("1", checkUpdatedPatientRecord)


def test_get_interval_average_good():
    from outsource import get_interval_average
    pAverage = get_interval_average(goodIntervalAverageRequest, patientRecord)
    assert pAverage == round((75+110)/2)


def test_get_interval_average_bad():
    from outsource import get_interval_average
    with pytest.raises(ValueError):
        get_interval_average(badIntervalAverageRequest, patientRecord)


def test_get_interval_average_no_set():
    from outsource import get_interval_average
    wantedAverage = get_interval_average(noDataAverageRequest, patientRecord)
    assert wantedAverage == "No heart rate measurements since this date."


def test_get_interval_average_noData():
    from outsource import get_interval_average
    with pytest.raises(ValueError):
        get_interval_average(deadRequest, checkUpdatedPatientRecord)
