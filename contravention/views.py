from django.shortcuts import render,redirect
from .models import *
from django.shortcuts import get_object_or_404

        # Page d'accueil
def home_views(requete):
    nassujettis = Assujettis.objects.count()
    ncontact = Contact.objects.count()
    ninfraction = Infraction.objects.count()
    namende = Amende.objects.count()
    npaiement = Paiement.objects.count()

    ctx = {
        'nassujettis' : nassujettis,
        'ncontact' : ncontact,
        'ninfraction' : ninfraction,
        'namende' : namende,
        'npaiement' : npaiement,
        'title' : "Home"
    }
    
    return render(requete, 'appcontra/home.html', ctx)

        # Page de création
    
def assujetti_views(requete):
    ctx = {
        'title' : "Formulaire Assujetti"
    }
    return render(requete, 'appcontra/assujetti.html', ctx)

def amende_views(requete):
    infractions = Infraction.objects.all()
    ctx = {
        'title' : "Formulaire Amende",
        'infractions' : infractions
    }
    return render(requete, 'appcontra/amende.html', ctx)

def contact_views(requete):
    assujettis = Assujettis.objects.all()
    ctx = {
        'title' : "Formulaire Contact",
        'assujettis' : assujettis
    }
    return render(requete, 'appcontra/contact.html', ctx)

def infraction_views(requete):
    assujettis = Assujettis.objects.all()
    ctx = {
        'title' : "Formulaire Infraction",
        'assujettis' : assujettis
    }
    return render(requete, 'appcontra/infraction.html', ctx)

def paiement_views(requete):
    amendes = Amende.objects.all()
    ctx = {
        'title' : "Formulaire Paiement",
        'amendes' : amendes
    }
    return render(requete, 'appcontra/paiement.html', ctx)
      #--------------------------
      
        # Page des listes
def assujettis_views(requete):
    assujettis = Assujettis.objects.all()
    ctx = {
        'assujettis' : assujettis,
        'title' : "Gestion des Assujettis"
    }
    return render(requete, 'appcontra/assujettis.html', ctx)

def amendes_views(requete):
    amendes = Amende.objects.all()
    ctx = {
        'amendes' : amendes,
        'title' : "Gestion des Amendes"
    }
    return render(requete, 'appcontra/amendes.html', ctx)

def contacts_views(requete):
    contacts = Contact.objects.all()
    ctx = {
        'contacts' : contacts,
        'title' : "Gestion des Contacts"
    }
    return render(requete, 'appcontra/contacts.html', ctx)

def infractions_views(requete):
    infractions = Infraction.objects.all()
    ctx = {
        'infractions' : infractions,
        'title' : "Gestion des Infractions"
    }
    return render(requete, 'appcontra/infractions.html', ctx)

def paiements_views(requete):
    paiements = Paiement.objects.all()
    ctx = {
        'paiements' : paiements,
        'title' : "Gestion des Paiements"
    }
    return render(requete, 'appcontra/paiements.html', ctx)
        # --------------------------
        # Page de modification

def mcontact_views(requete, cont):
    mc = Contact.objects.get(numero=cont)
    assujettis = Assujettis.objects.all()
    
    ctx = {
        'c' : mc,
        'assujettis' : assujettis,
        'title': "Modification d'un Contact"
    }
    return render(requete, 'appcontra/mcontact.html', ctx)

def minfraction_views(requete, inf):
    mi = Infraction.objects.get(id=inf)
    assujettis = Assujettis.objects.all()
    
    ctx = {
        'i' : mi,
        'assujettis' : assujettis,
        'title': "Modification d'une Infraction"
    }
    return render(requete, 'appcontra/minfraction.html', ctx)

def mamende_views(requete, am):
    ma = Amende.objects.get(numero=am)
    infractions = Infraction.objects.all()
    
    ctx = {
        'a' : ma,
        'infractions' : infractions,
        'title': "Modification d'une Amende"
    }
    return render(requete, 'appcontra/mamende.html', ctx)

def mpaiement_views(requete, paie):
    mp = Paiement.objects.get(numero=paie)
    amendes =Amende.objects.all()
    
    ctx = {
        'p' : mp,
        'amendes' : amendes,
        'title': "Modification d'un Paiement"
    }
    return render(requete, 'appcontra/mpaiement.html', ctx)

def massujettis_views(requete, ass):
    asm = Assujettis.objects.get(numero=ass)
    ctx ={
        'ass': asm,
        'title': "Modification d'un assujettis",
    }
    return render(requete,'appcontra/massujettis.html', ctx)



# -------------------------------------------

# Fonction des pages

            # Fonction de Suppression
            
#--------------------------------------------



def sassujettis_view(requete, ass):
    a_s = Assujettis.objects.get(numero=ass)
    a_s.delete()
    assujettis = Assujettis.objects.all()
    ctx = {
        'assujettis' : assujettis,
        'title' : "Gestion des Assujettis"
    }
    return render(requete, 'appcontra/assujettis.html', ctx)

def scontact_view(requete, cont):
    c_s = Contact.objects.get(numero=cont)
    c_s.delete()
    contacts = Contact.objects.all()
    ctx = {
        'contacts' : contacts,
        'title' : "Gestion des Contacts"
    }
    return render(requete, 'appcontra/contacts.html', ctx) 

def sinfraction_view(requete, inf):
    i_s = Infraction.objects.get(id=inf)
    i_s.delete()
    infractions = Infraction.objects.all()
    ctx = {
        'infractions' : infractions,
        'title' : "Gestion des infractions"
    }
    return render(requete, 'appcontra/infractions.html', ctx) 

def samende_view(requete, am):
    a_s = Amende.objects.get(numero=am)
    a_s.delete()
    amendes = Amende.objects.all()
    ctx = {
        'amendes' : amendes,
        'title' : "Gestion des Amendes"
    }
    return render(requete, 'appcontra/amendes.html', ctx) 

def spaiement_view(requete, paie):
    p_s = Paiement.objects.get(numero=paie)
    p_s.delete()
    paiements = Paiement.objects.all()
    ctx = {
        'paiements' : paiements,
        'title' : "Gestion des Paiements"
    }
    return render(requete, 'appcontra/paiements.html', ctx) 


#--------------------------------------------

                # Fonction Enregistrer
        # si c'est nouveau
# ------------------------------------------



def econtact_views(requete):
    nu = requete.POST['numero']
    te = requete.POST['telephone']
    e = requete.POST['email']
    m = requete.POST['message']

    assu_code = requete.POST['assujettis'] 
    ass = Assujettis.objects.get(numero=assu_code)
    rse = Contact.objects.filter(numero=nu)

    new = Contact()
    new.numero = nu
    new.assujettis = ass
    new.telephone = te
    new.email = e
    new.message = m
    new.save()

    contacts = Contact.objects.all()
    ctx = {
        'contacts' : contacts,
        'title' : "Gestion des Contacts"
    }
    return render(requete, 'appcontra/contacts.html', ctx)

def epaiement_views(requete):
    nu = requete.POST['numero']
    d = requete.POST['datep']
    m = requete.POST['mode']

    am_code = requete.POST['amende'] 
    am = Amende.objects.get(numero=am_code)
    rse = Paiement.objects.filter(numero=nu)

    new = Paiement()
    new.numero = nu
    new.datep = d
    new.mode = m
    new.amende = am
    new.save()

    paiements = Paiement.objects.all()
    ctx = {
        'paiements' : paiements,
        'title' : "Gestion des Paiements"
    }
    return render(requete, 'appcontra/paiements.html', ctx)


def einfraction_views(requete):
    i = requete.POST['id']
    de = requete.POST['detail']
    da = requete.POST['datein']
    l = requete.POST['lieu']

    ass_code = requete.POST['assujettis'] 
    ass = Assujettis.objects.get(numero=ass_code)

    rse = Infraction.objects.filter(id=i)

    new = Infraction()
    new.id = i
    new.detail = de
    new.datein = da
    new.lieu = l
    new.assujettis = ass
    new.save()

    infractions = Infraction.objects.all()
    ctx = {
        'infractions' : infractions,
        'title' : "Gestion des Infractions"
    }
    return render(requete, 'appcontra/infractions.html', ctx)

def eamende_views(requete):
    nu = requete.POST['numero']
    mo = requete.POST['montant']
    da = requete.POST['datem']
    s = requete.POST['status']

    in_code = requete.POST['infraction'] 
    inf = Infraction.objects.get(id=in_code)

    rse = Amende.objects.filter(numero=nu)

    new = Amende()
    new.numero = nu
    new.montant = mo
    new.datem = da
    new.status = s
    new.infraction = inf
    new.save()

    amendes = Amende.objects.all()
    ctx = {
        'amendes' : amendes,
        'title' : "Gestion des Amendes"
    }
    return render(requete, 'appcontra/amendes.html', ctx)



def eassujettis_views(requete):
    nu = requete.POST['numero']
    no = requete.POST['noms']
    se = requete.POST['sexe']
    d = requete.POST['date']
    a = requete.POST['adresse']
    t = requete.POST['telephone']
    rss = Assujettis.objects.filter(numero=nu)

    new = Assujettis()
    new.numero = nu
    new.noms = no
    new.sexe = se
    new.date = d
    new.adresse = a
    new.telephone = t
    new.save()

    assujettis = Assujettis.objects.all()
    ctx = {
        'assujettis' : assujettis,
        'title' : "Gestion des Assujettis"
    }
    return render(requete, 'appcontra/assujettis.html', ctx)


    # -------------------------------
        # si pour modifier
        
        
def emassujettis_views(requete):
    nu = requete.POST['numero']
    no = requete.POST['noms']
    se = requete.POST['sexe']
    d = requete.POST['date']
    a = requete.POST['adresse']
    t = requete.POST['telephone']
    rsp = Assujettis.objects.filter(numero=nu)

    hold = rsp.first()
    hold.noms = no
    hold.sexe = se
    hold.date = d
    hold.adresse = a
    hold.telephone = t
    hold.save()

    assujettis = Assujettis.objects.all()
    ctx = {
        'assujettis' : assujettis,
        'title' : "Gestion des Assujettis"
    }
    return render(requete,'appcontra/assujettis.html', ctx)

def emamende_views(requete):
    nu = requete.POST['numero']
    mo = requete.POST['montant']
    da = requete.POST['datem']
    s = requete.POST['status']

    in_code = requete.POST['infraction'] 
    inf = Infraction.objects.get(id=in_code)
    
    rse = Amende.objects.filter(numero=nu)

    hold = rse.first()
    hold.montant = mo
    hold.datem = da
    hold.status = s
    hold.infraction = inf
    hold.save()

    amendes = Amende.objects.all()
    ctx = {
        'amendes' : amendes,
        'title' : "Gestion des Amendes"
    }
    return render(requete, 'appcontra/amendes.html', ctx)

def eminfraction_views(requete):
    i = requete.POST['id']
    de = requete.POST['detail']
    da = requete.POST['datein']
    l = requete.POST['lieu']

    ass_code = requete.POST['assujettis'] 
    ass = Assujettis.objects.get(numero=ass_code)
    rse = Infraction.objects.filter(id=i)

    hold = rse.first()
    hold.detail = de
    hold.datein = da
    hold.lieu = l
    hold.assujettis = ass
    hold.save()

    infractions = Infraction.objects.all()
    ctx = {
        'infractions' : infractions,
        'title' : "Gestion des Infractions"
    }
    return render(requete, 'appcontra/infractions.html', ctx)


def emcontact_views(requete):
    nu = requete.POST['numero']
    te = requete.POST['telephone']
    e = requete.POST['email']
    m = requete.POST['message']

    assu_code = requete.POST['assujettis'] 
    ass = Assujettis.objects.get(numero=assu_code)

    rse = Contact.objects.filter(numero=nu)

    hold = rse.first()
    hold.telephone = te
    hold.email = e
    hold.message = m
    hold.assujettis = ass
    hold.save()

    contacts = Contact.objects.all()
    ctx = {
        'contacts' : contacts,
        'title' : "Gestion des Contacts"
    }
    return render(requete, 'appcontra/contacts.html', ctx)

def empaiement_views(requete):
    nu = requete.POST['numero']
    d = requete.POST['datep']
    m = requete.POST['mode']

    am_code = requete.POST['amende'] 
    am = Amende.objects.get(numero=am_code)

    rse = Paiement.objects.filter(numero=nu)

    hold = rse.first()
    hold.amende = am
    hold.datep = d
    hold.mode = m
    
    hold.save()

    paiements = Paiement.objects.all()
    ctx = {
        'paiements' : paiements,
        'title' : "Gestion des Paiements"
    }
    return render(requete, 'appcontra/paiements.html', ctx)