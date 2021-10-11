# Generated by Django 3.2.8 on 2021-10-06 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='modulo',
            options={'ordering': ('order',)},
        ),
        migrations.AddField(
            model_name='modulo',
            name='descricao',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='modulo',
            name='order',
            field=models.PositiveIntegerField(db_index=True, editable=False, null=True, verbose_name='order'),
        ),
        migrations.AddField(
            model_name='modulo',
            name='publico',
            field=models.TextField(null=True),
        ),
    ]
