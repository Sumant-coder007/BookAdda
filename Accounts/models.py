from django.db import models
from django.contrib.auth.models import User 
from PIL import Image
class Profile(models.Model):

    user=models.OneToOneField(User, on_delete = models.CASCADE)
    image=models.ImageField(default='default.jpg', upload_to='profile_pics')
    

    def __str__(self):
        return f'{self.user.username} Profile'
    def save(self,force_insert=False, force_update=False,using=None,update_fields=None):
        super().save(force_insert ,force_update,using,update_fields)
        img = Image.open(self.image.path)
        if img.height >150 and img.width > 150:
            output_size= (150,150)
            img.thumbnail(output_size)
            img.save(self.image.path)
class Book(models.Model):
    img =models.ImageField(upload_to='pics')
    name = models.CharField(max_length=100) 
    desc = models.TextField()
    link = models.TextField()