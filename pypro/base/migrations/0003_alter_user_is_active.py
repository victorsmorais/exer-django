# Generated by Django 3.2.7 on 2021-09-19 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active.' # noqa 
                                                              ' Unselect this instead of deleting accounts.',
                                      verbose_name='active'),
        ),
    ]
