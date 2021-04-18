from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    bio = models.TextField(max_length=500, blank=True, default='my bio')
    profileImg = models.ImageField('profy', default='a.png')

    def  __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.Profile.post_save()


class Post(models.Model):
    image = models.ImageField(upload_to='posty')
    name = models.CharField(max_length=40, blank=True)
    caption = models.CharField(max_length=250, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, related_name='posts')
    likes = models.ManyToManyField(User, related_name='likes', blank=True)


    def __str__(self):
        return self.name

    
    class Meta:
        ordering = ['-pk']

    


