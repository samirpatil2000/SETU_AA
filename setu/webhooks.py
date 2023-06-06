import json

from rest_framework.decorators import api_view
from rest_framework.response import  Response
from setu.constants import ConsentStatus, SessionStatus
from setu.models import Consent, Sessions
from rest_framework import status

@api_view(["POST"])
def consent_notification(request):
    payload = request.data
    consent_id = payload.get("consentId")
    success = payload.get("success", False)
    data = payload.get("data")
    if success == True and data != None:
        consent = Consent.objects.get(consent_id=consent_id)
        consent.status = data.get("status")
        consent.save()
    return Response(status=status.HTTP_200_OK)


@api_view(["POST"])
def session_notification(request):
    payload = request.data
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
