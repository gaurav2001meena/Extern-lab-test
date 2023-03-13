from django.db import models

# Create your models here.

class Userinfo(models.Model):
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    name = models.CharField( max_length=50)
    phone = models.CharField(max_length=12)
    
    def __str__(self):
      return self.email
    
    
    
class Document(models.Model):
    email = models.ForeignKey(Userinfo , on_delete=models.CASCADE , null=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    img = models.ImageField(upload_to="notes\img" , null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)