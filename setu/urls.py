from django.urls import path
from .views import *
from .webhooks import *
urlpatterns = [

    path('api/consent', create_consent_view),
    path('api/consent/<str:consent_id>', create_consent_view),
    path('api/session', create_data_session_view),

    # webhooks
    path('webhooks', set_notification_handler)

 ]