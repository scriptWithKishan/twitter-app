from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    dob = models.DateField(default=date.today)
    bio = models.TextField(default='', blank=True, null=True)

    def __str__(self):
        return self.user.username
    
class Follower(models.Model):
    follower_user = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    following_user = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    

class Tweet(models.Model):
    tweet = models.TextField(default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    image = models.ImageField(upload_to='tweet_images/', blank=True, null=True)
    
class Reply(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    reply = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    
class Like(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    
