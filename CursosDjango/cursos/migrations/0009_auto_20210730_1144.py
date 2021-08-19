# Generated by Django 3.2.4 on 2021-07-30 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0008_cursos_turno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursos',
            name='turno',
            field=models.TextField(verbose_name='Turno'),
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Clave')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Registrado')),
                ('coment', models.TextField(verbose_name='Comentario')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.cursos', verbose_name='Materia')),
            ],
            options={
                'verbose_name': 'Comentario',
                'verbose_name_plural': 'Comentarios',
                'ordering': ['-created'],
            },
        ),
    ]
