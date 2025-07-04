# Generated by Django 5.2.3 on 2025-06-23 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeletedEmployee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=20)),
                ('employee_name', models.CharField(max_length=100)),
                ('employee_email', models.EmailField(max_length=254)),
                ('employee_contact', models.CharField(max_length=20)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
