# Generated by Django 2.2.7 on 2019-11-25 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('F1Cont', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=300)),
                ('Fecha_Creacion', models.DateField()),
                ('Presupuesto', models.IntegerField()),
                ('Pais_Origen', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Neumaticos',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=300)),
                ('Tipo', models.CharField(choices=[('Blandos', 'Blandos'), ('Duros', 'Duros'), ('Lluvia', 'Lluvia'), ('Extremos', 'Extremos')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Suministrador',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=300)),
                ('Pais', models.CharField(max_length=300)),
                ('Cilindrada', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Piloto',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=300)),
                ('Apellido', models.CharField(max_length=300)),
                ('Numero', models.PositiveIntegerField()),
                ('Id_Agente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='F1Cont.Agente')),
                ('Id_Escuderia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='F1Cont.Equipo')),
            ],
        ),
        migrations.CreateModel(
            name='Patrocinador',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=300)),
                ('EsPrincipal', models.BooleanField()),
                ('EscuderiaAsig', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='F1Cont.Equipo')),
            ],
        ),
        migrations.AddField(
            model_name='equipo',
            name='Motor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='F1Cont.Suministrador'),
        ),
        migrations.CreateModel(
            name='Circuito',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=300)),
                ('Ciudad', models.CharField(max_length=300)),
                ('Pais', models.CharField(max_length=100)),
                ('Longitud', models.IntegerField()),
                ('Id_Serie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='F1Cont.Serie')),
            ],
        ),
    ]