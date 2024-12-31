from django.db import models
import random, string
# Create your models here.


class UserType(models.Model):
    user_type = models.CharField(max_length=5, choices={
        ('0', 'Master'),
        ('1', 'Child'),
    })
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=11)
    password = models.CharField(max_length=255)

    is_angle = models.BooleanField(default=False)
    angle_totp = models.CharField(max_length=255, null=True)
    angle_api_key = models.CharField(max_length=255, null=True)
    angle_seceret_key = models.CharField(max_length=255, null=True)

    is_zerodha = models.BooleanField(default=False)
    zerodha_totp = models.CharField(max_length=255, null=True)
    zerodha_api_key = models.CharField(max_length=255, null=True)
    zerodha_seceret_key = models.CharField(max_length=255, null=True)
    
    is_aliceblue = models.BooleanField(default=False)
    aliceblue_totp = models.CharField(max_length=255, null=True)
    aliceblue_api_key = models.CharField(max_length=255, null=True)
    aliceblue_seceret_key = models.CharField(max_length=255, null=True)

    referral_code = models.CharField(max_length=64, blank=True)
    child_name = models.CharField(max_length=255, blank=True)
    master_id = models.IntegerField(null=True, blank=True)

    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.username

    class Meta:
        db_table = 'UserType'
        ordering = ['-created']




