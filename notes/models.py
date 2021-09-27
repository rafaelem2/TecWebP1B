from django.db import models

class Tag(models.Model):
    tag = models.CharField(max_length=200)
    
    
class Note(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    

    def __str__(self):
        return f"{self.id}. {self.title}"


    