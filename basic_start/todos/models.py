from django.db import models

# Create your models here.
class Todos(models.Model):
    title=models.CharField(name="title",max_length=70)
    isdone=models.BooleanField(name="isdone",default=False)

    def __str__(self):
        return f"{self.title} is {"completed" if self.isdone==True else "not completed"}"