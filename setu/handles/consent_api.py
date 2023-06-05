import json
from typing import final
import requests
import pdb

from setu.models import Consent

X_CLIENT_ID = "255d0b6c-492d-44cf-8581-e9494c7b0914"
X_CLIENT_SECRET = "9c2fc756-3d17-46d6-b28d-be4d71953e83"

headers = {
    'x-client-id': '255d0b6c-492d-44cf-8581-e9494c7b0914',
    'x-client-secret': '9c2fc756-3d17-46d6-b28d-be4d71953e83',
    'Content-Type': 'application/json'
}


SETU_API_END_POINT: final(str) = "https://fiu-uat.setu.co/"
CONSENT_API_END_POINT: final(str) = "consents"


class ConsentHandler:

    def create_consent_api(self, phone_number):
        url = SETU_API_END_POINT + CONSENT_API_END_POINT

        payload = json.dumps({
            "Detail": {
                "consentStart": "2023-06-05T18:17:14.882Z",
                "consentExpiry": "2023-06-23T05:44:53.822Z",
                "Customer": {
                    "id": phone_number + "@onemoney"
                },
                "FIDataRange": {
                    "from": "2021-06-04T00:00:00Z",
                    "to": "2021-06-10T00:00:00Z"
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
                    "value": "CURRENT"
                }
            ],
            "redirectUrl": "https://setu.co"
        })

        response = requests.request("POST", url, headers=headers, data=payload)
        if response.status_code == 201:
            data = json.loads(response.text)
            self.create_consent(data, phone_number)
            return {"status": 1, "data" : {"redirect_url": data.get("url"), "id": data.get("id")}}
        return {"status": 0}

    def create_consent(self, data, phone_number):
        return Consent.objects.create(
            consent_id=data.get("id"),
            redirect_url=data.get("url"),
            status=data.get("status"),
            phone_number=phone_number
        )
