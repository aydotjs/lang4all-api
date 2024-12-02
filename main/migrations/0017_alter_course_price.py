# Generated by Django 5.1.1 on 2024-11-29 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0016_course_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="price",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]