from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup_view(request):

    if request.method == 'POST':
    # The user wants to sign up - the user has info and wants to have an account now!
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error':'Username is already taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('home')
        else:
        # User wants to enter information
            return render(request, 'accounts/signup.html', {'error':'Passwords must match'})
    else:
        context = {

        }
        return render(request, 'accounts/signup.html', context)

def login_view(request):

    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error':'Username or Password is incorrect. Please try again.'})

    else:
        context = {
        }
        return render(request, 'accounts/login.html', context)

def logout_view(request):

    # Lougout MUST be POST
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

    context = {

    }
    # TODO Need to write to homepage
    return render(request, 'accounts/signup.html', context)
