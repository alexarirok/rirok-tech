from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def home(request):
    template = 'index.html'
    return render(request, template, { })

def about(request):
    template = 'aboutus.html'
    return render(request, template, { })

@login_required
def contact(request):
    template = 'contact.html'
    if request.method == 'POST':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            name  = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, email, ['kipkoechk38@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('sucess') 
    return render(request, template, {'form':form})

def service(request):
    template = 'service.html'
    return render(request, template, { })

def base(request):
    template = 'base.html'
    return render(request, template, { })
# Create your views here.
