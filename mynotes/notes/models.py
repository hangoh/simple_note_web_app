from django.db import models
from django.contrib.auth import settings
# Create your models here.
class NotesList(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    name=models.CharField(max_length=400,null=False,blank=False)
    def __str__(self):
        return self.name
    
    

class Notes(models.Model):
    title=models.CharField(max_length=400,null=False,blank=False)
    description=models.TextField(null=True,blank=True)
    under_notelist=models.ForeignKey(NotesList, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
