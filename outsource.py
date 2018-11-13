"""Functions called by server's handlers.
"""


def add_new_patient(new_patient_data, patientRecord):
    """Initializes new patient.

    :param new_patient_data: Python object of received JSON
    :param patientRecord: dictionary of all records to date
    :returns: updated dictionary of all records
    """
    from validate import validate_new_patient
    npdata = validate_new_patient(new_patient_data)
    if npdata is not None:
        patientRecord[npdata["patient_id"]] = [npdata["attending_email"],
                                               npdata["user_age"], [[], []]]
    return patientRecord
