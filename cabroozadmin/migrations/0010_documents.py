# Generated by Django 3.1.6 on 2021-07-02 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cabroozadmin', '0009_servicetypes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promocode', models.CharField(blank=True, max_length=255, null=True)),
                ('discount', models.IntegerField(blank=True, null=True)),
                ('expiration', models.DateField(auto_now_add=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('usercount', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cabroozadmin.user')),
            ],
        ),
    ]
