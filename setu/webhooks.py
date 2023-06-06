import json

from rest_framework.decorators import api_view
from rest_framework.response import  Response
from setu.constants import ConsentStatus, SessionStatus
from setu.handles.data_session_handler import DataSessionHandler
from setu.models import Consent, Sessions
from rest_framework import status



@api_view(["POST"])
def notification_handler(request):
    payload = request.data
    notification_type = payload.get("type")
    if notification_type == "CONSENT_STATUS_UPDATE":
        return consent_notification(payload)
    elif notification_type == "SESSION_STATUS_UPDATE":
        return session_notification(payload)
    return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": "Invalid Type"})


def consent_notification(payload):
    consent_id = payload.get("consentId")
    success = payload.get("success", False)
    data = payload.get("data")
    if success == True and data != None:
        consent = Consent.objects.get(consent_id=consent_id)
        consent.status = data.get("status")
        consent.save()

        # TODO: Async Await
        DataSessionHandler().create_session_api(consent_id)

    return Response(status=status.HTTP_200_OK)


def session_notification(payload):
    session_id = payload.get("id")
    consent_id = payload.get("consentId")
    status = payload.get("status")
    data = payload.get("Payload")

    if SessionStatus.COMPLETED.name == status and data != None:
        data_session = Sessions.objects.get(sessions_id=session_id)
        data_session.status = status
        data_session.data = json.dumps(data)
        data_session.save()

    return Response(status=status.HTTP_200_OK)
