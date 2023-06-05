from rest_framework import mixins
from rest_framework import generics
from django.views import View
from django.http import JsonResponse

import requests
import json

from rest_framework.decorators import api_view
from rest_framework.response import Response

from setu.handles.consent_api import ConsentHandler


class CustomView(mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):
    class AbstractClass:
        abstract = True


def hello_world(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})

@api_view(['GET', 'POST'])
def create_custom_post(request):
    if request.method == "GET":
        return Response({"message": "Got some data!"})
    if request.method == 'POST':
        consent_handler = ConsentHandler()
        create_consent_response = consent_handler.create_consent()
        if create_consent_response.get("status") == 1:
            return Response({"message": "Consent Created Successfully", "data": create_consent_response.get("data")})
        return Response({"message": "something went wrong"})




class DataSessionView(CustomView):
    def get(self, request):
        # Implement the logic to handle GET requests for data session
        # using the SETU Account Aggregator API
        # Return the response as a JSON
        return JsonResponse({'status': 'GET request for data session'})

    def post(self, request):
        # Implement the logic to handle POST requests for data session
        # using the SETU Account Aggregator API
        # Return the response as a JSON
        return JsonResponse({'status': 'POST request for data session'})


class SampleDataView(CustomView):
    def get(self, request):
        # Implement the logic to handle GET requests for sample data
        # using the SETU Account Aggregator API
        # Return the response as a JSON
        return JsonResponse({'status': 'GET request for sample data'})

    def post(self, request):
        # Implement the logic to handle POST requests for sample data
        # using the SETU Account Aggregator API
        # Return the response as a JSON
        return JsonResponse({'status': 'POST request for sample data'})
