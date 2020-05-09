from django.db import models

# Create your models here.
class Dolphin(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=50)
    info = models.TextField()

    def __str__(self):
        return self.name

class Vote(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, editable=False)
    date = models.DateField(auto_now=True)
    recipient = models.ForeignKey(Dolphin, on_delete=False)

    def __str__(self):
        return "Vote for " + self.recipient.name