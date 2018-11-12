"""Module that runs the server.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/api/new_patient", methods=["POST"])
def new_patient():
    """POSTs new patient. Expects JSON dictionary with following string keys.

    :param patient_id: patient id as string
    :param attending_email: attending physician's email as string
    :param user_age: patient's age in years as integer
    """


@app.route("/api/heart_rate/<patient_id>", methods=["GET", "POST"])
def heart_rate(patient_id):
    """GETs all HRs or POSTs new heart rate with timestamp.
    Checks for tachycardia and emails physician if tachycardic.

    :param patient_id: patient id as string
    :param heart_rate: only if POSTing - heart rate as integer
    """


@app.route("/api/status/<patient_id>", methods=["GET"])
def status(patient_id):
    """GETs whether patient is tachycardic and returns timestamp using last HR.

    :param patient_id: patient id as string
    """


@app.route("/api/heart_rate/average/<patient_id>", methods=["GET"])
def average(patient_id):
    """GETs average HR over all stored HRs.

    :param patient_id: patient id as string
    """


@app.route("/api/heart_rate/interval_average", methods=["POST"])
def interval_average():
    """POSTs timestamp from which average HR calculation should begin.

    :param patient_id: patient id as string
    :param heart_rate_average_since: timestamp as string
    """


if __name__ == "__main__":
    app.run(host = "0.0.0.0")
