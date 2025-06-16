from django.shortcuts import render

# Create your views here.
def Index(request):
    return render(request, 'user/index.html')

def Sign_Up(request):
    return render(request, 'user/sign_up.html',{'hide_layout': True,})
    

def Otp_Validation(request):
    return render(request, 'user/otp_validation.html',{'hide_layout': True,})

def Sign_In(request):
    return render(request, 'user/sign_in.html',{'hide_layout': True,})

def Forgot_Password(request):
    return render(request, 'user/forgot_password.html',{'hide_layout': True,})  


def Email_Otp_Varification(request):
    return render(request,'user/email_otp_varification.html',{'hide_layout': True,})

def Reset_Password(request):
    return render(request, 'user/reset_password.html',{'hide_layout': True,})