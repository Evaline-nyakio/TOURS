# Generated by Django 3.2.12 on 2023-05-25 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0028_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logo',
            name='cover',
            field=models.ImageField(upload_to='logo/'),
        ),
    ]