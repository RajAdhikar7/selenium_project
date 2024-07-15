import os
from django.core.mail import EmailMessage
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_django_project.settings')
import django
django.setup()

def send_email():
    subject = 'Python (Selenium) Assignment - [Rameshwar Adhikar]'
    body = 'result of the assingment.'
    from_email = settings.EMAIL_HOST_USER
    to_email = ['tech@themedius.ai']
    cc_email = ['hr@themedius.ai']
    
    email = EmailMessage(subject, body, from_email, to_email, cc=cc_email)
    
    # Attach the screenshot
    email.attach_file('confirmation.png')
    
    # Send the email
    email.send()

send_email()
