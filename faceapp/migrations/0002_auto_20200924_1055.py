# Generated by Django 3.1.1 on 2020-09-24 09:55

from django.db import migrations, models
import faceapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('faceapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='img',
            field=models.ImageField(upload_to=faceapp.models.get_admin_upload_path),
        ),
        migrations.AlterField(
            model_name='student',
            name='img',
            field=models.ImageField(upload_to=faceapp.models.get_student_upload_path),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=15)),
                ('course_title', models.ManyToManyField(to='faceapp.Student')),
            ],
        ),
    ]