
from django.urls import path
from . import views
urlpatterns = [
    path('',views.Index, name='index'),
    path('sign-up',views.Sign_Up, name='sign_up'),
    path('sign-in',views.Sign_In, name='sign_in'),
    path('forgot-password',views.Forgot_Password, name='forgot_password'),
]