# Generated by Django 5.1.7 on 2025-04-11 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_number', models.CharField(max_length=50, unique=True, verbose_name='零件号')),
                ('name', models.CharField(max_length=100, verbose_name='品名')),
                ('unit', models.CharField(max_length=20, verbose_name='单位')),
                ('drawing_number', models.CharField(max_length=50, verbose_name='图号')),
                ('spec1', models.CharField(blank=True, max_length=50, verbose_name='规格1')),
                ('spec2', models.CharField(blank=True, max_length=50, verbose_name='规格2')),
                ('spec3', models.CharField(blank=True, max_length=50, verbose_name='规格3')),
                ('spec4', models.CharField(blank=True, max_length=50, verbose_name='规格4')),
                ('spec5', models.CharField(blank=True, max_length=50, verbose_name='规格5')),
                ('spec6', models.CharField(blank=True, max_length=50, verbose_name='规格6')),
                ('spec7', models.CharField(blank=True, max_length=50, verbose_name='规格7')),
                ('spec8', models.CharField(blank=True, max_length=50, verbose_name='规格8')),
                ('spec9', models.CharField(blank=True, max_length=50, verbose_name='规格9')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='价格')),
            ],
        ),
    ]
