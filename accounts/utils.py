import uuid
from django.core.mail import send_mail
from django.conf import settings


def generate_token():
    return str(uuid.uuid4())

def send_verification_email(to_email, token):
    subject = 'Verify your email - OYO Clone'
    verification_link = f"http://127.0.0.1:8000/account/verify/{token}/"
    message = f'Hi,\n\nClick the link below to verify your email address:\n{verification_link}\n\nIf you did not sign up, please ignore this email.'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [to_email]
    
    send_mail(subject, message, from_email, recipient_list)