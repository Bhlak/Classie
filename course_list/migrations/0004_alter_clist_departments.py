# Generated by Django 5.0.3 on 2024-05-17 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_list', '0003_department_faculty_alter_department_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clist',
            name='departments',
            field=models.ManyToManyField(related_name='courses', to='course_list.department'),
        ),
    ]
