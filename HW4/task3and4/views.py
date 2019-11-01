from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'task3and4/index.html')

def signup(request):
    return render(request, 'task3and4/signup.html')