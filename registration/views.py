from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import SignUpForm, CodeVerificationForm
from django.contrib.auth import login


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists() or User.objects.filter(
                    username=form.cleaned_data['username']).exists():
                return render(request, 'registration/sign_up.html', {"form": form, "error": 'Имя уже занято. Попробуйте другое имя'})
            else:
                new_user = User.objects.create_user(username=form.cleaned_data['username'],
                                                          password=form.cleaned_data['password'])
                login(request, new_user)
                return redirect('code_vef')

    else:
        form = SignUpForm
    return render(request, 'registration/sign_up.html', {"form": form})


def code_verification(request):
    if request.method == 'POST':
        form = CodeVerificationForm(request.POST)
    else:
        form = CodeVerificationForm
    return render(request, 'registration/code_verification.html', {"form": form})
