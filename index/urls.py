from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from .forms import LoginForm


urlpatterns = [
    path('', index, name="index"),

    path('project/', static_project, name="static_project"),
    path('tech/', static_tech, name="static_tech"),
    path('alliance/', static_alliance, name="static_alliance"),

    path(
        'user/signout/',
        auth_views.logout_then_login,
        name='signout',

    ),
    path(
        'user/signin/',
        auth_views.LoginView.as_view(template_name='layout/signin.html', authentication_form=LoginForm,
                                     extra_context={}),
        name="signin"
    ),
]
