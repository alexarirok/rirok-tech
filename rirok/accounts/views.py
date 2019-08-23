from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import login, authenticate

def signup(request):
    template = 'signup.html'
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm
    return render(request, template, {'form':form})


# Create your views here.
