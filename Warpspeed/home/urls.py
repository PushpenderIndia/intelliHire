from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_user, name="logout"),
    path("signup", views.signup, name="signup"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("job_offers", views.dashboard, name="dashboard"),
    path("potential_applicant", views.dashboard, name="dashboard"),
]