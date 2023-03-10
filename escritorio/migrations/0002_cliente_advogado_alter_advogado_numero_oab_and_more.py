# Generated by Django 4.1.6 on 2023-02-08 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('escritorio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='advogado',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='escritorio.advogado'),
        ),
        migrations.AlterField(
            model_name='advogado',
            name='numero_oab',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='endereco',
            field=models.CharField(max_length=250),
        ),
    ]
