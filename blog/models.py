from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

    class Meta: 
        abstract = True


# Create your models here.
class Post(TimestampedModel):
    title = models.CharField(max_length=255)
    body = models.TextField()
    

def __str__(self):
    return self.title