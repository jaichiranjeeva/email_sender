from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings
# Create your views here.
def index(request):
    return render(request, "index.html")

def send(request):
    subject = request.POST['sub']
    message = request.POST['msg']
    settings.EMAIL_HOST_USER = request.POST['frm']
    settings.EMAIL_HOST_PASSWORD = request.POST['pswd']
    tom=request.POST['too'].split(';')
    if subject and message and settings.EMAIL_HOST_USER:
        send_mail(subject, message, settings.EMAIL_HOST_USER, tom, fail_silently=False)
        return HttpResponse('Mails Sent Succesfully!!!')
    else:
        return HttpResponse('Make sure all fields are entered and valid.')