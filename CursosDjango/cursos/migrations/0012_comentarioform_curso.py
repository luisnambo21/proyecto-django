# Generated by Django 3.2.4 on 2021-08-04 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0011_comentarioform'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentarioform',
            name='curso',
            field=models.TextField(default=2, verbose_name='Curso'),
            preserve_default=False,
        ),
    ]