# Generated by Django 3.1.7 on 2021-05-15 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_boletos_descuento'),
    ]

    operations = [
        migrations.AddField(
            model_name='boletos',
            name='Valor',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True),
        ),
    ]
