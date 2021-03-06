# Generated by Django 3.1.1 on 2020-09-25 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faceapp', '0007_course_course_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='student_matric_number',
        ),
        migrations.AddField(
            model_name='course',
            name='student_matric_number',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.RemoveField(
            model_name='student',
            name='matric_number',
        ),
        migrations.AddField(
            model_name='student',
            name='matric_number',
            field=models.ManyToManyField(null=True, to='faceapp.Course'),
        ),
    ]
