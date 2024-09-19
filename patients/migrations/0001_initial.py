# Generated by Django 5.1.1 on 2024-09-17 22:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='Nome completo')),
                ('profession', models.CharField(max_length=100, verbose_name='Profissão')),
                ('address', models.CharField(max_length=200, verbose_name='Endereço')),
                ('city', models.CharField(max_length=200, verbose_name='Cidade')),
                ('state', models.CharField(max_length=50, verbose_name='Estado')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('phone', models.CharField(max_length=15, verbose_name='Telefone')),
                ('social_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome Social (opcional)')),
            ],
        ),
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('patient_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_fullname', to='patients.patient')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
