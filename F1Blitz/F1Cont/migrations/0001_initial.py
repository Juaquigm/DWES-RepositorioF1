# Generated by Django 2.2.7 on 2019-11-25 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agente',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=150)),
                ('Apellidos', models.CharField(max_length=300)),
                ('Pais', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=300)),
                ('Localizacion', models.CharField(max_length=50)),
            ],
        ),
    ]
