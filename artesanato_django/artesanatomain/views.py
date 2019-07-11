# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404

# Create your views here.
def indexView(request):
    # função pra pegar dados do banco
    context = {'posts':
                [
                    {'titulo': 'Post #1', 'conteudo': 'asdfghjklç', 'img': 'https://http2.mlstatic.com/artesanato-do-piaui-ilha-santa-isabel-em-palha-de-carnauba-D_NQ_NP_724041-MLB27111520895_042018-F.jpg'},
                    {'titulo': 'Post #2', 'conteudo': 'zxcvbnm', 'img': ''}
                ]
            }
    return render(request, 'artesanatoMain/index.html', context)

def historiaView(request, historia_id):
    historia = get_object_or_404(Historia, pk=historia_id)
    context={'historia':historia}
    return render(request, 'artesanatoMain/historia.html', context)

def tecnicaView(request, tecnica_id):
    tecnica = get_object_or_404(Tecnica, pk=tecnica_id)
    context={'tecnica':tecnica}
    return render(request, 'artesanatoMain/tecnica.html', context)
