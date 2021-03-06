# Generated by Django 2.2.14 on 2020-11-29 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('materias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('edad', models.IntegerField()),
                ('clases', models.ManyToManyField(related_name='estudiantes', to='materias.Materia')),
            ],
        ),
    ]
