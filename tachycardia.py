"""Deals with tachycardic states.
"""

import sendgrid
import os
from sendgrid.helpers.mail import *

ages = [1/365, 3/365, 1/52, 1/12, 3/12, 6/12, 1, 3, 5, 8, 12, 15]
cutoffs = [159, 166, 182, 179, 186, 169, 151, 137, 133, 130, 119, 100]


def is_tachycardic(age, latestHR):
    """Determines whether status is tachycardic.

    :param age: age of patient
    :param latestHR: heart rate to use in determination, integer
    :returns: "Yes." or "No." for ages >= 1 day old
    """
    oldest = ages[len(ages)-1]
    if age == oldest:
        ind = ages.index(oldest)-1
    else:
        ind = ages.index(oldest)
        while age < ages[ind] and ind >= 0:
            ind -= 1
        if ind < 0:
            return "Cannot evaluate at this age."
    if latestHR > cutoffs[ind]:
        return "Yes."
    else:
        return "No."


def send_email(attending_email, patient_id):
    """Sends warning email if patient is tachycardic.

    :param attending_email: email destination
    :param patient_id: patient who is tachycardic
    :returns: status code associated with request
    """
    sg = sendgrid.SendGridAPIClient(apikey='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')
    to_email = Email(attending_email)
    from_email = Email("jcsambangi@gmail.com")
    subject = "Tachycardia Warning"
    body = "Warning: patient {} is currently tachycardic.".format(patient_id)
    content = Content("text/plain", body)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    return response.status_code
