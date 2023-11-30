import threading

import requests
import json

msg91_email_url = ""


def send_email_to_msg91(self):
    payload_data = ""
    mail_response = requests.post(msg91_email_url, data=json.dumps(payload_data), headers=email_api_msg91_headers)
    print(self.to)
    return True


def send_email(to_email, subject, message):
    mail_api = "Not Defined"
    headers = {
        "user-agent": "Application",
        "Accept": "*/*",
        "Content-Type": "application/json; charset=utf-8",
    }

    mail_data = {"toEmail": to_email, "toCc": "", "subject": subject, "msg": message}

    response = requests.post(url=mail_api, headers=headers, json=mail_data)
    print(
        "Email to {} sent successfully with subject {} and message {} and response {}".format(
            to_email, subject, message, response.text
        )
    )


email_api_msg91_headers = {
    "Content-Type": "application/JSON",
    "Accept": "application/json",
    "authkey": "",
}
