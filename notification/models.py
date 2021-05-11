from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=70)
    pincode = models.CharField(max_length=50)
    age = models.CharField(max_length=20)
    notify_type = models.CharField(max_length=20, null=True)
    notified = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)



