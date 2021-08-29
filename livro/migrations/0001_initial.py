# Generated by Django 3.2.6 on 2021-08-29 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=30)),
                ('co_autor', models.CharField(max_length=30)),
                ('data_cadastro', models.DateField()),
                ('emprestado', models.BooleanField(default=False)),
                ('nome_emprestado', models.CharField(max_length=30)),
                ('data_emprestimo', models.DateTimeField()),
                ('data_devolucao', models.DateTimeField()),
                ('tempo_devolucao', models.DateField()),
            ],
        ),
    ]
