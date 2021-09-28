from django.db import models

class Tag(models.Model):
    tag = models.CharField(max_length=200)
    def __str__(self):

        return str(self.tag)
    
    
class Note(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    tag = models.ForeignKey(Tag, null=True, on_delete=models.SET_NULL)
    

    def __str__(self):
        return f"{self.id}. {self.title}"


    