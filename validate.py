"""Validates data send to the server.
"""


def validate_new_patient(new_patient_data):
    """Ensures new patient dictionary has correct fields and types.

    :param new_patient_data: Python object of received JSON
    :returns: validated Python dictionary or None
    """
    npdata = new_patient_data
    if type(npdata) is not dict:
        raise TypeError
    if "patient_id" not in npdata:
        raise TypeError
    if type(npdata["patient_id"]) is not str:
        raise ValueError
    if "attending_email" not in npdata:
        raise TypeError
    if type(npdata["attending_email"]) is not str:
        raise ValueError
    if "user_age" not in npdata:
        raise TypeError
    age = npdata["user_age"]
    if type(age) is not int and type(age) is not float:
        raise ValueError
    if age < 0:
        raise ValueError
    return npdata
