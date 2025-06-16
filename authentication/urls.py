
from django.urls import path
from . import views
urlpatterns = [
    path('',views.Index, name='index'),
    path('sign-up',views.Sign_Up, name='sign_up'),
    path('otp-validation',views.Otp_Validation, name='otp_validation'),
    path('sign-in',views.Sign_In, name='sign_in'),
    path('sign-in/forgot-password',views.Forgot_Password, name='forgot_password'),
    path('sign-in/emil-otp-veification',views.Email_Otp_Varification, name='email_otp_verification'),
    path('sign-in/reset-password', views.Reset_Password, name='reset_password')
]
