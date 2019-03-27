from django.db import models
from django.contrib.auth.models import User
# Create your models here

class Profile(models.Model):
    profile_photo= models.CharField(max_length =60)
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

    def save_profile(self):
        self.save() 
    def delete_profile(self):
        self.delete() 
    def update_profile(self):
        self.update()           
    @classmethod
    def get_profile(cls):
        profiles = Profile.objects.all()
        return images
        
class Image(models.Model):
    image = models.ImageField(upload_to = 'instagram/')
    image_name = models.CharField(max_length =30)
    image_caption = models.CharField(max_length =30)
    comments= models.CharField(max_length =30)
    likes = models.CharField(max_length =30)
    user=models.ForeignKey(User)
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)

    def save_image(self):
        self.save() 
    def delete_image(self):
        self.delete() 
    def update_caption(self):
        self.update()           
    @classmethod
    def get_image(cls):
        images = Image.objects.all()
        return images





class Comment(models.Model):
    comments = models.TextField()
    image=models.ForeignKey(Image, on_delete=models.CASCADE)


    def save_comment(self):
        self.save() 
    def delete_comment(self):
        self.delete() 
     

   
class like(models.Model):
    like = models.CharField(max_length =30) 
    image=models.ForeignKey(Image, on_delete=models.CASCADE)

class Followers(models.Model):
    followers= models.ForeignKey(Profile,related_name='followers')
    followees=models.ForeignKey(Profile,related_name='followees')