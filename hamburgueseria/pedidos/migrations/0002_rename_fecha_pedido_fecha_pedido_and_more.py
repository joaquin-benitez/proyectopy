# Generated by Django 5.1.3 on 2024-12-05 21:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0002_hamburguesa_imagen'),
        ('pedidos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='fecha',
            new_name='fecha_pedido',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='direccion',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='email',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='nombre_usuario',
        ),
        migrations.AddField(
            model_name='pedido',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='cantidad',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='hamburguesa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu_app.hamburguesa'),
        ),
    ]