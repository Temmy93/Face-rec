# Generated by Django 3.1.1 on 2020-09-25 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faceapp', '0004_auto_20200925_1456'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='course_title',
            new_name='student',
        ),
    ]
