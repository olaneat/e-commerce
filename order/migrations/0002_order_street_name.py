# Generated by Django 2.2.3 on 2019-08-01 23:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='street_name',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
