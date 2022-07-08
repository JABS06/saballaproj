# Generated by Django 3.1.6 on 2022-07-06 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saballasys', '0008_auto_20220706_0411'),
    ]

    operations = [
        migrations.AddField(
            model_name='components',
            name='gpu',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='components',
            name='mobo',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='components',
            name='procs',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='components',
            name='psu',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='components',
            name='ram',
            field=models.CharField(max_length=100, null=True),
        ),
    ]