# Generated by Django 5.0.7 on 2024-07-14 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataManager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DescuentoProducto',
            fields=[
                ('id_dcto', models.SmallAutoField(primary_key=True, serialize=False)),
                ('porc_dcto', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'descuento_producto',
                'managed': False,
            },
        ),
    ]