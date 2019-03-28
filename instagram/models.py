from django.db import models
from django.contrib.auth.models import User
# Create your models here

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30,null=True)
    last_name = models.CharField(max_length=30,null=True)
    prof_image = models.ImageField(upload_to = 'images/',null=True)
    bio = models.CharField(max_length =200)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profile(cls):
        profiles = cls.objects.all()
        return profiles

    @classmethod
    def search_by_username(cls,search_term):
        profiles = cls.objects.filter(first_name__icontains=search_term)
        return profiles

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length =30)
    image_caption = models.CharField(max_length =30)
    comments= models.CharField(max_length =30)
    likes = models.CharField(max_length =30)
    user=models.ForeignKey(User)
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE, null=True)

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
    comments = models.CharField(max_length =30)
    image=models.ForeignKey(Image, on_delete=models.CASCADE)


    def save_comment(self):
        self.save() 
    def delete_comment(self):
        self.delete() 
    @classmethod
    def get_comment(cls):
        comments = Comment.objects.all()
        return comments


   
class like(models.Model):
    like = models.CharField(max_length =30) 
    image=models.ForeignKey(Image, on_delete=models.CASCADE)

class Followers(models.Model):
    followers= models.ForeignKey(Profile,related_name='followers')
    followees=models.ForeignKey(Profile,related_name='followees')