from django.shortcuts import render

# Create your views here.
def signup_view(request):
    context = {

    }
    return render(request, 'accounts/signup.html', context)

def login_view(request):
    context = {

    }
    return render(request, 'accounts/login.html', context)

def logout_view(request):
    context = {

    }
    # TODO Need to write to homepage
    return render(render, 'accounts/signup.html', context)
