from django.shortcuts import render
from .models import Users
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserLoginForm,UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from category.models import Category,Product
from django.contrib.auth.mixins import LoginRequiredMixin

class LandingPageView(View):
    def get(self, request):
        category = Category.objects.all()
        product = Product.objects.all()
        user = Users.objects.all()
        contex = {
            'category':category,
            'product':product,
            'user':user,

        }
        return render(request, 'main/index.html',contex)

class UserRegisterView(View):
    def get(self, request):
        return render(request, "main/login.html")

    def post(self, request):
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        username = request.POST["username"]
        password_1 = request.POST["password_1"]
        password_2 = request.POST["password_2"]
        if password_1 == password_2:
            user_check = Users.objects.filter(username=username, password=password_1)
            if user_check:
                return render(request, "main/login.html")
            else:
                user = Users(first_name=first_name, last_name=last_name, email=email, username=username)
                user.set_password(password_1)
                user.save()
                return redirect("login")
        else:
            return render(request, "main/login.html")


class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        context = {
            "form": form
        }
        return render(request, "main/login.html", context)

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]

        data = {
            "username": username,
            "password": password
        }
        login_form = AuthenticationForm(data=data)
        if login_form.is_valid():
            customer = login_form.get_user()
            login(request, customer)
            return redirect("landing")

        else:
            form = UserLoginForm()
            context = {
                "form": form
            }
            return render(request, "main/login.html", context)

class UserLogOutView(View):
    def get(self, request):
        logout(request)
        return redirect("landing")


