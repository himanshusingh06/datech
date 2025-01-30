from django.shortcuts import render,redirect
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from datech.settings import EMAIL_HOST_USER
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'landing.html')


def about(request):
    return render(request,'about.html')

def services(request):
    return render(request, 'services.html')
# def send_mail_to_admin(user_name, user_email, mobile_number,subject,user_message):
    
#     message_body = f'Form filled by {user_name}--- with the email {user_email}.\n\nMobile number -- {mobile_number}\n\nThe Message provided is :\n {user_message}'
#     message = EmailMessage(
#         subject=f'New form filled by {user_name}--- with subject {subject}',
#         body=message_body,
#         from_email=settings.EMAIL_HOST_USER,
#         to=['galsphat@gmail.com']
#     )
#     message.send()

def contact(request):
    if request.method == 'POST':
        user_name = request.POST.get('name')
        user_email = request.POST.get('email')
        mobile_number = request.POST.get('phone')
        usubject = request.POST.get('subject')
        user_message = request.POST.get('message')


        subject = f'New form filled by {user_name}--- with subject {usubject}'
        message = f'Form filled by {user_name}--- with the email {user_email}.\n\nMobile number -- {mobile_number}\n\nThe Message provided is :\n {user_message}'
        recipient_list = ["himanshukrs5760@gmail.com"]

        send_mail(subject, message, EMAIL_HOST_USER, recipient_list, fail_silently=True)
        
        
        # send_mail_to_admin(user_name, user_email, mobile_number, subject, user_message)
        return redirect('home')
    else:
        return render(request, 'contact.html')