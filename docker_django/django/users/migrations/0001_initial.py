# Generated by Django 3.1.7 on 2021-05-12 23:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CITAS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=30)),
                ('Edad', models.IntegerField(blank=True, null=True)),
                ('Peso', models.DecimalField(blank=True, decimal_places=15, max_digits=30, null=True)),
                ('Altura', models.DecimalField(blank=True, decimal_places=15, max_digits=30, null=True)),
                ('Fecha', models.DateField(blank=True, null=True)),
                ('Hora', models.TimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=10)),
                ('userImage', models.ImageField(blank=True, null=True, upload_to='users/pictures')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
