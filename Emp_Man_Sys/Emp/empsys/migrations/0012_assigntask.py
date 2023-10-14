# Generated by Django 4.2.4 on 2023-10-02 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empsys', '0011_task_id_alter_task_employee_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=255)),
                ('employee_email', models.EmailField(max_length=254)),
                ('employee_phone', models.CharField(max_length=15)),
                ('employee_role', models.CharField(max_length=100)),
                ('task_name', models.CharField(max_length=255)),
                ('task_description', models.TextField()),
                ('task_submission_date', models.DateField()),
                ('file_submission', models.FileField(upload_to='task_files')),
            ],
        ),
    ]
