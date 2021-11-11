from .models import  User
from django.db.models.signals import post_save
from django.dispatch import receiver
from meristaff.models import Staff
@receiver(post_save, sender=User)        
def create_user_profile(sender,instance,created,**kwargs):
  
    if created:
        if instance.user_type==1:
            Staff.objects.create(user=instance)
            

@receiver(post_save, sender=User)        
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.staff.save()            
            