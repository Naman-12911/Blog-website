# Generated by Django 3.0.8 on 2021-04-16 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_blogcomment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tumbnail',
        ),
    ]
