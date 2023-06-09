# Generated by Django 4.0.6 on 2023-05-14 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rename_resume_applicant_resume_path_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shortlisted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('job_role', models.CharField(max_length=255)),
                ('recruiter_username', models.CharField(max_length=255)),
                ('no_of_questions', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
