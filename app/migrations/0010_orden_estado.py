# Generated by Django 4.2.6 on 2024-06-14 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_rename_totalproducto_productoorden_totalproducto'),
    ]

    operations = [
        migrations.AddField(
            model_name='orden',
            name='estado',
            field=models.CharField(choices=[('creada', 'creada'), ('rectificada', 'Rectificada')], default='creada', max_length=20),
        ),
    ]