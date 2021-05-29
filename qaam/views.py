from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def index(request):
    return HttpResponse("Hello, world. You're at the qaam index.")



