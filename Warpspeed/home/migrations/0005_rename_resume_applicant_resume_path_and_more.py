# Generated by Django 4.0.6 on 2023-05-14 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_applicant'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicant',
            old_name='resume',
            new_name='resume_path',
        ),
        migrations.AddField(
            model_name='applicant',
            name='resume_url',
            field=models.CharField(default='', max_length=255),
        ),
    ]
