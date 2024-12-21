from django.db import models
import random, string
# Create your models here.

def create_referral_code():
    while True:
        ref_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
        if not Master.objects.filter(referal_code=ref_code).exists():
            return ref_code

class Master(models.Model):

    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phn_number = models.CharField(max_length=11)
    password = models.CharField(max_length=255)
    referal_code = models.CharField(max_length=64,editable=False, default=create_referral_code)
    broker = models.CharField(max_length=9, default='Angle', choices=[
        ('Angle', 'Angle'),
        ('Zerodha', 'Zerodha'),
        ('AliceBlue', 'AliceBlue'),
    ])
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

    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.username

    class Meta:
        db_table = 'master'
        ordering = ['created']