# Generated by Django 3.2.16 on 2022-10-19 00:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Depto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('andar', models.IntegerField(verbose_name='Andar')),
                ('ramal', models.IntegerField(verbose_name='Ramal')),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
            },
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('sobrenome', models.CharField(max_length=70, verbose_name='Sobrenome')),
                ('funcao', models.CharField(choices=[('Contador', 'CONTADOR'), ('Administrador', 'ADMINISTRADOR'), ('Economista', 'ECONOMISTA'), ('Outros', 'OUTROS')], max_length=13, verbose_name='Função')),
                ('depto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.depto', verbose_name='funcionarios')),
            ],
            options={
                'verbose_name': 'Funcionário',
                'verbose_name_plural': 'Funcionários',
                'ordering': ['depto', 'nome'],
            },
        ),
    ]
