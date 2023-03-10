# Generated by Django 4.1.6 on 2023-02-08 23:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('escritorio', '0002_cliente_advogado_alter_advogado_numero_oab_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='advogado',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='advogado',
            name='telefone',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='cliente',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='advogado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clientes', to='escritorio.advogado'),
        ),
    ]
