# Generated by Django 4.0.4 on 2022-05-28 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='image',
            name='description',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='location',
            name='Description',
            field=models.TextField(max_length=255),
        ),
    ]
