import uuid
from django.db import models

class Word(models.Model):
    word=models.CharField(max_length=128)
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)

    def __str__(self):
        return self.word

class Wordmeanig(models.Model):
     id=models.UUIDField(default=uuid.uuid4,primary_key=True)
     word=models.ForeignKey('web.Word',max_length=128, on_delete=models.CASCADE)
     Wordmeanig=models.CharField(max_length=128)
     priority=models.IntegerField(null=True)


     def __str__(self):
        return self.Wordmeanig
