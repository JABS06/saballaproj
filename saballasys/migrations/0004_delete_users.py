# Generated by Django 4.0.3 on 2022-06-26 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saballasys', '0003_rename_item_users'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
    ]
