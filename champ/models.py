from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from accounts.models import CustomUser
# Create your models here.

class champ(models.Model):
    champ=models.CharField(max_length=255)
    owner=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    champ_type=models.CharField(max_length=255)
    description=models.TextField(default='description')
    img_url=models.TextField(default='NO image available!')


    def __str__(self):
        return self.champ
    
    def get_absolute_url(self):
        return reverse('champ_detail', args=[self.id])
