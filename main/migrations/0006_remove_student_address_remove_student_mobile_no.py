# Generated by Django 5.1.1 on 2024-10-21 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_teacher_detail_alter_chapter_course_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='address',
        ),
        migrations.RemoveField(
            model_name='student',
            name='mobile_no',
        ),
    ]
