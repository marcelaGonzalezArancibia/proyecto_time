# Generated by Django 4.2.6 on 2024-06-14 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_orden_direccion_entrega_orden_foto_entrega_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RechazoHistorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.TextField()),
                ('orden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rechazos', to='app.orden')),
            ],
        ),
    ]
