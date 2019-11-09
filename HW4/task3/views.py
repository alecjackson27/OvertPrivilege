from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
import re
from .models import User
from .utils import *
from .task2 import task2

# Create your views here.
def index(request):
    return render(request, 'task3/index.html')

def signup(request):
    return render(request, 'task3/signup.html')

def create(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print(request.POST)
        # Use form data (contained in request.POST) to validate info using methods from tasks 1 and 2
        with open('../task1/createdPasswords.txt', 'r') as f:
            ECLP1 = f.read().split()
        dictionary_word = ""
        for i in range(len(ECLP1)):
            if ECLP1[i] =="$":
                dictionary_word = ECLP1[i + 1]
            elif ECLP1[i] == request.POST['password']:
                # Password is a variation of dictionary_word. Return to signup and inform user
                print("Placeholder")

        birth_date = request.POST['birth date'][6:8] + "/" + request.POST['birth date'][8:] \
            + "/" + request.POST['birth date'][:5]

        phone = re.sub("[^0-9]", "", request.POST['phone'])
        if len(phone) != 10:
            # Number is the wrong length. Return to signup and inform user
            print("Placeholder")
        else:
            phone = phone[:4] + "-" + phone[4:7] + "-" + phone[7:]

        ECLP2 = task2(request.POST['first'], request.POST['last'], request.POST['email'],
        phone, birth_date, request.POST['street'], request.POST['apt'], request.POST['city'],
        request.POST['state'], request.POST['zip'])

        for i in range(len(ECLP2) - 2):
            if ECLP2[i][0] == request.POST['password']:
                # Password is a variation on ECLP2[i][1]. Return to signup and inform user
                print("Placeholder")
        for i in range(len(ECLP2[len(ECLP2)-1])):
            if request.POST['password'].contains(ECLP2[len(ECLP2)-1][i][0]):
                # Password contains the number from ECLP2[len(ECLP2)-1][i][1]. Return to signup
                # and inform user
                print("Placeholder")

        

        
        # If data checks out, create a new user with form data and save it in the database, then
        # save hashed password and salt to respective files. Then redirect to a new URL:
        return HttpResponseRedirect('/thanks/')

        # Else take user back to form and give an error message

class UserDetailView(generic.DetailView):
    model = User
    template_name = 'task3/user_detail.html'
