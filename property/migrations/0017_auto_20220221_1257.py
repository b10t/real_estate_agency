# Generated by Django 2.2.24 on 2022-02-21 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0016_auto_20220221_0646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='new_building',
            field=models.NullBooleanField(verbose_name='Новостройка'),
        ),
    ]