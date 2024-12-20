# Generated by Django 5.1.2 on 2024-11-10 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_tipotratamiento_tratamientos_tipo_tratamiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='citas',
            name='comentarios',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='citas',
            name='servicio',
            field=models.CharField(choices=[('Consulta médica', 'Consulta médica'), ('Asesoría', 'Asesoría'), ('Revisión', 'Revisión'), ('Otro', 'Otro')], default='Consulta médica', max_length=50),
        ),
        migrations.AlterField(
            model_name='citas',
            name='descripcion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='citas',
            name='fecha',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='citas',
            name='hora',
            field=models.TimeField(),
        ),
    ]
