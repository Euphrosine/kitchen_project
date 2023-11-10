from django.db import models

class KitchenData(models.Model):
    temperature = models.FloatField()
    gas_level = models.FloatField()
    flame = models.BooleanField()
    relay1 = models.BooleanField()
    relay2 = models.BooleanField()
    switch1 = models.BooleanField()
    switch2 = models.BooleanField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"KitchenData - {self.datetime}"
