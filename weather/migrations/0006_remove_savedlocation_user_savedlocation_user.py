# Generated by Django 4.1.7 on 2023-03-03 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0005_alter_user_managers_user_date_joined_user_is_active_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='savedlocation',
            name='user',
        ),
        migrations.AddField(
            model_name='savedlocation',
            name='user',
            field=models.ManyToManyField(to='weather.user'),
        ),
    ]
