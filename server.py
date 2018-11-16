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
    global patientRecord
    new_patient_data = request.get_json()
    from outsource import add_new_patient
    try:
        patientRecord = add_new_patient(new_patient_data, patientRecord)
        return jsonify(patientRecord), 200
    except TypeError:
        return jsonify("Please check that all fields were input."), 400
    except ValueError:
        return jsonify("Please check that input data is correct."), 400
    except:
        return jsonify("Something went wrong."), 501


@app.route("/api/heart_rate", methods=["POST"])
def heart_rate_post():
    """POSTs patient's new heart rate with timestamp.
    Checks for tachycardia and emails physician if tachycardic.

    :param patient_id: patient id as string
    :param heart_rate: heart rate as integer
    :returns: updated records as JSON
    """
    global patientRecord
    new_HR = request.get_json()
    from outsource import add_heart_rate
    try:
        patientRecord = add_heart_rate(new_HR, patientRecord)
        return jsonify(patientRecord), 200
    except TypeError:
        return jsonify("Please check that all fields were input."), 400
    except ValueError:
        return jsonify("Please check that input data is correct."), 400
    except:
        return jsonify("Something went wrong."), 501


@app.route("/api/heart_rate/<patient_id>", methods=["GET"])
def heart_rate_get(patient_id):
    """GETs all HRs for patient.

    :param patient_id: patient id as string
    :returns: list of HRs as JSON
    """
    global patientRecord
    from outsource import get_heart_rates
    try:
        return jsonify(get_heart_rates(patient_id, patientRecord)), 200
    except TypeError:
        return jsonify("Please check that patient id is a string."), 400
    except ValueError:
        return jsonify("Please initialize the patient first."), 400
    except:
        return jsonify("Something went wrong."), 501


@app.route("/api/status/<patient_id>", methods=["GET"])
def status(patient_id):
    """GETs whether patient is tachycardic and returns timestamp using last HR.

    :param patient_id: patient id as string
    :returns: whether patient is tachycardic and last timestamp
    """
    global patientRecord
    from outsource import get_status
    try:
        return jsonify(get_status(patient_id, patientRecord)), 200
    except TypeError:
        return jsonify("Please check that patient id is a string."), 400
    except ValueError:
        return jsonify("The patient must be initialized and have data."), 400
    except:
        return jsonify("Something went wrong."), 501


@app.route("/api/heart_rate/average/<patient_id>", methods=["GET"])
def average(patient_id):
    """GETs average HR over all stored HRs.

    :param patient_id: patient id as string
    :returns: average HR as JSON
    """
    global patientRecord
    from outsource import get_average
    try:
        return jsonify(get_average(patient_id, patientRecord)), 200
    except TypeError:
        return jsonify("Please check that patient id is a string."), 400
    except ValueError:
        return jsonify("The patient must be initialized and have data."), 400
    except:
        return jsonify("Something went wrong."), 501


@app.route("/api/heart_rate/interval_average", methods=["POST"])
def interval_average():
    """POSTs timestamp from which average HR calculation should begin.

    :param patient_id: patient id as string
    :param heart_rate_average_since: timestamp as string
    :returns: average HR over interval as JSON
    """
    global patientRecord
    query_interval_average = request.get_json()
    from outsource import get_interval_average
    try:
        interval_average = get_interval_average(query_interval_average,
                                                patientRecord)
        return jsonify(interval_average), 200
    except TypeError:
        return jsonify("Please check that all fields were input."), 400
    except ValueError:
        return jsonify("Please check input and that patient has data."), 400
    except:
        return jsonify("Something went wrong."), 501


if __name__ == "__main__":
    app.run(host="0.0.0.0")
