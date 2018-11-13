"""Functions called by server's handlers.
"""

from datetime import datetime


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


def add_heart_rate(new_HR, patientRecord):
    """Adds new HR measurement and timestamp to appropriate patient record.

    :param newHR: Python object of received JSON
    :param patientRecord: dictionary of all records to date
    :returns: updated dictionary of all records
    """
    from validate import validate_new_HR
    newHR = validate_new_HR(new_HR)
    if newHR is not None and newHR["patient_id"] in patientRecord:
        patientRecord[newHR["patient_id"]][2][0].append(newHR["heart_rate"])
        patientRecord[newHR["patient_id"]][2][1].append(datetime.now())
    return patientRecord


def get_heart_rates(patient_id, patientRecord):
    """Gets all HRs associated with requested patient id.

    :param patient_id: patient id as string
    :param patientRecord: dictionary of all records to date
    :returns: dictionary of all HRs associated with requested patient
    """
    return farmHR


def get_status(patient_id, patientRecord):
    """Determines whether patient is tachycardic and returns latest timestamp.

    :param patient_id: patient id as string
    :param patientRecord: dictionary of all records to date
    :returns: dictionary of status and latest timestamp
    """
    return status


def get_average(patient_id, patientRecord):
    """Calculates average HR over all stored HRs.

    :param patient_id: patient id as string
    :param patientRecord: dictionary of all records to date
    :returns: dictionary of average HR
    """
    return average_HR


def get_interval_average(query_interval_average, patientRecord):
    """Calculates average HR since specified time.

    :param query_interval_average: Python object of received JSON
    :param patientRecord: dictionary of all records to date
    :returns: dictionary of average HR over interval
    """
    """Bad input?"""
    from validate import validate_query_interval_average
    interval = validate_query_interval_average(query_interval_average)
    if interval is not None and interval["patient_id"] in patientRecord:
        patientID = interval["patient_id"]
        startTime = interval["heart_rate_average_since"]
        allHRdata = patientRecord[patientID][2]
        index = 0
        while allHRdata[1][index] <= timestamp
            index += 1
        summation = 0
        numSum = len(allHRdata[1]-index)
        for i in range(index, numSum):
            summation += allHRdata[0][i]
        interval_average_HR = round(summation/numSum)
    return interval_average_HR
