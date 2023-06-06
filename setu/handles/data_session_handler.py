import json
import requests

from setu.constants import SETU_API_ENDPOINT, SETU_API_HEADERS
from setu.models import Sessions, Consent

import logging

logger = logging.getLogger(__name__)

class DataSessionHandler:
    DATA_SESSION_API_ENDPOINT = "sessions"

    def create_session_api(self, consentId):
        url = SETU_API_ENDPOINT + self.DATA_SESSION_API_ENDPOINT

        payload = json.dumps({
            "consentId": consentId,
            "DataRange": {
                "from": "2023-06-06T00:00:00.000Z",
                "to": "2023-06-08T00:00:00.000Z"
            },
            "format": "json"
        })
        logger.info("create_session_api: request consent session api request => {}".format(payload))
        response = requests.request("POST", url, headers=SETU_API_HEADERS, data=payload)
        logger.info("create_session_api: response consent session api response => {}".format(response))
        data = json.loads(response.text)
        print(data)
        if response.status_code == 201:
            self._create_session(data)
            return {"status": 1, "data": {}}
        return {"status": 0, "error": {"error_code": data.get("errorCode"), "error_message": data.get("errorMsg")}}


    def fetch_data_session(self, session_id):
        url = SETU_API_ENDPOINT + self.DATA_SESSION_API_ENDPOINT + "/" + session_id


    def _create_session(self, data):
        consent_object = Consent.objects.get(consent_id=data["consentId"])
        return Sessions.objects.create(
            sessions_id=data["id"],
            consent_id=consent_object.id,
            status=data["status"]
        )