from django.db import models

# Create your models here.
class Services(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='services-images/', blank=True, null=True)
    icon = models.ImageField(upload_to='services-icons/', blank=True, null=True)
    
    def __str__(self):
        return self.title