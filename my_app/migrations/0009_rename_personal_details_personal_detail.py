# Generated by Django 5.0.7 on 2024-08-20 00:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0008_rename_personal_detail_personal_details'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='personal_details',
            new_name='personal_detail',
        ),
    ]