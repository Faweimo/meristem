from django.db import models
from accounts.models import User
# Create your models here.

class Staff(models.Model):
    
    user                        = models.OneToOneField(User,on_delete=models.CASCADE)
    created_at                  = models.DateTimeField(auto_now_add=True)
    updated_at                  = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("staff")
        verbose_name_plural = ("staffs")

    def __str__(self):
        return str(self.user)

    # def get_absolute_url(self):
    #     return reverse("staff_detail", kwargs={"pk": self.pk})
