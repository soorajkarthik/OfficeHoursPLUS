# Generated by Django 3.2.8 on 2021-10-23 18:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('officehoursplus', '0005_usermentorassociations_creation_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassUserHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_joined', models.DateTimeField(auto_now_add=True)),
                ('time_left', models.DateTimeField()),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='officehoursplus.classes')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='ClassOnlineUsers',
        ),
    ]