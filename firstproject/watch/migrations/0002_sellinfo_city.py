# Generated by Django 4.1.7 on 2023-06-04 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellinfo',
            name='city',
            field=models.CharField(default='New York', max_length=90),
        ),
    ]
