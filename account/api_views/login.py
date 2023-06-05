from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView


class LoginAPIView(TokenObtainPairView):

    def post(self, request, *args, **kwargs):
        try:
            token = super(TokenObtainPairView, self).post(request, *args, **kwargs)
            data = {
                "token": token.data["access"]
            }
            result = {'status': status.HTTP_200_OK, 'message': "successfully login", 'data': data}
        except Exception as e:
            result = {'status': status.HTTP_400_BAD_REQUEST, 'message': str(e)}
        return Response(result)
