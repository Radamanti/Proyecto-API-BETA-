# Generated by Django 4.0 on 2021-12-21 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ClientApp', '0004_rename_username_user_username_user_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='passWord',
            new_name='password',
        ),
    ]