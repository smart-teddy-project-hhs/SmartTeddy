# Generated by Django 3.1.2 on 2020-10-24 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('speechrecognition', '0004_auto_20201024_0842'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LemmaSaid',
            new_name='SaidLemma',
        ),
    ]
