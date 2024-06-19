from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from .models import Profile, Tweet, Follower
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    
    user = request.user
    following_users = Follower.objects.filter(follower_user=user).values_list('following_user', flat=True)
    tweets = Tweet.objects.filter(user__in=following_users).order_by('-date_time')
    
    return render(request, 'app/index.html', {
        'tweets': tweets
    })
        
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'app/login.html', {
                'message': 'Invalid Credentials'
            })
    
    return render(request, 'app/login.html') 
    
def logout_view(request):
    logout(request)
    return render(request, 'app/login.html', {
        'message': 'Logged out'
    })


def profile_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    user = request.user
    profile = Profile.objects.get(user=user)
    tweets = Tweet.objects.filter(user=user).order_by('-date_time')
    return render(request, 'app/profile.html', {
        'user': user,
        'profile': profile,
        'tweets': tweets
    })

    
def edit_profile_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    
    user = request.user 
    profile = Profile.objects.get(user = user)
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        gender = request.POST['gender']
        dob = request.POST['dob']
        bio = request.POST['bio']
        
        user.username = username 
        user.first_name = first_name
        user.last_name = last_name 
        user.email = email 
        user.save()
        
        profile.gender = gender
        profile.dob = dob 
        profile.bio = bio 
        profile.save()
        
        return redirect('profile')
        
    return render(request, 'app/edit_profile.html', {
        'user': user,
        'profile': profile
    })
    
import logging
logger = logging.getLogger(__name__)

def post_tweet_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    if request.method == 'POST':
        tweet_content = request.POST['tweet']
        
        Tweet.objects.create(
            tweet=tweet_content,
            user=request.user,
            date_time=timezone.now()
        )

        
        return redirect('profile')

    return render(request, 'app/post_tweet.html')

def delete_post_view(request, tweet_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    
    tweet = get_object_or_404(Tweet, id=tweet_id, user=request.user)
    tweet.delete()
    return redirect('profile')
        
def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password != confirm_password:
            return render(request, 'app/register.html', {
                'message': 'Password does not match'
            })
        
        try:
            user = User.objects.create_user(username, password)
            user.save()
            
            profile = Profile.objects.create(user=user)
            profile.save()
            
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        except:
            return render(request, 'app/register.html', {
                'message': 'Username already exists'
            })
        
    return render(request, 'app/register.html')
        