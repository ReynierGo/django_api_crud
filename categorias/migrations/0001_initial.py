# Generated by Django 4.1.2 on 2022-10-24 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateField(auto_created=True)),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
            ],
        ),
    ]