
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import render_to_string, get_template
# Create your views here.

def index(request):
    return render(request, 'index.html')

def email_one(request):
    subject = "I am the text email"
    to = ['harry0520520@gmail.com']
    from_email = 'harry0520520@gmail.com'
    ctx = {
        'user': 'Harry',
        'major': 'computer science'
    }

    message = render_to_string("body.txt", ctx)

    EmailMessage(subject, message, to=to, from_email=from_email).send()

    return HttpResponse('email_one')

def email_two(request):
    subject = "I am an HTML email"
    to = ['harry0520520@gmail.com']
    from_email = 'harry0520520@gmail.com'

    ctx = {
        'user': 'buddy',
        'major': 'computer science'
    }

    message = render_to_string("email.html", ctx)
    msg = EmailMessage(subject, message, to=to, from_email=from_email)
    msg.content_subtype = 'html'
    msg.send()

    return HttpResponse('email_two')