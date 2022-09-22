from lib2to3.pgen2.pgen import generate_grammar
import re
from django.shortcuts import render

import string
import random

# from django.http import HttpResponse

# Create your views here.
def about(request):
    return render(request, "about.html")


def home(request):
    return render(request, "home.html")


def password(request):
    characters = list(string.ascii_lowercase)
    upper = string.ascii_uppercase
    number = string.digits
    punctuation = string.punctuation
    password_generated = []

    if request.GET.get("uppercase"):
        characters.extend(upper)
    if request.GET.get("number"):
        characters.extend(number)
    if request.GET.get("punctuation"):
        characters.extend(punctuation)

    password_length = int(request.GET.get("length"))
    random.shuffle(characters)
    for x in range(password_length):
        password_generated.append(random.choice(characters))

    random.shuffle(password_generated)

    password_generated = "".join(password_generated)
    return render(request, "password.html", {"password": password_generated})
