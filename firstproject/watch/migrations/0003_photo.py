# Generated by Django 4.1.7 on 2023-06-04 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0002_sellinfo_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='myimage')),
            ],
        ),
    ]