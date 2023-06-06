from django.urls import path
from .views import *
from .webhooks import *


urlpatterns = [

    # this is responsible for create consent
    path('api/consent-handshake', create_consent_view),

    # this is responsible for fetching the session data
    path('api/sessions/<str:consent_id>', get_session_data),

    # webhooks
    path('webhooks', notification_handler)

 ]