from .models import *
from haystack import indexes

class PerguntaIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True,use_template=True)
    pergunta = indexes.CharField(model_attr='pergunta')
    
    def get_model(self):
        return Pergunta
    
    def index_queryset(self, using=None):
        return self.get_model().objects.all()