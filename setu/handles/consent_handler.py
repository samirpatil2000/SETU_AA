import json
from typing import final
import requests
import pdb

from setu.constants import SETU_API_ENDPOINT, SETU_API_HEADERS
from setu.models import Consent, User
import logging
from datetime import datetime


logger = logging.getLogger(__name__)



class ConsentHandler:

    CONSENT_API_END_POINT: final(str) = "consents"

    def create_consent_api(self, phone_number):
        url = SETU_API_ENDPOINT + self.CONSENT_API_END_POINT
        current_datetime = datetime.now().isoformat()
        payload = json.dumps({
            "Detail": {
                "consentStart": str(current_datetime[:-3]) + "Z",
                "consentExpiry": "2023-06-23T05:44:53.822Z",
                "Customer": {
                    "id": phone_number + "@onemoney"
                },
                "FIDataRange": {
                    "from": "2023-04-01T00:00:00Z",
                    "to": "2023-04-08T00:00:00Z"
                },
                "consentMode": "STORE",
                "consentTypes": [
                    "TRANSACTIONS",
                    "PROFILE",
                    "SUMMARY"
                ],
                "fetchType": "PERIODIC",
                "Frequency": {
                    "value": 30,
                    "unit": "MONTH"
                },
                "DataFilter": [
                    {
                        "type": "TRANSACTIONAMOUNT",
                        "value": "5000",
                        "operator": ">="
                    }
                ],
                "DataLife": {
                    "value": 1,
                    "unit": "MONTH"
                },
                "DataConsumer": {
                    "id": "setu-fiu-id"
                },
                "Purpose": {
                    "Category": {
                        "type": "string"
                    },
                    "code": "101",
                    "text": "Loan underwriting",
                    "refUri": "https://api.rebit.org.in/aa/purpose/101.xml"
                },
                "fiTypes": [
                    "DEPOSIT"
                ]
            },
            "context": [
                {
                    "key": "accounttype",
                    "value": "SAVINGS"
                }
            ],
            "redirectUrl": "https://setu.co"
        })

        logger.info("create_session_api: request consent create api request => {}".format(payload))
        response = requests.request("POST", url, headers=SETU_API_HEADERS, data=payload)
        logger.info("create_session_api: request consent create api request => {}".format(payload))

        print(response.text)
        if response.status_code == 201:
            data = json.loads(response.text)
            self._create_consent(data, phone_number)
            return {"status": 1, "data" : {"redirect_url": data.get("url"), "id": data.get("id")}}
        return {"status": 0}

    def _create_consent(self, data, phone_number):
        obj, created = User.objects.get_or_create(phone_number=phone_number)
        return Consent.objects.create(
            consent_id=data.get("id"),
            redirect_url=data.get("url"),
            status=data.get("status"),
            user_id=obj.id
        )
