# Generated by Django 4.0.3 on 2022-06-29 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('saballasys', '0004_delete_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_fname', models.CharField(max_length=100, null=True)),
                ('p_sname', models.CharField(max_length=100, null=True)),
                ('p_email', models.CharField(max_length=100, null=True)),
                ('p_purpose', models.CharField(max_length=100, null=True)),
                ('p_budget', models.IntegerField(max_length=100, null=True)),
            ],
        ),
    ]
