from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from .models import Profile
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        # When user created create a profile
        Profile.objects.create(user=user, email=user.email)
        print('Profile created!')
    else:
        # Update user email if it has been changed e.g. in the admin
        profile = get_object_or_404(Profile, user=user)
        profile.email = user.email
        profile.save()


@receiver(post_save, sender=Profile)
def update_user(sender, instance, created, **kwargs):
    profile = instance
    if created == False:
        user = get_object_or_404(User, id=profile.user.id)
        if user.email != profile.email:
            user.email = profile.email
            user.save()