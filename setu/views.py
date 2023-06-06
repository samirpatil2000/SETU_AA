from rest_framework import mixins
from rest_framework import generics
from django.views import View
from django.http import JsonResponse


from rest_framework.decorators import api_view
from rest_framework.response import Response

from setu.constants import ConsentStatus
from setu.handles.consent_handler import ConsentHandler
from setu.handles.data_session_handler import DataSessionHandler
from setu.models import Consent


@api_view(['POST'])
def create_consent_view(request):
    if request.method == "GET":
        return Response({"message": "Got some data!"})
    if request.method == 'POST':
        payload = request.data
        create_consent_response = ConsentHandler().create_consent_api(phone_number="9730614299")

        if create_consent_response.get("status") == 1:
            # Create data sessions
            data = create_consent_response.get("data")
            consent_id = data.get("id")
            create_data_session_view(consent_id)
            return Response({"message": "Consent Created Successfully", "data": data})
        # TODO: Status Codes, proper error messages
        return Response({"message": "something went wrong"})


def create_data_session_view(consent_id):
    consent_object = Consent.objects.get(consent_id)
    if consent_object.status == ConsentStatus.ACTIVE.name:
        create_data_session_response = DataSessionHandler().create_session_api(consent_id)
        if create_data_session_response.get("status") == 1:
            return Response({"message": "Data Session Created Successfully", "data": create_data_session_response.get("data")})
        # TODO: Status Codes, proper error messages
        return Response({"message": create_data_session_response["error"].get("error_message")})
    return Response({"message": "Consent Not Approved Yet"})



