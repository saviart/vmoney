from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    user_id = models.CharField(max_length=100, null=True)
    user_paypal= models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200, unique=True)
    user_name= models.CharField(max_length=100, null=True)
    user_coins = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    recommended_by = models.CharField(max_length=200,null=True)
    ref_code = models.CharField(max_length=200,unique=False,null=False)
    is_baned = models.BooleanField(default=False)
    avatar = models.CharField(max_length=200,null=True, unique=False)
    user_xp = models.IntegerField(default=0,null=True)


    def __str__(self):
        return self.username

