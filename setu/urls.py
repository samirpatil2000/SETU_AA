from django.urls import path
from .views import *

urlpatterns = [

    path('consent', create_custom_post),
    path('consent/<str:consent_id>', create_custom_post),
    path('datasession/<str:data_session_id>', DataSessionView.as_view()),
    path('data', SampleDataView.as_view()),

 ]