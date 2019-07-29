# Generated by Django 2.2.3 on 2019-07-29 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0004_auto_20190723_1444'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('surname', models.CharField(max_length=150)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('paid', models.BooleanField(default=False)),
                ('created', models.DateTimeField()),
                ('address', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('item_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='order.Order')),
                ('product_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='shop.Product')),
            ],
        ),
    ]