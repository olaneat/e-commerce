from django.db import models
from django.contrib.auth.models import User
from django,db.models.signals import post_save
from django.dispatch import reciever

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirm = models.BooleanField(defaualt = False)
    picture = models.ImageField(upload_to = 'media/profile', blank = True)

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user = instance)
        instance.profile.save()