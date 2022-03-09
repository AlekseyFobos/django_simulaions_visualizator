from django.db import models

class Simulator(models.Model):
    simulator_name = models.CharField(max_length=100)
