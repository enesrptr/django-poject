from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def user_login(request):

    if request.user.is_authenticated and "next" in request.GET:
        return render(request, "account/login.html", {"error":"You doesn't have permission"}, )

    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request, username=username, password= password)

        if user is not None:
            login(request, user)
            nextUrl = request.GET.get("next", None)

            if nextUrl is None:
                return redirect("index")
            else:
                return redirect(nextUrl)
        else:
            return render(request, "account/login.html", {"error":"username or password wrong"}, )
    else:
        return render(request, "account/login.html")
    


def user_register(request):

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        if password != repassword:
            return render(request, "account/register.html",
                          {"error":"Entered password already exists",
                           "username":username,
                           "email":email},)
        
        if User.objects.filter(username = username).exists():
            return render(request, "account/register.html",
                          {"error":"Entered username already exists",
                           "username":username,
                           "email":email},)
        
        if User.objects.filter(email = email).exists():
            return render(request, "account/register.html", 
                          {"error":"Entered email already exists",
                           "username":username,
                           "email":email},)
                
        user = User.objects.create_user(username = username, email=email, password=password)
        user.save()
        return redirect("user_login")

    else:
            return render(request, "account/register.html")
        

def user_logout(request):
    logout(request)
    return redirect("index")