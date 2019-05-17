from Answer import Answer

class Question:
    
    def __init__(self,question):
        self._question = question 
        self._answers = []

    def __str__(self):
        return "Pergunta: " + self.Question + '\n' + "Possíveis respostas: " + str(self.Answer)

    @property 
    def Question(self):
        return self._question
    
    @property
    def Answer(self):
        return self._answers

    def setAnswer(self,text,value):
        ans = Answer(text,value)
        self._answers.append(ans)
    
