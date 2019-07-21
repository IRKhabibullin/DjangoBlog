from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account for {username} is created')
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'])
            login(request, new_user)
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')
