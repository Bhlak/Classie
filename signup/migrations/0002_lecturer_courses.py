# Generated by Django 5.0.4 on 2024-06-19 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_list', '0001_initial'),
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecturer',
            name='courses',
            field=models.ManyToManyField(to='course_list.clist'),
        ),
    ]
