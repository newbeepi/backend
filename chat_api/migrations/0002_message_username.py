# Generated by Django 4.1.4 on 2022-12-23 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='username',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
