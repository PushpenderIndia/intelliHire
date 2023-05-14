from django.contrib import admin
from .models import User
from .models import Recruiter
from .models import Applicant

# Register your models here.
admin.site.register(User)
admin.site.register(Recruiter)
admin.site.register(Applicant)