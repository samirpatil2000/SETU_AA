from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import Account
from account.serializers.register_serializer import AccountSerializer


class RegistrationAPIView(APIView):

    def get_object(self, user):
        try:
            return Account.objects.get(email=user)
        except Account.DoesNotExist:
            raise Http404

    def get(self, request):
        try:
            if not request.user.is_authenticated:
                result = {'status': status.HTTP_403_FORBIDDEN, "message": "Not Authenticated!", "data": {}}
                return Response(result)
            account = self.get_object(request.user)
            serializers = AccountSerializer(account)
            result = {'status': status.HTTP_200_OK, "message": "successfully register", "data": serializers.data}
        except Exception as e:
            result = {'status': status.HTTP_400_BAD_REQUEST, "message": str(e), "data":{}}
        return Response(result)

    def is_exists(self, email=None):

        if email and Account.objects.filter(email=email).exists():
            message = "Email already exists"
            return True, message

        return False, None