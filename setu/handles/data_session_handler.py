import json
import requests

from setu.constants import SETU_API_ENDPOINT, SETU_API_HEADERS
from setu.models import Sessions, Consent


class DataSessionHandler:
    DATA_SESSION_API_ENDPOINT = "sessions"

    def create_session_api(self, consentId):
        url = SETU_API_ENDPOINT + self.DATA_SESSION_API_ENDPOINT

        payload = json.dumps({
            "consentId": consentId,
            "DataRange": {
                "from": "2021-04-01T00:00:00Z",
                "to": "2021-09-30T00:00:00Z"
            },
            "format": "json"
        })

        response = requests.request("POST", url, headers=SETU_API_HEADERS, data=payload)
        data = json.loads(response.text)
        if response.status_code == 201:
            self.create_session(data)
            return {"status": 1, "data": {}}
        return {"status": 0, "error": {"error_code":data.get("errorCode"), "error_message": data.get("errorMsg")}}

    def create_session(self, data):
        consent_object = Consent.objects.get(consent_id=data["consentId"])
        return Sessions.objects.create(
            sessions_id=data["id"],
            consent_id=consent_object.id,
            status=data["status"]
        )