class Answer:
    
    def __init__(self,answer,value):
        self._answer = answer
        self._value = value

    def __str__(self):
        return "Resposta: " + self.Answer + '\n' + "Peso: " + str(self.Value)
    
    @property
    def Answer(self):
        return self._answer
    
    @property
    def Value(self):
        return self._value

