from django.shortcuts import render
from .models import HotelUser
from django.shortcuts import render, redirect
from django.contrib import messages
from .utils import generate_token,send_verification_email
from django.contrib.auth import authenticate, login

from django.contrib.auth.hashers import check_password


def login_page(request):
    if request.method == "POST":
        email = request.POST.get('email', '').strip().lower()
        password = request.POST.get('password', '')

        if not email or not password:
            messages.error(request, "Please enter both email and password.")
            return render(request, 'login.html')

        try:
            user = HotelUser.objects.get(email=email)
            if check_password(password, user.password):
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request, user)
                messages.success(request, "Login successful.")
                return redirect('/')
            else:
                messages.error(request, "Incorrect password.")
        except HotelUser.DoesNotExist:
            messages.error(request, "No account found with this email.")

    return render(request, 'login.html')  

def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')

        if HotelUser.objects.filter(email=email).exists():
            messages.error(request, "Email already in use.")
            return render(request, 'register.html')

        if HotelUser.objects.filter(phone_number=phone_number).exists():
            messages.error(request, "Phone number already in use.")
            return render(request, 'register.html')

        user = HotelUser.objects.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            username=email,
            phone_number=phone_number,
            email_token=generate_token()
        )
        user.set_password(password)
        user.save()
        send_verification_email(email,user.email_token)
        messages.success(request, "Account created successfully. Please log in.")
        return redirect('/account/register/') 

    return render(request, 'register.html')


def verify_email(request, token):
    try:
        user = HotelUser.objects.get(email_token=token)
        if user.is_verified:
            messages.info(request, "Email already verified. Please log in.")
        else:
            user.is_verified = True
            user.save()
            messages.success(request, "Email verified successfully.")
    except HotelUser.DoesNotExist:
        messages.error(request, "Invalid or expired verification link.")
    
    return redirect('/account/login/')
   