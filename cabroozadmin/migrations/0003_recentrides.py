# Generated by Django 3.1.6 on 2021-07-01 09:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cabroozadmin', '0002_auto_20210630_2143'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecentRides',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('details', models.TextField()),
                ('time', models.TimeField(auto_now_add=True)),
                ('action', models.CharField(blank=True, max_length=255, null=True)),
                ('totalusers', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]