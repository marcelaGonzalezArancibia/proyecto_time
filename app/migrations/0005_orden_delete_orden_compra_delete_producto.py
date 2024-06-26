# Generated by Django 4.2.6 on 2024-06-05 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_orden_compra_telefono_cliente_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='orden',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombrevendedor', models.CharField(max_length=90)),
                ('rutvendedor', models.CharField(max_length=9)),
                ('nombreempresa', models.CharField(max_length=90)),
                ('direccionv', models.CharField(max_length=90)),
                ('correovendedor', models.CharField(max_length=90)),
                ('nombrecliente', models.CharField(max_length=90)),
                ('rutcliente', models.CharField(max_length=9)),
                ('direccioncliente', models.CharField(max_length=90)),
                ('correo', models.CharField(max_length=90)),
                ('telefono', models.IntegerField()),
                ('producto', models.CharField(max_length=90)),
                ('descripcion', models.TextField()),
                ('cantidad', models.IntegerField()),
                ('preciounidad', models.IntegerField()),
                ('sumatotal', models.IntegerField()),
                ('iva', models.IntegerField()),
                ('valorenvio', models.IntegerField()),
                ('preciototal', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='orden_compra',
        ),
        migrations.DeleteModel(
            name='producto',
        ),
    ]
