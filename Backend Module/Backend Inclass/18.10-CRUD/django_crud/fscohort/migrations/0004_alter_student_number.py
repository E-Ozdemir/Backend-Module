# Generated by Django 3.2.8 on 2021-11-26 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fscohort', '0003_alter_student_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='number',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
