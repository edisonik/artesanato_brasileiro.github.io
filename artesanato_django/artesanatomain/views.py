# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
from haystack.generic_views import SearchView

# Create your views here.
def indexView(request):
    # função pra pegar dados do banco
    tecnicas = Tecnica.objects.all()
    context = {'posts':
                [
                    {'titulo': 'Post #1', 'conteudo': 'asdfghjklç', 'img': 'https://http2.mlstatic.com/artesanato-do-piaui-ilha-santa-isabel-em-palha-de-carnauba-D_NQ_NP_724041-MLB27111520895_042018-F.jpg', 'id': '1'},
                    {'titulo': 'Post #2', 'conteudo': 'zxcvbnm', 'img': '', 'id' : '2'}
                ],
                'tecnicas':tecnicas
            }
    return render(request, 'artesanatoMain/index.html', context)

def historiaView(request, historia_id):
    tecnicas = Tecnica.objects.all()
    historia = get_object_or_404(Historia, pk=historia_id)
    # artesao = get_object_or_404(Artesao, pk=historia.artesao_id)
    pessoa = get_object_or_404(Pessoa, pk=historia.artesao.pessoa_id)
    context={'historia':historia, 'nome':pessoa.nome, 'tecnicas': tecnicas}
    return render(request, 'artesanatoMain/historia.html', context)

def tecnicaView(request, tecnica_id):
    tecnicas = Tecnica.objects.all()

    tecnica = get_object_or_404(Tecnica, pk=tecnica_id)
    context={'tecnica':tecnica, 'tecnicas': tecnicas}
    print(tecnica.nome, tecnica.descricao)
    return render(request, 'artesanatoMain/tecnica.html', context)

def descubraView(request):
    context={}
    return render(request, 'artesanatoMain/descubra.html', context)

    