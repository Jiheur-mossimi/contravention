from django.contrib import admin
from .models import Amende, Assujettis, Contact, Infraction, Paiement
# Register your models here.

admin.site.register(Amende, list_display=['numero','infraction', 'montant', 'datem', 'status'])
admin.site.register(Assujettis, list_display=['numero','noms', 'sexe', 'date', 'adresse', 'telephone'])
admin.site.register(Contact, list_display=['id','assujettis', 'telephone', 'email', 'message'])
admin.site.register(Infraction, list_display=['id','assujettis', 'detail', 'datein', 'lieu'])
admin.site.register(Paiement, list_display=['numero','amende', 'datep', 'mode'])