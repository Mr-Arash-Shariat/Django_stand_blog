# Generated by Django 3.2 on 2022-04-17 12:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20220417_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]