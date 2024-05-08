# Generated by Django 5.0.3 on 2024-05-07 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('faculty', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('course_title', models.CharField(max_length=100)),
                ('course_code', models.CharField(max_length=100)),
                ('passwordd', models.CharField(max_length=100)),
            ],
        ),
    ]
