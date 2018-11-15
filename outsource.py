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
    if newHR["patient_id"] in patientRecord:
        patientRecord[newHR["patient_id"]][2][0].append(newHR["heart_rate"])
        patientRecord[newHR["patient_id"]][2][1].append(datetime.now())
        return patientRecord
    else:
        raise ValueError


def get_heart_rates(patient_id, patientRecord):
    """Gets all HRs associated with requested patient id.

    :param patient_id: patient id as string
    :param patientRecord: dictionary of all records to date
    :returns: dictionary of all HRs associated with requested patient
    """
    if patient_id in patientRecord:
        farmHR = patientRecord[patient_id][2][0]
        return farmHR
    else:
        raise ValueError


def get_status(patient_id, patientRecord):
    """Determines whether patient is tachycardic and returns latest timestamp.

    :param patient_id: patient id as string
    :param patientRecord: dictionary of all records to date
    :returns: dictionary of status and latest timestamp
    """
    if patient_id in patientRecord:
        from tachycardia import is_tachycardic
        allHRdata = patientRecord[patient_id][2]
        HRs = allHRdata[0]
        yesOrNo = is_tachycardic(patientRecord[patient_id][1], HRs.reverse()[0])
        timestamps = allHRdata[1]
        latest = timestamps.reverse()[0]
        return {"Is {} tachycardic?".format(patient_id): yesOrNo,
                "Time of latest heart rate measurement": latest}
    else:
        raise ValueError


def get_average(patient_id, patientRecord):
    """Calculates average HR over all stored HRs.

    :param patient_id: patient id as string
    :param patientRecord: dictionary of all records to date
    :returns: integer average HR
    """
    if patient_id in patientRecord:
        HRs = patientRecord[patient_id][2][0]
        summation = 0
        for x in HRs:
            summation += x
        average_HR = round(summation/len(HRs))
        return average_HR
    else: 
        raise ValueError


def get_interval_average(query_interval_average, patientRecord):
    """Calculates average HR since specified time.

    :param query_interval_average: Python object of received JSON
    :param patientRecord: dictionary of all records to date
    :returns: integer average HR over interval
    """
    from validate import validate_query_interval_average
    interval = validate_query_interval_average(query_interval_average)
    if interval["patient_id"] in patientRecord:
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
    else:
        raise ValueError
