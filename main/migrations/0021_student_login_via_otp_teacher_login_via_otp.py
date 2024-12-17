# Generated by Django 5.1.1 on 2024-12-16 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0020_rename_status_teacher_verify_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="login_via_otp",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="teacher",
            name="login_via_otp",
            field=models.BooleanField(default=False),
        ),
    ]
