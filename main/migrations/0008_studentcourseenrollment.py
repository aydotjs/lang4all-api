# Generated by Django 5.1.1 on 2024-10-21 16:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_rename_qualification_student_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentCourseEnrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrolled_time', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrolled_courses', to='main.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrolled_student', to='main.student')),
            ],
            options={
                'verbose_name_plural': '6. Enrolled Courses',
            },
        ),
    ]
