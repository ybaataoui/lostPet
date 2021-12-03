# Generated by Django 3.2.9 on 2021-11-21 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0004_auto_20211120_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petowner',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='petowner',
            name='first_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='petowner',
            name='last_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='petowner',
            name='phone',
            field=models.CharField(max_length=255),
        ),
    ]