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
    path('register', views.register_view, name="register"),
    path('all_users/', views.all_users_view, name='all_users'),
    path('follow_user/<int:user_id>/', views.follow_user_view, name='follow_user'),
    path('following/', views.following_users_view, name='following_users'),
    path('followers/', views.follower_users_view, name='follower_users'),
    path('like_unlike/<int:tweet_id>/', views.like_unlike_tweet, name='like_unlike'),
    path('view_comments/<int:tweet_id>/', views.view_add_comments, name='view_comments'),
    path('user/<int:user_id>/', views.user_detail_view, name='user_detail'),
] 