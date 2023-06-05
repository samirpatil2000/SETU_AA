from django.urls import path
from django import views
from . import views
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt import views as jwt_views
from account.api_views import RegistrationAPIView, LoginAPIView

urlpatterns = [

    path('token/refresh',
         jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('register', RegistrationAPIView.as_view()),
    path('login', LoginAPIView.as_view()),

    path('',views.index,name='home'),

    path('password-reset',
         auth_views.PasswordResetView.as_view(template_name='account/password_reset.html'),
         name='password_reset'),
    path('password-reset/done',
         auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html')
         , name='password_reset_confirm'),
    path('password-reset-complete',
         auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),
         name='password_reset_complete'),
    path('password_change/done',
         auth_views.PasswordChangeDoneView.as_view(template_name='account/password_change_done.html'),
         name='password_change_done'),
    path('password_change', auth_views.PasswordChangeView.as_view(template_name='account/password_change.html'),
         name='password_change'),

 ]