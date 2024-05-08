# Generated by Django 5.0.4 on 2024-05-06 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=10)),
                ('matric_no', models.CharField(max_length=10)),
                ('faculty', models.CharField(max_length=15)),
                ('department', models.CharField(max_length=20)),
                ('level', models.IntegerField()),
                ('user_type', models.CharField(default='student', max_length=10)),
            ],
        ),
    ]
