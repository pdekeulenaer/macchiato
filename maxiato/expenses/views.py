from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            u = form.save()
            return HttpResponseRedirect("/expenses/welcome")
    else:
        form = UserCreationForm()

    return render(request, "registration/registration.html", {'form':form})

# from django.http import HttpResponse

@login_required
def welcome(request):
    return HttpResponse("Hello " + request.user.username)

# def index(request):
#     return HttpResponse("Hello, world. You're at the expenses index.")
