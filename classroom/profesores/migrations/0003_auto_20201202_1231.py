# Generated by Django 2.2.14 on 2020-12-02 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profesores', '0002_auto_20201129_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesor',
            name='clase',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='materias.Materia'),
        ),
    ]
