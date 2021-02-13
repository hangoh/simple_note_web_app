from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
# Create your models here.
class AccontManager(BaseUserManager):
    def create_user(self,username,email,password=None):
        if not email:
            raise ValueError('email is required')
        if not username:
            raise ValueError('username is required')
        user=self.model(
            username=username,
            email=email,
            
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username,email,password=None):
        user=self.create_user(
            username=username,
            email=email,
            password=password
        )
        user.is_admin=True
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email=models.EmailField(max_length=60,unique=True,verbose_name='email')
    username = models.CharField(max_length=60)
    date_joined=models.DateField(auto_now_add=True)
    last_login=models.DateField(auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']

    objects=AccontManager()

    def __str__(self):
        return self.username
    
    def has_module_perms(self,app_lable):
        return True
    
    def has_perm(self,perm,obj=None):
        return self.is_admin