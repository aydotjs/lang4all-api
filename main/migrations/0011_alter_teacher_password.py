# Generated by Django 5.1.1 on 2024-10-24 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_teacher_detail_teacher_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='password',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
