# Generated by Django 3.2.4 on 2021-07-30 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0007_rename_curso_cursos_materia'),
    ]

    operations = [
        migrations.AddField(
            model_name='cursos',
            name='turno',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]
