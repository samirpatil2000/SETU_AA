from rest_framework.decorators import api_view
from rest_framework.response import Response

from setu.handles.consent_handler import ConsentHandler
from setu.models import Sessions


@api_view(['POST'])
def create_consent_view(request):
    payload = request.data
    create_consent_response = ConsentHandler().create_consent_api(phone_number=payload.get("phone_number", "9730614299"))

    if create_consent_response.get("status") == 1:
        # Create data sessions
        data = create_consent_response.get("data")
        return Response({"message": "Consent Created Successfully", "data": data})
    # TODO: Status Codes, proper error messages
    return Response({"message": "something went wrong"})


@api_view(['GET'])
def get_session_data(request, consent_id):
    session_objects = Sessions.objects.all(consent_id=consent_id)
    if session_objects.exists():
        session_object = session_objects[0]
        return Response({"data": session_object.get("data")})
    return Response({"message": "something went wrong"})


