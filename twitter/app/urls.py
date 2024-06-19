from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('profile', views.profile_view, name='profile'),
    path('profile/edit', views.edit_profile_view, name='edit_profile'),
    path('post', views.post_tweet_view, name="post_tweet"),
    path('post/delete/<int:tweet_id>', views.delete_post_view, name="delete_post"),
    path('register', views.register_view, name="register")
]