# Generated by Django 4.2.3 on 2023-07-20 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_student_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='dob',
        ),
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(default=' ', max_length=50),
            preserve_default=False,
        ),
    ]
