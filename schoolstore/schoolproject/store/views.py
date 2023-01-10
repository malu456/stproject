from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# Create your views here.
def demo(request):
    return render(request,"index.html")
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['confirm password']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect("login")

            else:
                user = User.objects.create_user(username=username, password=password)
                user.save();
                return redirect('register')

        else:
            messages.info(request, "password not matching")
            return redirect('/')
        return redirect('register')
    return render(request, "register.html")
def npage(request):

    return render(request,"newpage.html")
def form(request):
    return render(request,"form.html")
def msg(request):
    return render(request,"msg.html")