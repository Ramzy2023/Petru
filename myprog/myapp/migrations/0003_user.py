# Generated by Django 5.1.3 on 2024-11-09 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_travelorder_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100, verbose_name='Username')),
                ('password', models.CharField(max_length=100, verbose_name='Password')),
                ('user_type', models.CharField(max_length=100)),
            ],
        ),
    ]