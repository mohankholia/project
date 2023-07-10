from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("about", views.about, name="about"),
    path("ranking", views.ranking, name="ranking"),
    path("contest", views.contest, name="contest"),
    path("Login", views.login, name="Login"),
    path("profile", views.profile, name="profile"),
    path("Signup", views.signup, name="Signup"),
    path("submit", views.submit, name="submit"),
    path("welcome", views.welcome, name="welcome"),
]
