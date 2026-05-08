from django.db import models

GOLEMINA_CHOICES = [
    ('mal', 'Мал'),
    ('sreden', 'Среден'),
    ('golem', 'Голем'),
]

class Buket(models.Model):
    ime = models.CharField(max_length=100)
    tip_na_cveke = models.CharField(max_length=100)
    golemina = models.CharField(max_length=10, choices=GOLEMINA_CHOICES)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    fotografija = models.ImageField(upload_to='buketi/', blank=True, null=True)
    godina_na_podgotovka = models.IntegerField()
    sveze = models.BooleanField(default=True)
    dali_e_od_EU = models.BooleanField(default=False)

    def __str__(self):
        return self.ime