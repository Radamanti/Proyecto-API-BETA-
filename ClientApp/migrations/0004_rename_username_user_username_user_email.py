# Generated by Django 4.0 on 2021-12-21 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClientApp', '0003_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='userName',
            new_name='username',
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='yesid', max_length=254),
            preserve_default=False,
        ),
    ]
