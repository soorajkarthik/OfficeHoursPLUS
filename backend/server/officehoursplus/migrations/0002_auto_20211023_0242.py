# Generated by Django 3.2.8 on 2021-10-23 06:42

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('officehoursplus', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='classonlineusers',
            unique_together={('user_id', 'class_id')},
        ),
        migrations.AlterUniqueTogether(
            name='usermentorassociations',
            unique_together={('user_id', 'class_id')},
        ),
    ]