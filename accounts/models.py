from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, phone_number,email,other_name,user_type, password=None):
        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError('User must have an username')

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            other_name = other_name,
            phone_number=phone_number,
            user_type = user_type
        )
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, other_name, phone_number, user_type, email, username, password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
            other_name= other_name,
            phone_number= phone_number,
            user_type= user_type
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        
        user.save(using=self._db)
        return user



class User(AbstractBaseUser):
    first_name          = models.CharField(max_length=50)
    last_name           = models.CharField(max_length=50)
    other_name           = models.CharField(max_length=50,blank=True,null=True)
    username            = models.CharField(max_length=50, unique=True)
    email               = models.EmailField(max_length=100, unique=True)
    phone_number        = models.CharField(max_length=50)

    # required
    date_joined         = models.DateTimeField(auto_now_add=True)
    last_login          = models.DateTimeField(auto_now_add=True)
    is_admin            = models.BooleanField(default=False)
    is_staff            = models.BooleanField(default=False)
    is_active           = models.BooleanField(default=False)
    is_superadmin       = models.BooleanField(default=False)
    user_type_choices   = ((1,'is_meristaff'),
                            
                            
                            )
    user_type           = models.PositiveSmallIntegerField(choices = user_type_choices,blank=True,null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name','other_name','phone_number','user_type']

    objects = UserManager()

#custom user review name
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True
    
    