# Generated by Django 3.0.8 on 2021-04-10 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210410_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tumbnail',
            field=models.ImageField(upload_to='static/img'),
        ),
    ]
