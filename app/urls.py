from django.urls import path
from .views import *
from app.views import PostLikeToggle, PostLikeAPIToggle


urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup , name='signup'),
    path('profile/<username>/', profile, name='profile'),
    path('user_profile/<username>/', user_profile, name='user_profile'),
    path('follow/<pk>', follow, name='follow'),
    path('unfollow/<pk>',unfollow, name='unfollow'),
    path('post/<pk>', comment, name='comment'),
    path('post/<id>/like', PostLikeToggle.as_view(), name='liked'),
    path('api/post/<id>/like', PostLikeAPIToggle.as_view(), name='liked-api'),
    
]