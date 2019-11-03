from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from .models import User
from .utils import *

# Create your views here.
def index(request):
    return render(request, 'task3/index.html')

def signup(request):
    return render(request, 'task3/signup.html')

def create(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # Use form data (contained in request.POST) to validate info using methods from tasks 1 and 2

        # If data checks out, create a new user with form data and save it in the database, then
        # save hashed password and salt to respective files. Then redirect to a new URL:
        return HttpResponseRedirect('/thanks/')

        # Else take user back to form and give an error message

class UserDetailView(generic.DetailView):
    model = User
    template_name = 'task3/user_detail.html'
