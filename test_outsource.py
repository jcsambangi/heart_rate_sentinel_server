"""Unit tests for outsource.py module
"""

new_patient_data = {
        "patient_id": "1",
        "attending_email": "suyash.kumar@duke.edu",
        "user_age": 50
}
patientRecord = {
        "2": ["suyash.kumar@duke.edu", 50, [[], []]]
}
checkUpdatedPatientRecord = {
        "1": ["suyash.kumar@duke.edu", 50, [[], []]],
        "2": ["suyash.kumar@duke.edu", 50, [[], []]]
}


def test_add_new_patient():
    from outsource import add_new_patient
    updatedPatientRecord = add_new_patient(new_patient_data, patientRecord)
    assert updatedPatientRecord == checkUpdatedPatientRecord
