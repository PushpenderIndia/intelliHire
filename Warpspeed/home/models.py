from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPES = [
        ('applicant', 'Applicant'), 
        ('recruiter', 'Recruiter')
    ]
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='applicant')

class Recruiter(models.Model):
    owner = models.CharField(max_length=255, default='')
    job_role = models.CharField(max_length=255, default='')
    no_of_applicant = models.IntegerField()
    additional_skills = models.CharField(max_length=255, blank=True, null=True)
    no_of_questions = models.IntegerField()
    want_disabled_applicant = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.job_role
    
class Applicant(models.Model):
    owner = models.CharField(max_length=255, default='')
    resume_path = models.CharField(max_length=255, default='')
    resume_url = models.CharField(max_length=255, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Shortlisted(models.Model):
    username = models.CharField(max_length=255)
    job_role = models.CharField(max_length=255)
    recruiter_username = models.CharField(max_length=255)
    no_of_questions = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} - {self.job_role} ({self.recruiter_username})"