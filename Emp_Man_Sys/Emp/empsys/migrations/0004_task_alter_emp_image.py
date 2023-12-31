# Generated by Django 4.2.4 on 2023-09-25 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empsys', '0003_emp_address_emp_country_emp_image_emp_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('employee_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('employee_name', models.CharField(max_length=255)),
                ('employee_email', models.EmailField(max_length=254)),
                ('employee_phone', models.CharField(max_length=15)),
                ('employee_role', models.CharField(max_length=100)),
                ('task_number', models.CharField(max_length=10)),
                ('task_name', models.CharField(max_length=255)),
                ('task_description', models.TextField()),
                ('task_submission_date', models.DateField()),
                ('file_submission', models.FileField(upload_to='task_files')),
                ('status', models.CharField(choices=[('Approved', 'Approved'), ('Not Approved', 'Not Approved')], max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='emp',
            name='image',
            field=models.ImageField(default='profile_images/default.png', upload_to='profile_images'),
        ),
    ]
