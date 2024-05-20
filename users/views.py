
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from category.models import Category,Product
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserLoginForm,UserRegisterForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseNotFound

class LandingPageView(View):
    def get(self, request):
        category = Category.objects.all()
        product = Product.objects.all()
        users = User.objects.all()
        contex = {
            'category':category,
            'product':product,
            'users':users

        }
        return render(request, 'main/index.html',contex)

class UserRegisterView(View):
    def get(self, request):
        return render(request, "auth/register.html")

    def post(self, request):
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        username = request.POST["username"]
        password_1 = request.POST["password_1"]
        password_2 = request.POST["password_2"]
        if password_1 == password_2:
            user_check = User.objects.filter(username=username, password=password_1)
            if user_check:
                return render(request, "auth/register.html")
            else:
                user = User(first_name=first_name, last_name=last_name, email=email, username=username)
                user.set_password(password_1)
                user.save()
                return redirect("login")
        else:
            return render(request, "auth/register.html")


class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        context = {
            "form": form
        }
        return render(request, "auth/login.html", context)

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]

        data = {
            "username": username,
            "password": password
        }
        login_form = AuthenticationForm(data=data)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect("landing")

        else:
            form = UserLoginForm()
            context = {
                "form": form
            }
            return render(request, "auth/login.html", context)

class UserLogOutView(View):
    def get(self, request):
        logout(request)
        return redirect("landing")


class UserCrudView(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, "auth/crud.html", {'users':users})

    def post(request):
        if request.method == "POST":
            user = User()
            user.first_name = request.POST.get("first_name")
            user.last_name = request.POST.get("last_name")
            user.email = request.POST.get("email")
            user.phone = request.POST.get("phone")
            user.password = request.POST.get("password")
            user.save()
        return HttpResponseRedirect("/")

    def edit(request, id):
        try:
            user = User.objects.get(id=id)

            if request.method == "POST":
                user.first_name = request.POST.get("first_name")
                user.last_name = request.POST.get("last_name")
                user.email = request.POST.get("email")
                user.phone = request.POST.get("phone")
                user.password = request.POST.get("password")
                user.save()
                return HttpResponseRedirect("/")
            else:
                return render(request, "edit.html", {"user": user})
        except User.DoesNotExist:
            return HttpResponseNotFound("<h2>Person not found</h2>")

    def delete(request, id):
        try:
            user = User.objects.get(id=id)
            user.delete()
            return HttpResponseRedirect("/")
        except User.DoesNotExist:
            return HttpResponseNotFound("<h2>Person not found</h2>")
