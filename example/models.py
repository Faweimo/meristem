from django.db import models
from django.urls import reverse
# Create your models here.

class Client(models.Model):
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)

    class Meta:
        verbose_name = ("Client")
        verbose_name_plural =("Clients")

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse("client_detail", kwargs={"pk": self.pk})
