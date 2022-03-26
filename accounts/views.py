from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, AccountUpdateForm, ProfileFormUpdate

def account_signup(request):
    """
    Is what is run when the signup url is called upon
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/signup.html', {'form' : form})


# Creates the login_view
def login_view(request):
    """
    Is what is run when the login in url is called upon
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('tattooposts:gallery')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


# Creates the log out view
def logout_view(request):
    """
    Logsout the user to the site
    """
    if request.method == 'POST':
        logout(request)
        return redirect('homepage')
    form = AuthenticationForm()
    return render(request, 'accounts/logout.html', {'form': form})


@login_required(login_url="/accounts/login/")
def profile_view(request):
    """
    Shows the Users profile only if logged in
    """
    if request.method == 'POST':
        account_form = AccountUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileFormUpdate(request.POST, request.FILES, instance=request.user.profile)
        if account_form.is_valid() and profile_form.is_valid():
            account_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been saved!')
            return redirect('profile')
    else:
        account_form = AccountUpdateForm(instance=request.user)
        profile_form = ProfileFormUpdate(instance=request.user.profile)
    
    context = {
        'account_form' : account_form,
        'profile_form' : profile_form
    }

    return render(request, 'accounts/profile.html', context)
