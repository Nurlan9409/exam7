from django.urls import path
from .views import LandingPageView
#from .views import UserRegisterView, UserLoginView, UserLogOutView

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing'),
]