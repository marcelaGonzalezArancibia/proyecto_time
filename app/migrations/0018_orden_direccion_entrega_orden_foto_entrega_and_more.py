# Generated by Django 4.2.6 on 2024-06-14 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_alter_orden_estado_alter_orden_estadoentrega'),
    ]

    operations = [
        migrations.AddField(
            model_name='orden',
            name='direccion_entrega',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='orden',
            name='foto_entrega',
            field=models.ImageField(blank=True, null=True, upload_to='fotos_entrega/'),
        ),
        migrations.AddField(
            model_name='orden',
            name='motivo_rechazo',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='orden',
            name='rut_receptor',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
