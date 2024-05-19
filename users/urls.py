from django.urls import path
from .views import LandingPageView
from .views import UserRegisterView, UserLoginView, UserLogOutView

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing'),
    path("auth/register/", UserRegisterView.as_view(), name="register"),
    path("auth/login/", UserLoginView.as_view(), name="login"),
    path("auth/logout/", UserLogOutView.as_view(), name="logout"),

]