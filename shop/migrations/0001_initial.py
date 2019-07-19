# Generated by Django 2.2.3 on 2019-07-18 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150)),
                ('slug', models.SlugField(max_length=150)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150)),
                ('slug', models.SlugField(max_length=150)),
                ('description', models.TextField()),
                ('available', models.BooleanField(default=True)),
                ('meta_description', models.CharField(max_length=150)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.IntegerField()),
                ('image', models.ImageField(upload_to='media/img')),
                ('created', models.DateField()),
                ('category', models.ForeignKey(on_delete='models.CASCADE', to='shop.Category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ('created',),
                'index_together': {('id', 'slug')},
            },
        ),
    ]
