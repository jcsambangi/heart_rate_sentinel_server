"""Validates data send to the server.
"""


def validate_new_patient(new_patient_data):
    """Ensures new patient dictionary has correct fields and types.

    :param new_patient_data: Python object of received JSON
    :returns: validated Python dictionary or None
    """
    npdata = new_patient_data
    if type(npdata) is not dict:
        return None
    if "patient_id" not in npdata:
        return None
    if type(npdata["patient_id"]) is not str:
        return None
    if "attending_email" not in npdata:
        return None
    if type(npdata["attending_email"]) is not str:
        return None
    if "user_age" not in npdata:
        return None
    if type(npdata["user_age"]) is not int:
        return None
    return npdata
