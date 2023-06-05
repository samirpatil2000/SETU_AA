from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class UserView(APIView):

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            result = {'status': status.HTTP_403_FORBIDDEN, "message": "Not Authenticated!", "data": {}}
            return Response(result)
        user = request.user
        user_info = {
            "email": user.email,
            "followers": user.total_followers(),
            "following": user.total_following(),
        }
        print(user_info)
        result = {'status': status.HTTP_200_OK, 'message': "", "data": user_info}
        return Response(result)