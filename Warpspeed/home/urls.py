from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_user, name="logout"),
    path("signup", views.signup, name="signup"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("job_offers", views.job_offers, name="job_offers"),
    path("potential_applicant", views.potential_applicant, name="potential_applicant"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)