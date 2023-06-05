from rest_framework.decorators import api_view
from rest_framework.response import  Response
from setu.constants import ConsentStatus
from setu.models import Consent
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
