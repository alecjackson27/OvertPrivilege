from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
import re
from .models import User
from .utils import *
from .task2 import task2

# Create your views here.
OFFSET = timedelta(hours=7)

def index(request):
    return render(request, 'task3/index.html')


def login(request):
    # TO DO: login
    if request.method == "GET":
        # print(request.GET)
        user = User.objects.filter(email=request.GET['login'])
        if len(user) == 0:
            # No such user, return to login and tell user
            messages.warning(request, "No user with that email is registered")
            url = "../task3/"
            return HttpResponseRedirect(url, request)
        elif user[0].locked_out_until > timezone.now() - OFFSET:
            messages.warning(request, (user[0].email + " is locked out until "
            + user[0].locked_out_until.strftime("%m/%d/%Y, %H:%M:%S")))
            url = "../task3/"
            return HttpResponseRedirect(url, request)
        elif calculate_hash2(request.GET['password'], user[0].salt) == get_password_byID(user[0].id):
            request.session.__setitem__(
                "authentication", get_password_byID(user[0].id))
            request.session.__setitem__('authenticate_email', user[0].email)
            request.session.save()
            user[0].failed_logins = 0
            user[0].save()
            url = "../task3/" + str(user[0].id) + "/"
            return HttpResponseRedirect(url, request)
        else:
            # Invalid login credentials, return to login and tell user. Increment failed logins
            # and, if necessary, lock user out
            user[0].failed_logins += 1
            user[0].save()
            if user[0].failed_logins % 3 == 0:
                minutes = 2 ** (user[0].failed_logins / 3 - 1)
                user[0].locked_out_until = timezone.now() - OFFSET + \
                    timedelta(minutes=minutes)
                user[0].save()
                messages.warning(request, "Too many failed login attempts. "
                                 + (user[0].email + " is locked out until "
                                    + user[0].locked_out_until.strftime("%m/%d/%Y, %H:%M:%S")))
                url = "../task3/"
                return HttpResponseRedirect(url, request)
            else:
                messages.warning(request, "Invalid login")
                url = "../task3/"
                return HttpResponseRedirect(url, request)


def logout(request):
    request.session.flush()
    request.session.save()
    return HttpResponseRedirect("../task3", request)


def signup(request):
    return render(request, 'task3/signup.html')


def create(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        if len(request.POST['password']) < 8:
            messages.warning(request,
            'Password must be at least 8 characters long', )
            return HttpResponseRedirect("../signup", request)
        # print(request.POST)
        # Use form data (contained in request.POST) to validate info using methods from tasks 1 and 2
        with open('task1/createdPasswords.txt', 'r') as f:
            ECLP1 = f.read().split()
        dictionary_word = ""
        for i in range(len(ECLP1)):
            if ECLP1[i] == "$":
                dictionary_word = ECLP1[i + 1]
            elif ECLP1[i] == request.POST['password']:
                # Password is a variation of dictionary_word. Return to signup and inform user
                messages.warning(request,
                                 'Input password is vulnerable to dictionary guessing attack because it used the dictionary word: '
                                 + dictionary_word + " or a variation of this word")
                return HttpResponseRedirect("../signup", request)

        birthDate = request.POST['birth'][5:7] + "/" + request.POST['birth'][8:] \
            + "/" + request.POST['birth'][:4]

        phone = re.sub("[^0-9]", "", request.POST['phone'])
        if len(phone) != 10:
            # Number is the wrong length. Return to signup and inform user
            messages.warning(request,
                             'Input phone number is invalid', )
            return HttpResponseRedirect("../signup", request)
        else:
            phone = phone[:4] + "-" + phone[4:7] + "-" + phone[7:]

        ECLP2 = task2(request.POST['first'], request.POST['last'], request.POST['email'],
                      phone, birthDate, request.POST['street'], request.POST['apt'], request.POST['city'],
                      request.POST['state'], request.POST['zip'])

        for i in range(len(ECLP2) - 1):
            print(ECLP2[i][0])
            if ECLP2[i][0] == request.POST['password']:
                # Password is a variation on ECLP2[i][1]. Return to signup and inform user
                messages.warning(request,
                                 'Input password is vulnerable to targeted guessing attack because it used all or part of your '
                                 + ECLP2[i][1] + " or a variant")
                return HttpResponseRedirect("../signup", request)
        for i in range(len(ECLP2[len(ECLP2)-1])):
            if ECLP2[len(ECLP2)-1][i][0] in request.POST['password']:
                # Password contains the number from ECLP2[len(ECLP2)-1][i][1]. Return to signup
                # and inform user
                messages.warning(request,
                                 'Input password is vulnerable to targeted guessing attack because it used all or part of a number from your '
                                 + ECLP2[len(ECLP2)-1][i][1])
                return HttpResponseRedirect("../signup", request)

        if len(User.objects.filter(email=request.POST['email'])) > 0:
            # Email is taken. return to signup and inform user.
            messages.warning(request,
                             'Email already taken')
            return HttpResponseRedirect("../signup", request)

        new_user = User(
            first_name=request.POST['first'],
            last_name=request.POST['last'],
            email=request.POST['email'],
            birth_date=birthDate,
            street=request.POST['street'],
            apt=request.POST['apt'],
            city=request.POST['city'],
            state=request.POST['state'],
            zip=request.POST['zip'],
            phone_number=phone
        )

        new_user.save()

        calculate_hash(request.POST['password'], new_user.salt, new_user.id)

        sessionID = get_password_byID(new_user.id)

        request.session.__setitem__("authentication", sessionID)
        request.session.__setitem__('authenticate_email', new_user.email)
        request.session.save()

        # If data checks out, create a new user with form data and save it in the database, then
        # save hashed password and salt to respective files. Then redirect to a new URL:
        url = "../" + str(new_user.id) + "/"
        return HttpResponseRedirect(url, request)

        # Else take user back to form and give an error message


class UserDetailView(generic.DetailView):
    model = User
    template_name = 'task3/user_detail.html'

    def get(self, request, *args, **kwargs):
        user = User.objects.filter(id=self.kwargs['pk'])
        if request.session.__contains__('authentication') \
                and request.session.__contains__('authenticate_email'):
            if request.session.__getitem__('authentication') == get_password_byID(user[0].id) \
                    and request.session.__getitem__('authenticate_email') == user[0].email:
                self.object = user[0]
                context = self.get_context_data(object=self.get_object())
                return render(request, self.template_name, context)
            else:
                return HttpResponseRedirect("../../task3", request)
        else:
            return HttpResponseRedirect("../../task3", request)
