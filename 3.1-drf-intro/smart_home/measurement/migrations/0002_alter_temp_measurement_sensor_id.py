# Generated by Django 4.1.3 on 2022-12-26 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temp_measurement',
            name='sensor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='measurement.sensor'),
        ),
    ]
