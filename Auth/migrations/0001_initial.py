# Generated by Django 3.2.6 on 2021-08-10 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=1)),
                ('country', models.CharField(max_length=5)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
