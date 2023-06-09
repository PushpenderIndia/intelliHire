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
    path("start_quiz", views.start_quiz, name="start_quiz"),
    path("quiz", views.main_quiz, name="quiz"),
    path("end_quiz", views.end_quiz, name="end_quiz"),
    path("interview", views.interview, name="interview"),
    path("ask_follow_ups", views.ask_follow_ups, name="ask_follow_ups"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)