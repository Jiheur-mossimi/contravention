from django.urls import path
from .views import *

urlpatterns = [
    
    # 1 Pages d'affichage
                # Page d'accueil
    path('', home_views, name="home"),
                 # - Pages pour créer
    path('assujetti/add', assujetti_views, name="assujetti"),
    path('contact/add', contact_views, name="contact"),
    path('amende/add', amende_views, name="amende"),
    path('infraction/add', infraction_views, name="infraction"),
    path('paiement/add', paiement_views, name="paiement"),

                # Pages pour modifier
    path('massujettis/<str:ass>/', massujettis_views, name="massujettis"),
    path('mcontact/<str:cont>/', mcontact_views, name="mcontact"),
    path('mamende/<str:am>/', mamende_views, name="mamende"),
    path('minfraction/<str:inf>/', minfraction_views, name="minfraction"),
    path('mpaiement/<str:paie>/', mpaiement_views, name="mpaiement"),

                #Pages pour les listes
    path('assujettis/', assujettis_views, name="assujettis"),
    path('econtacts/', contacts_views, name="contacts"),
    path('amendes/', amendes_views, name="amendes"),
    path('infractions/', infractions_views, name="infractions"),
    path('paiements/', paiements_views, name="paiements"),

                    #-----------------------

    # 2 Les actions des pages
                # Pour enrégistrer nouvelle
    path('eassujettis/', eassujettis_views, name="eassujettis"),
    path('eamende/', eamende_views, name="eamende"),
    path('epaiement/', epaiement_views, name="epaiement"),
    path('einfraction/', einfraction_views, name="einfraction"),
    path('econtact/', econtact_views, name="econtact"),
    
                # pour modifier un élément
    path('emassujettis/', emassujettis_views, name="emassujettis"),
    path('emcontact/', emcontact_views, name="emcontact"),
    path('emamende/', emamende_views, name="emamende"),
    path('empaiement/', empaiement_views, name="empaiement"),
    path('eminfraction/', eminfraction_views, name="eminfraction"),
    path('emcontact/', emcontact_views, name="emcontact"),


                # Pour Supprimer
    path('sassujettis/<str:ass>/', sassujettis_view, name="sassujettis"),
    path('scontact/<str:cont>/', scontact_view, name="scontact"),
    path('samende/<str:am>/', samende_view, name="samende"),
    path('sinfraction/<str:inf>/', sinfraction_view, name="sinfraction"),
    path('spaiement/<str:paie>/', spaiement_view, name="spaiement"),


]