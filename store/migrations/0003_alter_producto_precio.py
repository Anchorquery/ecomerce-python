# Generated by Django 3.2.12 on 2022-10-27 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]