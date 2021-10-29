from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
import cloudinary
from cloudinary.models import CloudinaryField

# Create your models here.

class Neighbourhood(models.Model):
    name = models.CharField(max_length=50)
    location= models.CharField(max_length=60)
    admin = models.ForeignKey("Profile",on_delete=models.CASCADE, related_name = 'hood')
    description = models.TextField( default = '')
    hood_photo =cloudinary.models.CloudinaryField('photo', default='photo')
    emergency_contact=models.CharField(max_length=100,null=True, blank=True)
    occupants_count = models.IntegerField(null  = True ,blank = True)
    

    def __str__(self):
        return f'{self.name} neighbourhood'


    def save_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()
        
        
    @classmethod
    def find_hood(cls, hood_id):
        return cls.objects.filter(id=hood_id)

    @property
    def occupants_count(self):
        return self.neighbourhood_users.count()

    def update_hood(self):
        hood_name = self.hood_name
        self.hood_name = hood_name    


class Profile(models.Model):
    username = models.CharField(max_length=100, blank =True )
    bio = models.TextField(max_length=300,blank =True)
    user = models.OneToOneField(User, on_delete = models.CASCADE , related_name='profile')
    email = models.CharField(max_length=100, default = '')
    location = models.CharField(max_length=100,blank =True)
    profile_pic = cloudinary.models.CloudinaryField('profile', default='photo')
    neighbourhood = models.ForeignKey(
        Neighbourhood, on_delete=models.CASCADE, default='', null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save_profile(self):
        self.save
    
    def delete_user(self):
        self.delete()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):

    if created:
        Profile.objects.create(user=instance)
        
        

        
        
class Business(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default = '')
    image = cloudinary.models.CloudinaryField('images', default='photo')
    email = models.CharField(max_length=100, default = '')
    description = models.TextField( default = '')
    neighbourhood = models.ForeignKey("Neighbourhood",on_delete=models.CASCADE, default='', null=True, blank=True)
    



    def __str__(self):
        return f'{self.name} business'


    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def hood_business(cls, id):
        hoodbusiness = Business.objects.filter(neighbourhood = id)
        return hoodbusiness
    
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,default = '')
    date = models.DateField(auto_now_add=True)
    neighbourhood = models.ForeignKey("Neighbourhood",on_delete=models.CASCADE, default='', null=True, blank=True)
    

    @classmethod
    def hood_post(cls,id):
        hoodpost = Post.objects.filter(neighbourhood = id)
        return hoodpost
    
    def __str__(self):
        return f'{self.title} Post'

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()
        
