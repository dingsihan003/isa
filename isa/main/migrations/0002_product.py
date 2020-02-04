# Generated by Django 2.2.4 on 2020-02-04 16:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_title', models.CharField(max_length=200)),
                ('product_base_price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('product_description', models.TextField()),
                ('product_date_added', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('sold', models.BooleanField(default=False)),
            ],
        ),
    ]
