# Generated by Django 2.2.4 on 2019-09-04 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20190723_1444'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-created', 'name'), 'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
    ]
