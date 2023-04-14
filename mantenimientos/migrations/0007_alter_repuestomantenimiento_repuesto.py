# Generated by Django 4.1.7 on 2023-04-06 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repuestos', '0002_alter_repuesto_options'),
        ('mantenimientos', '0006_rename_delete_repuestomantenimiento_eliminado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repuestomantenimiento',
            name='repuesto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mantenimientos', to='repuestos.repuesto'),
        ),
    ]