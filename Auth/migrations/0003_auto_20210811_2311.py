# Generated by Django 3.2.6 on 2021-08-11 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0002_account_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='password',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='account',
            name='token',
            field=models.TextField(),
        ),
    ]
