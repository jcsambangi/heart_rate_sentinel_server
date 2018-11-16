# heart_rate_sentinel_server
BME 590.06: Heart Rate Sentinel Server Assignment
v1.0.0 released 11/16/18 by Jaydeep Sambangi (GitHub: jcsambangi, NetID: js593)

## Overview
This software is a server built to store and lightly analyze heart rate data for patients in a clinical setting. It can additionally utilize the Sendgrid API to send an email to an attending physician if their patient is thought to be tachycardic. These calculations are age-sensitive and based on this simple [reference](https://en.wikipedia.org/wiki/Tachycardia). The server was deployed on the day of release on a Duke virtual machine using Flask. Specifics of the HTTP requests that can be made to the server can be found in the [functional specifications](https://github.com/mlp6/Medical-Software-Design/blob/master/Lectures/databases/sentinel-server-assignment.md); a brief summary of the API routes this Flask web service accommodates are below:
  + `POST /api/new_patient`
  + `POST /api/heart_rate`
  + `POST /api/heart_rate/interval_average`
  + `GET /api/status/<patient_id>`
  + `GET /api/heart_rate/<patient_id>`
  + `GET /api/heart_rate/average/<patient_id>`

## Using the Server
The server should be deployed and can be accessed at the following address and port:
  + `http://vcm-7315.vm.duke.edu:5000/`
