# Generated by Django 5.1.5 on 2025-02-24 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0036_remove_case_details_id_case_details_case_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_details',
            name='User_Id',
        ),
    ]
