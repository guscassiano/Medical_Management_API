from django.db import models

# Create your models here.

class Patient(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='Nome completo')
    profession = models.CharField(max_length=100, verbose_name='Profissão')
    address = models.CharField(max_length=200, verbose_name='Endereço')
    city = models.CharField(max_length=200, verbose_name='Cidade')
    state = models.CharField(max_length=50, verbose_name='Estado')
    email = models.EmailField(max_length=100, verbose_name='Email')
    phone = models.CharField(max_length=15, verbose_name='Telefone')
    social_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Nome Social (opcional)')

    def __str__(self):
        return self.full_name

class Consultation(models.Model):
    id = models.AutoField(primary_key=True)
    patient_name = models.ForeignKey(Patient, related_name='Paciente', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
    consultation_data = models.DateTimeField(verbose_name='Data da consulta')

    class Meta:
        ordering = ['consultation_data']

    def __int__(self):
        return self.consultation_data