from django.db import models

# Create your models here.
class Agent(models.Model):
    agent_id = models.AutoField(primary_key=True)
    agent_name = models.CharField(max_length=50, unique=True)
    agent_investment = models.FloatField()
    agent_current_value = models.FloatField(default=0)
    safety = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)


class Transactions(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    agent_name = models.CharField(max_length=50)
    agent_current_value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

