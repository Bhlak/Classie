# Generated by Django 5.0.3 on 2024-05-17 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_list', '0002_department_remove_clist_departments_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='faculty',
            field=models.CharField(default='faculty of computing and engineering sciences', max_length=100),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
