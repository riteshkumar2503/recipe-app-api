# Generated by Django 2.1.15 on 2021-08-29 20:38

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customusermodel111',
            managers=[
                ('objects123', django.db.models.manager.Manager()),
            ],
        ),
    ]
