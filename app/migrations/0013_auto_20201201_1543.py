# Generated by Django 2.2.2 on 2020-12-01 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20201201_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicantregisteration',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]