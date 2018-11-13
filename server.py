"""Module that runs the server.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)
patientRecord = {}


@app.route("/api/new_patient", methods=["POST"])
def new_patient():
    """POSTs new patient. Expects JSON dictionary with following string keys.

    :param patient_id: patient id as string
    :param attending_email: attending physician's email as string
    :param user_age: patient's age in years as integer
    :returns: updated records as JSON
    """
    new_patient_data = request.get_json()
    from outsource import add_new_patient
    patientRecord = add_new_patient(new_patient_data, patientRecord)
    return jsonify(patientRecord)


@app.route("/api/heart_rate", methods=["POST"])
def heart_rate_post():
    """POSTs patient's new heart rate with timestamp.
    Checks for tachycardia and emails physician if tachycardic.

    :param patient_id: patient id as string
    :param heart_rate: heart rate as integer
    :returns: updated records as JSON
    """
    """EMAIL"""
    new_HR = request.get_json()
    from outsource import add_heart_rate
    patientRecord = add_heart_rate(new_HR, patientRecord)
    return jsonify(patientRecord)


@app.route("/api/heart_rate/<patient_id>", methods=["GET"])
def heart_rate_get(patient_id):
    """GETs all HRs for patient.

    :param patient_id: patient id as string
    :returns: list of HRs as JSON
    """
    from outsource import get_heart_rates
    return jsonify(get_heart_rates(patient_id, patientRecord))


@app.route("/api/status/<patient_id>", methods=["GET"])
def status(patient_id):
    """GETs whether patient is tachycardic and returns timestamp using last HR.

    :param patient_id: patient id as string
    :returns: whether patient is tachycardic and last timestamp
    """
    from outsource import get_status
    return jsonify(get_status(patient_id, patientRecord))


@app.route("/api/heart_rate/average/<patient_id>", methods=["GET"])
def average(patient_id):
    """GETs average HR over all stored HRs.

    :param patient_id: patient id as string
    :returns: average HR as JSON
    """
    from outsource import get_average
    return jsonify(get_average(patient_id, patientRecord))


@app.route("/api/heart_rate/interval_average", methods=["POST"])
def interval_average():
    """POSTs timestamp from which average HR calculation should begin.

    :param patient_id: patient id as string
    :param heart_rate_average_since: timestamp as string
    :returns: average HR over interval as JSON
    """
    query_interval_average = request.get_json()
    from outsource import get_interval_average
    return jsonify(get_interval_average(query_interval_average, patientRecord))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
