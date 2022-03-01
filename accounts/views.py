from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

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
