# Generated by Django 3.1.6 on 2022-07-08 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saballasys', '0013_remove_info_p_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedmes', models.TextField(null=True)),
                ('feedname', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(null=True)),
                ('feedname', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
