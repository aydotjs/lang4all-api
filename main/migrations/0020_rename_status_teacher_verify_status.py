# Generated by Django 5.1.1 on 2024-12-16 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0019_rename_verify_status_teacher_status"),
    ]

    operations = [
        migrations.RenameField(
            model_name="teacher",
            old_name="status",
            new_name="verify_status",
        ),
    ]
