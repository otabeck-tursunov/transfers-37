from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Season(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Club(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='clubs', null=True, blank=True)
    president = models.CharField(max_length=255, blank=True, null=True)
    coach = models.CharField(max_length=255, blank=True, null=True)
    found_date = models.DateField(blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=255)
    number = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(99)])
    position = models.CharField(max_length=255, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    price = models.FloatField(validators=[MinValueValidator(0)])
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Transfer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    old_club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='export_transfers')
    new_club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='import_transfers')
    price = models.FloatField(validators=[MinValueValidator(0)], blank=True, null=True)
    price_tft = models.FloatField("Price(tft.com)", validators=[MinValueValidator(0)], blank=True, null=True)
    created_at = models.DateField(blank=True, null=True)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)

    def __str__(self):
        return f"Transfer: {self.player} - {self.old_club} to {self.new_club}"
