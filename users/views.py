from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

from users.forms import RegisterForm, ProfileForm


# Create your views here.
class RegisterView(View):
    def get(self,request):
        user = RegisterForm()
        return render(request,'register.html',{"form":user})
    def post(self,request):
        user = RegisterForm(data=request.POST,files=request.FILES)

        if user.is_valid():
            user.save()
            return redirect('users:login')
        else:
            return render(request, 'register.html', {"form": user})


class Login(View):
    def get(self,request):
        user = AuthenticationForm()
        return render(request,'login.html',{"form":user})
    def post(self,request):
        user = AuthenticationForm(data=request.POST)


        if user.is_valid():
            user = user.get_user()
            login(request, user)
            user.save()
            return redirect("landing")
        else:
            return render(request, 'login.html', {"form": user})



class ProfileView(View):
    def get(self,request):
        user = request.user
        user_form = ProfileForm(instance=request.user)
        return render(request,'profile.html',{"user":user,"form":user_form})
    def post(self,request):
        user_form = ProfileForm(instance=request.user,data=request.POST,files=request.FILES)
        if user_form.is_valid():
            user_form.save()
            return redirect("users:profile")
        else:
            return render(request, 'profile.html', {"user": user, "form": user_form})
