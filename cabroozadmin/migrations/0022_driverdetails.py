# Generated by Django 3.1.6 on 2021-07-05 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cabroozadmin', '0021_delete_driverdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='DriverDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drivername', models.CharField(blank=True, max_length=65, null=True)),
                ('country', models.CharField(blank=True, max_length=65, null=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('gender', models.CharField(blank=True, max_length=65, null=True)),
                ('referal', models.CharField(blank=True, max_length=255, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('cnicfront', models.ImageField(blank=True, null=True, upload_to='')),
                ('cnicback', models.ImageField(blank=True, null=True, upload_to='')),
                ('driverslicensefront', models.ImageField(blank=True, null=True, upload_to='')),
                ('driverslicenseback', models.ImageField(blank=True, null=True, upload_to='')),
                ('vehicle', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('time', models.DateField(auto_now_add=True)),
                ('wallet', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cabroozadmin.user')),
            ],
        ),
    ]
