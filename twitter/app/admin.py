from django.contrib import admin
from .models import Profile, Follower, Tweet, Reply, Like 
# Register your models here.

admin.site.register(Profile)
admin.site.register(Follower)
admin.site.register(Tweet)
admin.site.register(Reply)
admin.site.register(Like)