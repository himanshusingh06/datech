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
def portfolio(request):
    return render(request,'portfolio.html')

def services(request):
    return render(request, 'services.html')
def testimonial(request):
    return render(request, 'testimonial.html')
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
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')


        message_body = f'Contact form filled by {name}--- with the email {email}.\n\nMobile number -- {phone}\n\nThe Message provided is :\n {message}\n\n '
        message2 = EmailMessage(
        subject=subject,
        body=message_body,
        from_email=EMAIL_HOST_USER,
        to=['himanshuks062@gmail.com','arunk.mmc@gmail.com'])
        message2.send()
        return redirect('home')  # Redirect to the contact page or any other page
    return render(request, 'contact.html')  # Render the contact form template
