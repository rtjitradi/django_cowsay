# Generated by Django 3.1 on 2020-08-19 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cowchat_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textline',
            name='text_line',
            field=models.CharField(max_length=110),
        ),
    ]