from django.urls import path
from .views import LandingPageView
from .views import UserRegisterView, UserLoginView, UserLogOutView,UserCrudView

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing'),
    path("auth/register/", UserRegisterView.as_view(), name="register"),
    path("auth/login/", UserLoginView.as_view(), name="login"),
    path("auth/logout/", UserLogOutView.as_view(), name="logout"),
    path("auth/crud", UserCrudView.as_view(), name="crud"),
    path("auth/create", UserCrudView.as_view,name="create"),
    path("auth/edit/<int:id>/", UserCrudView.as_view,name='edit'),
    path("auth/delete/<int:id>/", UserCrudView.as_view,name='delete'),

]