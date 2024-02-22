from django.db import models

class Togrisoz(models.Model):
    soz = models.CharField(max_length=90)


    def __str__(self):
        return f"{self.soz}"


class Notogrisoz(models.Model):
    soz = models.CharField(max_length=90)
    togri_soz = models.ForeignKey(Togrisoz, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.soz}"