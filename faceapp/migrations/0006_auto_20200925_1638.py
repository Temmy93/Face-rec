# Generated by Django 3.1.1 on 2020-09-25 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faceapp', '0005_auto_20200925_1636'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='student',
            new_name='student_matric_number',
        ),
    ]
