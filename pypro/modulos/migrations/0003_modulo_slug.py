# Generated by Django 3.2.8 on 2021-10-06 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0002_auto_20211005_2224'),
    ]

    operations = [
        migrations.AddField(
            model_name='modulo',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
