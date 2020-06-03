from django.db import models

# Create your models here.

class Coupon(models.Model):
    url = models.CharField('URL', blank=True, max_length=2048)
    request_code = models.CharField('request_code', max_length=50)
    arg1 = models.CharField('arg1', max_length=255)
    arg2 = models.IntegerField('arg2', blank=True, default=0)

    created_at = models.DateTimeField('created_at', auto_now=False, auto_now_add=True,)
    updated_at = models.DateTimeField('updated_at', auto_now=True, auto_now_add=False,)


    def __str__(self):
        return self.request_code
