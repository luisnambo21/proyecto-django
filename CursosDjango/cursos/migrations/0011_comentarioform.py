# Generated by Django 3.2.4 on 2021-07-30 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0010_alter_comentario_coment'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComentarioForm',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Clave')),
                ('nombre', models.TextField(verbose_name='Usuario')),
                ('correo', models.TextField(verbose_name='Correo')),
                ('mensaje', models.TextField(verbose_name='Comentario')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Registrado')),
            ],
            options={
                'verbose_name': 'Comentario Formulario',
                'verbose_name_plural': 'Comentarios Formularios',
                'ordering': ['-created'],
            },
        ),
    ]