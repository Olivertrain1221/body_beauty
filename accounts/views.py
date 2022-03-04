from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.


def account_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #log the user in at some point!!!
            return redirect('tattooposts:gallery')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'formsignup': form})

# Creates the login_view
def login_view(request):
    if request.method == 'POST':
       form = AuthenticationForm(data=request.POST)
       if form.is_valid():
           #login user
           return redirect('tattooposts:gallery')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})