# Generated by Django 5.0 on 2023-12-14 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]