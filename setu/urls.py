from django.urls import path
from .views import *
from .webhooks import *
urlpatterns = [

    path('consent', create_consent_view),
    path('consent/<str:consent_id>', create_consent_view),
    path('datasession', create_data_session_view),
    # path('datasession/<str:data_session_id>', DataSessionView.as_view()),
    # path('data', SampleDataView.as_view()),

    # webhooks
    path('webhook/consents/response', consent_notification),
    path('webhook/sessions/response', session_notification)

 ]