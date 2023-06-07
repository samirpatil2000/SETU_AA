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
            "DataRange":{
                "from": "2023-04-01T00:00:00Z",
                "to": "2023-04-08T00:00:00Z"
            },
            "format": "json"
        })
        logger.info("create_session_api: create consent session api request => {}".format(payload))
        response = requests.request("POST", url, headers=SETU_API_HEADERS, data=payload)
        logger.info("create_session_api: create consent session api response => {}".format(response))
        data = json.loads(response.text)
        print(data)
        if response.status_code == 201:
            self._create_session(data)
            return {"status": 1, "data": {}}
        return {"status": 0, "error": {"error_code": data.get("errorCode"), "error_message": data.get("errorMsg")}}

    def _create_session(self, data):
        consent_object = Consent.objects.get(consent_id=data["consentId"])
        return Sessions.objects.create(
            sessions_id=data["id"],
            consent_id=consent_object.id,
            status=data["status"]
        )

    def fetch_session_data(self, session_id):
        url = SETU_API_ENDPOINT + self.DATA_SESSION_API_ENDPOINT + "/" + session_id
        response = requests.request("GET", url, headers=SETU_API_HEADERS)
        data = json.loads(response.text)
        print(data)
        if response.status_code == 200:
            self._update_session(data, session_id)
            return {"status": 1, "data": {}}
        return {"status": 0, "error": {"error_code": data.get("errorCode"), "error_message": data.get("errorMsg")}}

    def _update_session(self, data, session_id):
        session_object = Sessions.objects.get(sessions_id=session_id)
        session_object.session_data = json.dumps(data.get("Payload")[0])
        session_object.save()
