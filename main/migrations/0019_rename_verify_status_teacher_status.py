# Generated by Django 5.1.1 on 2024-12-16 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0018_student_otp_digit_student_verify_status_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="teacher",
            old_name="verify_status",
            new_name="status",
        ),
    ]
