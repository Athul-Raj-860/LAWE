# Generated by Django 5.1.5 on 2025-02-24 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0031_rename_id_case_details_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lawyer_register',
            old_name='Lawyer_Id',
            new_name='Id',
        ),
    ]
