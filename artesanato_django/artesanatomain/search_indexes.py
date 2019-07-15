from .models import *
from haystack import indexes
from django.forms.models import model_to_dict

class PerguntaIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True,use_template=True)
    pergunta = indexes.EdgeNgramField(model_attr='pergunta')
    
    def get_model(self):
        return Pergunta
    
    def index_queryset(self, using=None):
        return self.get_model().objects.all()

class RespostaIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    resposta = indexes.EdgeNgramField(model_attr='resposta')
    pergunta = indexes.EdgeNgramField(model_attr='pergunta')

    def get_model(self):
        return Resposta
    
    def index_queryset(self, using=None):
        return self.get_model().objects.all()

class PessoaIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    nome = indexes.EdgeNgramField(model_attr='nome')
    data_nascimento = indexes.EdgeNgramField(model_attr='datanascimento')
    nacionalidade = indexes.EdgeNgramField(model_attr='nacionalidade')

    def get_model(self):
        return Pessoa
    
    def index_queryset(self, using=None):
        return self.get_model().objects.all()

class ArtesaoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    pessoa = indexes.EdgeNgramField(model_attr='pessoa')

    def get_model(self):
        return Artesao
    
    def index_queryset(self, using=None):
        return self.get_model().objects.all()

class HistoriaIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    texto = indexes.EdgeNgramField(model_attr='texto')
    artesao = indexes.EdgeNgramField(model_attr='artesao')

    def get_model(self):
        return Historia
    
    def index_queryset(self, using=None):
        return self.get_model().objects.all()

class TecnicaIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    artesao = indexes.EdgeNgramField(model_attr='artesao')

    def get_model(self):
        return Tecnica
    
    def index_queryset(self, using=None):
        return self.get_model().objects.all()

class Tipo_ArtesanatoIndex(indexes.SearchIndex, indexes. Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    descricao = indexes.EdgeNgramField(model_attr='descricao')
    artesao = indexes.EdgeNgramField(model_attr='artesao')

    def get_model(self):
        return Tipo_Artesanato
    
    def index_queryset(self, using=None):
        return self.get_model().objects.all()

