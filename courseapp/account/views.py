from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages

from account.forms import LoginUserForm, NewUserForm, UserPasswordChangeForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm



def user_login(request):

    if request.user.is_authenticated and "next" in request.GET:
        return render(request, "account/login.html", {"error":"You doesn't have permission"}, )

    
    if request.method == "POST":
        form = LoginUserForm(request, data = request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
        
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, "login successful")
                nextUrl = request.GET.get("next", None)

                if nextUrl is None:
                    return redirect("index")
                else:
                    return redirect(nextUrl)
                
            else:
                return render(request, "account/login.html", {"form":form})
        
        else:
            return render(request, "account/login.html", {"form":form})
    else:
        form = LoginUserForm()
        return render(request, "account/login.html", {"form":form})
    


def user_register(request):

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
           form.save()

           username = form.cleaned_data["username"]
           password = form.cleaned_data["password1"]

           user = authenticate(request, username=username, password=password)
           login(request, user)
           return redirect("index")
       
        else:
            return render(request, "account/register.html", {"form": form})

    else:
        form = NewUserForm()
        return render(request, "account/register.html", {"form": form})
    


def change_password(request):
    if request.method == "POST":
        form = UserPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "password have updated")
            return redirect("change_password")
        return render(request, "account/change-password.html", {"form": form})
    
    form = UserPasswordChangeForm(request.user)
    return render(request, "account/change-password.html", {"form": form})



def user_logout(request):
    messages.add_message(request, messages.SUCCESS, "logout successful")
    logout(request)
    return redirect("index")