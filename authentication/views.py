from django.shortcuts import render

# Create your views here.
def Index(request):
    return render(request, 'user/index.html')


def Sign_Up(request):
    return render(request, 'user/sign_up.html')


def Sign_In(request):
    return render(request, 'user/sign_in.html')

def Forgot_Password(request):
    return render(request, 'user/forgot_password.html')
