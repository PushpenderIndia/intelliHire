from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from .models import User 
from .models import Recruiter
from .models import Applicant
from .forms import RecruiterForm


def index(request):
    return render(request, "index.html")

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            # Add error message for invalid credentials
            context = {'error_message': 'Invalid username or password.'}
            return render(request, 'login.html', context=context)
    else:
        return render(request, 'login.html')
    
def logout_user(request):
    logout(request)
    return redirect('login')

def signup(request):
    if request.method == 'POST':
        user_type = request.GET.get("user_type", "applicant")
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        if password != confirm_password:
            messages.error(request, 'Password not matched!')
            return render(request, 'signup.html')

        if User.objects.filter(username=login).exists():
            messages.error(request, 'Username already exists')
            return render(request, 'signup.html')

        # Validate password complexity
        password_complexity = [
            lambda s: any(x.isupper() for x in s),
            lambda s: any(x.islower() for x in s),
            lambda s: any(x.isdigit() for x in s),
            lambda s: len(s) >= 8
        ]
        if not all(rule(password) for rule in password_complexity):
            messages.error(request, 'Password should contain at least 8 characters, one uppercase letter, one lowercase letter, and one digit')
            return render(request, 'signup.html')

        # Create user with is_active=False so that the admin can approve it first
        user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)
        user.user_type = user_type
        user.save()

        return redirect("dashboard")

    return render(request, 'signup.html')

def dashboard(request):
    context = {}
    if request.method == 'POST':
        if request.user.user_type == 'applicant':
            try:
                file = request.FILES['myfile']
                fs = FileSystemStorage()
                filename = fs.save(file.name, file)
                uploaded_file_url = fs.url(filename)
                uploaded_file_path = fs.path(filename)
                Applicant(owner=request.user, resume_path=uploaded_file_path, resume_url=uploaded_file_url).save()
                messages.success(request, f'Resume Uploaded Successfully!')

            except Exception as e:
                print(f"Error [Upload]: {e}")

        else:
            form = RecruiterForm(request.POST)
            if form.is_valid():
                job_role                = form.cleaned_data['job_role']
                no_of_applicant         = form.cleaned_data['no_of_applicant']
                additional_skills       = form.cleaned_data['additional_skills']
                no_of_questions         = form.cleaned_data['no_of_questions']
                want_disabled_applicant = form.cleaned_data['want_disabled_applicant']
                recruiter = Recruiter(owner=request.user, job_role=job_role, no_of_applicant=no_of_applicant, 
                                    additional_skills=additional_skills, 
                                    no_of_questions=no_of_questions, 
                                    want_disabled_applicant=want_disabled_applicant)
                recruiter.save()
                messages.success(request, 'Job Post Created Successfully! Click on Potential Applicant to View Job Post')
            context['form'] = form
    else:
        form = RecruiterForm()
        context['form'] = form
        if Applicant.objects.last() is not None:
            context["resume_uploaded"] = Applicant.objects.last()
    return render(request, 'dashboard.html', context)

def job_offers(request):
    return render(request, "job_offer.html")

def potential_applicant(request):
    context = {}
    context['recruiter'] = Recruiter.objects.filter(owner=request.user)
    return render(request, "potential_applicant.html", context)

