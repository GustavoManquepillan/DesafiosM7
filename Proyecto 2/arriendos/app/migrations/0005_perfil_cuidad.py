# Generated by Django 4.2 on 2024-06-05 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_perfil_tipo_usuario_alter_inmueble_numero_banos_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='cuidad',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
