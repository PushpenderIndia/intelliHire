from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_TYPES = [
        ('applicant', 'Applicant'), 
        ('recruiter', 'Recruiter')
    ]
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='applicant')
