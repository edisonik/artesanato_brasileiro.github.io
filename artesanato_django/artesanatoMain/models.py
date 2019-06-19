# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models
class Pessoa(models.Model):
    nome = models.CharField(max_length=150, null=False,verbose_name='Nome da Pessoa')
    datanascimento = models.DateTimeField()
    nacionalidade = models.CharField(max_length=150)

    def __str__(self):
        return self.nome

class Artesao (models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pessoa)

class Historia(models.Model):
    texto = models.CharField(max_length=5000, null=False, verbose_name='História')
    artesao = models.ForeignKey(Artesao, on_delete=models.CASCADE)

    def __str__(self):
        return self.texto

class Tecnica(models.Model):
    nome = models.CharField(max_length=150, null=False, verbose_name='Nome da Técnica')
    artesao = models.ManyToManyField(Artesao)

    def __str__(self):
        return self.nome

class Tipo_Artesanato(models.Model):
    descricao = models.CharField(max_length=150, null=False, verbose_name='Tipo de Artesanato')
    artesao = models.ManyToManyField(Artesao)

    def __str__(self):
        return self.descricao

class Pergunta(models.Model):
    pergunta = models.CharField(max_length=250, null=False, verbose_name='Texto da Pergunta')
    tipoartesanato = models.ForeignKey(Tipo_Artesanato, on_delete=models.CASCADE)

    def __str__(self):
        return self.pergunta

class Resposta(models.Model):
    resposta = models.CharField(max_length=250, null=False, verbose_name='Texto da Resposta')
    pergunta = models.ManyToManyField(Pergunta)

    def __str__(self):
        return self.resposta
