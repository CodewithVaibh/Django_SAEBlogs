from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime,date

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=120)
    author=models.CharField(max_length=120)
    body=models.TextField()
    post_date=models.DateField(auto_now_add=True)
    
    def __str__(self) :
        return self.title + " by " + str(self.author)
    
    def get_absolute_url(self):
        return reverse("postview", kwargs={"pk": self.pk})
    
    
    

    
