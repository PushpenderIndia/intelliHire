from django import forms

class RecruiterForm(forms.Form):
    job_role = forms.CharField(max_length=255)
    no_of_applicant = forms.IntegerField(min_value=1)
    additional_skills = forms.CharField(max_length=255, required=False)
    no_of_questions = forms.IntegerField(min_value=1)
    want_disabled_applicant = forms.BooleanField(required=False)