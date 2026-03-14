from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Assujettis(models.Model):
    numero = models.CharField(max_length=10, primary_key=True, verbose_name="ID")
    noms = models.CharField(max_length=150, verbose_name="NOMS")
    sexe = models.CharField(max_length=1, verbose_name="SEXE")
    date = models.DateField(verbose_name="DATE", null=True, blank=True)
    adresse = models.CharField(max_length=150, verbose_name="ADRESSE")
    telephone = models.CharField(max_length=15, verbose_name="TELEPHONE")
    
    def __str__(self):
        return self.noms


class Contact(models.Model):
    id = models.CharField(max_length=10, primary_key=True, verbose_name="ID")
    assujettis = models.ForeignKey(Assujettis, on_delete=models.CASCADE, verbose_name="ID ASSUJETTIS")
    telephone = models.CharField(max_length=20, verbose_name="TELEPHONE")
    email = models.EmailField(max_length=254, verbose_name="EMAIL")
    message = models.CharField(max_length=500, verbose_name="MESSAGE")


class Infraction(models.Model):
    id = models.CharField(max_length=10, primary_key=True, verbose_name="ID")
    assujettis = models.ForeignKey(Assujettis, on_delete=models.CASCADE, verbose_name="ID ASSUJETTIS")
    detail = models.CharField(max_length=254, verbose_name="DETAIL D'INFRACTION")
    datein = models.DateTimeField(verbose_name="DATE D'INFRACTION")
    lieu = models.CharField(max_length=150, verbose_name="LIEU")
    
    def __str__(self):
        return self.detail


class Amende(models.Model):
    numero = models.CharField(max_length=10, primary_key=True, verbose_name="ID")
    infraction = models.ForeignKey(Infraction, on_delete=models.CASCADE, verbose_name="ID INFRACTION")
    montant = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="MONTANT")
    datem = models.DateTimeField(verbose_name="DATE D'EMISSION")
    status = models.CharField(max_length=20, verbose_name="STATUS")
    
    def __str__(self):
        return self.montant
    

class Paiement(models.Model):
    numero = models.CharField(max_length=10, primary_key=True, verbose_name="numero")
    amende = models.ForeignKey(Amende, on_delete=models.CASCADE, verbose_name="ID AMENDE")
    datep = models.DateTimeField(verbose_name="DATE DE PAIEMENT")
    mode = models.CharField(max_length=20, verbose_name="MODE DE PAIEMENT")