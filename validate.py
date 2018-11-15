"""Validates data send to the server.
"""


def validate_new_patient(new_patient_data):
    """Ensures new patient dictionary has correct fields and types.

    :param new_patient_data: Python object of received JSON
    :returns: validated Python dictionary
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


def validate_new_HR(new_HR):
    """Ensures new HR dictionary has correct fields and types.

    :param new_HR: Python object of received JSON
    :returns: validated Python dictionary
    """
    newHR = new_HR
    if type(newHR) is not dict:
        raise TypeError
    if "patient_id" not in newHR:
        raise TypeError
    if type(newHR["patient_id"]) is not str:
        raise ValueError
    if "heart_rate" not in newHR:
        raise TypeError
    HR = newHR["heart_rate"]
    if type(HR) is not int and type(HR) is not float:
        raise ValueError
    if HR < 0:
        raise ValueError
    return newHR


def check_patient_id(patient_id):
    """Ensures patient id is of appropriate form.

    :param patient_id: Python variable from GET request
    :returns: validated patient id as string
    """
    if type(patient_id) is not str:
        raise TypeError
    return patient_id


def validate_query_interval_average(query_interval_average):
    """Ensures query for interval average dictionary is correctly formatted.

    :param query_interval_average: Python object of received JSON
    :returns: validated Python dictionary
    """
    interval = query_interval_average
    if type(interval) is not dict:
        raise TypeError
    if "patient_id" not in interval:
        raise TypeError
    if type(interval["patient_id"]) is not str:
        raise ValueError
    if "heart_rate_average_since" not in interval:
        raise TyperError
