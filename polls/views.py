from django.shortcuts import render

# Create your views here.

from .models import Question, Choice

# Det Questins n display


def index(request):
    return render(request, "polls/index.html")
