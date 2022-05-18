from django.shortcuts import render
from helpers.tests import *
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
import time
from helpers.remplirbd import *
from django.contrib.auth.hashers import check_password, make_password
# Create your views here.

FRAIS_1 = 0.6
FRAIS_2 = 1
MAXITRANSACTIONS = 500000
MAXICOMPTE = 200000
PROMO = FRAIS_1/2

def create_key():
    key = Fernet.generate_key()
    f = key.decode()
    return f


@api_view(['POST'])
def demande (request):
    try:
        data =[]
        username = request.data['username']
        mdp = request.data['mdp']
        user = Bac17.objects.filter(bac17username=crypterMotPasse(username))
        if user:
            i = Bac17.objects.get(bac17username=crypterMotPasse(username))
            if check_password(mdp,i.bac17mdp):
                token = generer_author(i)
                tokenR = generer_authorR(i)
                data.append({"auth": token, "refresh": tokenR})
                return retour(200, data)
            else:
                return retour(300,data)
        else:
            return retour(301, data)
    except:
        return retour(505,data)
# Renouvellement token


@api_view(['POST'])
def refresh(request):
    try:
        data = []
        ab = verification_authorR(request)
        ac = ab.get("bool")
        if ac:
            pd = Bac17.objects.get(bac17username=ab.get("user"))
            token = generer_author(pd)
            data.append({"auth": token})
            return retour(200, data)
        else:
            # Identifiant incorrect
            return retour(300, data)
    except:
        return retour(505, data)

"""
def bdd(request):
    cd = Dcbr()
    cd.remplirbd()
    ere = compte_cinit()
    return JsonResponse(dict({'er':'e'}))
"""


######################################################## Vérification du numéro téléphone

@api_view(['POST'])
def verifa(request):
    data = []
    if verification_author(request):
        if expiration_author(request):
            try:
                ab = int(request.data['telephone'])
            except:
                return retour(303, data)

            if not len(request.data['telephone']) == 10:
                return retour(302, data)

            acteur = Pg002.objects.filter(username=request.data['telephone'])
            if acteur:
                acteur = Pg002.objects.get(username=request.data['telephone'])
                data.append(dict({"id": acteur.pk, "test": acteur.pg002id}))
                if acteur.password == "":
                  return retour(201, data)  
                return retour(200, data)
            else:
                acteur = Pg002()
                acteur.username = request.data['telephone']
                acteur.pg002id = genererIdentifiant('UNIM')
                acteur.is_active = False
                acteur.pg002ps = generate_otp(4)
                otp = generate_otp(6)
                acteur.pg002otp = otp
                acteur.pg002otp_expired = time.time()
                acteur.save()

                ##############Table compte
                compte = Ps003()
                compte.ps003id = genererIdentifiant('COM{}PTI'.format(generate_otp(2)))
                compte.ps003numero_compte = genererIdentifiant('{}'.format(generate_otp(3)))
                compte.ps003timetransaction=0
                compte.ps003timesomme=0
                compte.ps003plafond = MAXICOMPTE
                compte.pg002_id = acteur
                compte.save()
                data.append(dict({"id": acteur.pk, "test": acteur.pg002id}))
                return retour(202, data)
        else:
            return retour(450, data)
    else:
        return retour(400, data)


#1------------ Générer OTP

@api_view(['POST'])
def generer_otp(request):
    try:
        data = []
        if verification_author(request):
            if expiration_author(request):
                id = request.data['id']
                test = request.data['test']
                if not Pg002.objects.filter(pk=id, pg002id=test):
                    return retour(300, data)
                acteur = Pg002.objects.get(pk=id, pg002id=test)
                otp = generate_otp(6)
                acteur.pg002otp = otp
                acteur.pg002otp_expired = time.time()
                acteur.save()
                ####Appel d'api de SMS
                data.append(dict({"id": acteur.pk, "test": acteur.pg002id,"otp":otp}))
                return retour(200, data)
            else:
                return retour(450, data)
        else:
            return retour(400, data)
    except:
        return retour(505, data)

##*********************************************  PROCESSUS D'INSCRIPTION     ***************************




#2------------ Vérification de l' OTP
@api_view(['POST'])
def validation(request):
    try:
        data = []
        if verification_author(request):
            if expiration_author(request):
                otp = request.data['otp']
                id = request.data['id']
                test = request.data['test']
                if Pg002.objects.filter(pk=id, pg002id=test):
                    acteur = Pg002.objects.get(pk=id, pg002id=test)
                    if acteur.pg002otp == otp:
                        if evaluate_time(acteur.pg002otp_expired, 120):
                            ab = generate_otp(6)
                            acteur.pg002otp = ab
                            acteur.pg002otp_expired = time.time()
                            acteur.save()
                            return retour(200, data)
                        else:
                            return retour(300, data)
                    else:
                        return retour(301, data)
                return retour(302, data)
            else:
                return retour(450, data)
        else:
            return retour(400, data, )
    except:
        return retour(505, data)


#3 ------------ Enregistrement du mot de passe

@api_view(['POST'])
def enregistrer_password(request):
    data = []
    if verification_author(request):
        if expiration_author(request):
            id = request.data['id']
            test = request.data['test']
            mdp = request.data['toi']
            acteur = Pg002.objects.filter(pk=id, pg002id=test)
            if acteur:
                acteur = Pg002.objects.get(pk=id,pg002id=test)
                mdu = "{}{}".format(mdp,acteur.pg002ps)
                acteur.password = make_password(mdu)
                acteur.is_active = True
                acteur.save()
                ##############Table connexion
                pm = Ps110.objects.filter(pg002_id=acteur, ps110statut_connexion=True)
                if pm :
                    for i in pm:
                        i.delete()
                connexion = Ps110()
                connexion.ps110id = genererIdentifiant('LOGIN')
                connexion.ps110telephone = create_key()
                connexion.ps110statut_connexion = True
                connexion.pg002_id = acteur
                connexion.save()
                print(acteur.password)
                token = generer_token(acteur,connexion)
                tokenR = generer_tokenR(acteur,connexion)
                data.append(dict({"id": acteur.pk, "moi": acteur.pg002id,"authUser":token,"refreshUser":tokenR}))    
                return retour(200, data)
            else:
                return retour(301, data)
        else:
            return retour(450, data)
    else:
        return retour(400, data)


#4 ------------ Information de la personne

@api_view(['POST'])
def newinformation(request):
    data = []
    if verification_author(request):
        if expiration_author(request):
            if verification_token(request):
                if expiration_token(request):
                    nom = request.data['nom']
                    prenom = request.data['prenom']
                    sexe = request.data['sexe']
                    if get_id_by_token(request) == False:
                        return retour(300,data)
                    acteur = get_id_by_token(request)
                    acteur.first_name = nom.upper()
                    acteur.last_name = prenom.upper()
                    acteur.pg002sexe = sexe
                    acteur.save()
                    d = dict()
                    d['nom'] = acteur.first_name
                    d['prenoms'] = acteur.last_name
                    d['username'] = acteur.username
                    data.append(d)
                    return retour(200, data)
                else:
                    return retour(470, data)
            else:
                return retour(460, data)
        else:
            return retour(450, data)
    else:
        return retour(400, data)
####################################### Processus de log étant déconnecté

#1 ------------ Vérification du mot de passe
@api_view(['POST'])
def verification_password(request):
    try:
        data = []
        if verification_author(request):
            if expiration_author(request):
                id = request.data['id']
                test = request.data['test']
                mdp = request.data['toi']
                acteur = Pg002.objects.filter(pk=id, pg002id=test)
                if acteur:
                    acteur = Pg002.objects.get(pk=id, pg002id=test)
                    mdu = "{}{}".format(mdp,acteur.pg002ps)
                    if check_password(mdu,acteur.password):
                        data.append(dict({"id": acteur.pk, "test": acteur.pg002id}))
                        return retour(200, data)
                    return retour(305, data)
                else:
                    return retour(301, data)
            else:
                return retour(450, data)
        else:
            return retour(400, data)
    except:
        return retour(505, data)

#2------------ Vérification de l' OTP avec connexion
@api_view(['POST'])
def validation_afterconnexion(request):
    try:
        data = []
        if verification_author(request):
            if expiration_author(request):
                otp = request.data['otp']
                id = request.data['id']
                test = request.data['test']
                if Pg002.objects.filter(pk=id, pg002id=test):
                    acteur = Pg002.objects.get(pk=id, pg002id=test)
                    if acteur.pg002otp == otp:
                        if evaluate_time(acteur.pg002otp_expired, 120):
                            ab = generate_otp(6)
                            acteur.pg002otp = ab
                            acteur.pg002otp_expired = time.time()
                            acteur.save()
                            pm = Ps110.objects.filter(pg002_id=acteur, ps110statut_connexion=True)
                            if pm :
                                for i in pm:
                                    i.delete()
                            connexion = Ps110()
                            connexion.ps110id = genererIdentifiant('LOGIN')
                            connexion.ps110telephone = create_key()
                            connexion.ps110statut_connexion = True
                            connexion.pg002_id = acteur
                            connexion.save()
                            token = generer_token(acteur,connexion)
                            tokenR = generer_tokenR(acteur,connexion)
                            data.append(dict({"id": acteur.pk, "moi": acteur.pg002id,"authUser":token,"refreshUser":tokenR}))  
                            return retour(200, data)
                        else:
                            return retour(300, data)
                    else:
                        return retour(301, data)
                return retour(302, data)
            else:
                return retour(450, data)
        else:
            return retour(400, data, )
    except:
        return retour(505, data)

####################################### Processus de log étant connecté

#1 ------------ Vérification du mot de passe
@api_view(['POST'])
def verification_password_connexion(request):
    try:
        data = []
        if verification_author(request):
            if expiration_author(request):
                if verification_token(request):
                    if expiration_token(request):
                        if get_id_by_token(request) == False:
                            return retour(300,data)
                        mdp = request.data['toi']
                        acteur = get_id_by_token(request)
                        mdu = "{}{}".format(mdp,acteur.pg002ps)
                        if check_password(mdu,acteur.password):
                            return retour(200, data)
                        return retour(305, data)
                    else:
                        return retour(470, data)
                else:
                        return retour(460, data)
            else:
                return retour(450, data)
        else:
            return retour(400, data)
    except:
        return retour(505, data)



###############********************************** Une fois connecctée


####"************ 5 -------- Historique des paiements 

@api_view(['GET'])
def historiquepaiements(request):
    try:
        data = []
        if verification_author(request):
            if expiration_author(request):
                if verification_token(request):
                    if expiration_token(request):
                        if get_id_by_token(request) == False:
                            return retour(300,data)
                        acteur = get_id_by_token(request)
                        compte = Ps003.objects.get(pg002_id=acteur)
                        envoi = Pg100.objects.filter(ps003codeEnvoi=compte)
                        for i in envoi:
                            d = dict()
                            d['type']= "ENVOI"
                            d['somme']= i.pg100somme
                            d['date'] = i.dateCreation
                            data.append(d)
                        recu = Pg100.objects.filter(ps003codeRecu=compte)
                        for i in envoi:
                            d = dict()
                            d['type']= "REÇU"
                            d['somme']= i.pg100somme
                            d['date'] = i.dateCreation
                            data.append(d)
                        return retour(200, data)
                    
                    else:
                        return retour(470, data)
                else:
                        return retour(460, data)
            else:
                return retour(450, data)
        else:
            return retour(400, data)
    except:
        return retour(505, data)


####"************ 2 -------- GENERATION QR CODE

@api_view(['GET'])
def qrcode(request):
    try:
        data = []
        if verification_author(request):
            if expiration_author(request):
                if verification_token(request):
                    if expiration_token(request):
                        if get_id_by_token(request) == False:
                            return retour(300,data)
                        acteur = get_id_by_token(request)
                        qrcode = code_qr(acteur.pk,False)
                        d= dict()
                        d['qrcode'] = qrcode
                        data.append(qrcode)
                        return retour(200, data)
                    else:
                        return retour(470, data)
                else:
                        return retour(460, data)
            else:
                return retour(450, data)
        else:
            return retour(400, data)
    except:
        return retour(505, data)


####"************ 1 -------- Processus de paiement


@api_view(['POST'])
def scanqrcode(request):
    try:
        data = []
        if verification_author(request):
            if expiration_author(request):
                if verification_token(request):
                    if expiration_token(request):
                        if get_id_by_token(request) == False:
                            return retour(300,data)
                        acteur = get_id_by_token(request)
                        url = request.data['url']
                        qrcode = verif_qr(url)
                        if qrcode == False:
                            return retour(301,data)
                        id = qrcode['id']
                        type = qrcode['type']

                        if type == 10:
                            if not Pg002.objects.filter(pk=id, is_active = True, pg002test=False):
                                return retour(302,data)
                            destination = Pg002.objects.get(pk=id)
                            der = dict()
                            der['id'] = destination.pk
                            der['test'] = destination.pg002id
                            der['nom'] = destination.first_name
                            der['prenoms'] = destination.last_name
                            der['numéro'] = destination.username
                            return retour(200, der)

                        if type == 11:
                            if not Pg001.objects.filter(pk=id, pg001compte_valide = True, pg001test=False):
                                return retour(303,data)
                            destination = Pg001.objects.get(pk=id)
                            der = dict()
                            der['id'] = destination.pk
                            der['test'] = destination.pg001id
                            der['raison_social'] = destination.pg001raisonSocial
                            der['sigle'] = destination.pg001sigle
                            return retour(201, der)
                    else:
                        return retour(470, data)
                else:
                        return retour(460, data)
            else:
                return retour(450, data)
        else:
            return retour(400, data)
    except:
        return retour(505, data)


@api_view(['POST'])
def transfertdm(request):
    data = []
    if verification_author(request):
        if expiration_author(request):
            if verification_token(request):
                if expiration_token(request):

                    #***************** Récupéprer l'id de l'acteur
                    if get_id_by_token(request) == False:
                        return retour(300,data)
                    source = get_id_by_token(request)


                    #***************** Récupération des données du récepteur
                    id_destinateur = request.data['id']
                    test_destinateur = request.data['test']
                    montant_destinateur = float(request.data['montant'])
                    type_destinateur = request.data['type']

                    #******************* Frais

                    frais = 0.6
                    if montant_destinateur < 15000:
                        frais = FRAIS_1
                    elif montant_destinateur > 15000:
                        frais = FRAIS_2

                    ################### Vérification des acteurs/groupes
                    groupe_promo = False
                    #************** Compte de la source valide    
                    if not source.is_active or source.pg002test== True:
                        return retour(300,data)

                    #************** Compte groupe / physique 
                    compte_recu = ""
                    if type_destinateur ==11:
                        if not Pg001.objects.filter(pk=id_destinateur, pg001id=test_destinateur ,pg001compte_valide = True, pg001test=False):
                            return retour(302,data)
                        destination = Pg001.objects.get(pk=id_destinateur,pg001id=test_destinateur)
                        compte_recu = Ps003.objects.get(pg001_id=destination,ps003compte_groupe=True)
                        if destination.pg001identifie == True:
                            groupe_promo = True


                    elif type_destinateur ==10:
                        if not Pg002.objects.filter(pk=id_destinateur,pg002id=test_destinateur ,is_active = True, pg002test=False):
                            return retour(303,data)
                        destination = Pg002.objects.get(pk=id_destinateur,pg002id=test_destinateur)
                        compte_recu = Ps003.objects.get(pg002_id=destination)
                    
                    compte_envoi = Ps003.objects.get(pg002_id=source)
                    compte_cinit = Ps003.objects.get(ps003compte_cinit=True)

                    if compte_envoi == compte_recu:
                        return retour(306,data)
                    #***************** Vérification des achats sur un délai de 1 mois temps
                    b = time.time()
                    diff = int(b) - int(compte_envoi.ps003timetransaction)
                    if diff > 2592000:
                        compte_envoi.ps003timetransaction = time.time()
                        compte_envoi.ps003timesomme = 0
                        compte_envoi.save()

                    #******************** Vérification du solde et du montant demandé
                    if compte_envoi.ps003morant < montant_destinateur :
                        return retour(304,data)

                    #******************** Vérification du maximum de transaction sur 1 mois
                    verifa = compte_envoi.ps003timesomme + montant_destinateur
                    if verifa > MAXITRANSACTIONS:
                        return retour(305,data)

                    #********************* Processus de Transaction 
                    
                    argent_transferer = montant_destinateur-(montant_destinateur*frais)/100
                    futur_solde_recepteur = argent_transferer + compte_recu.ps003morant

                    ####Plafond 
                    if futur_solde_recepteur > compte_recu.ps003plafond:
                        return retour(402,data)
                    print('SOLDE INITIAL: ',compte_envoi.ps003morant)    
                    compte_envoi.ps003morant = compte_envoi.ps003morant-montant_destinateur
                    compte_envoi.ps003timesomme = compte_envoi.ps003timesomme + montant_destinateur
                    compte_envoi.save()
                    print('SOLDE MIS A JOUR: ',compte_envoi.ps003morant)

                    print('ARGENT RECU INITIAL: ',compte_recu.ps003morant)
                    compte_recu.ps003morant = compte_recu.ps003morant + argent_transferer
                    compte_recu.save()
                    print('ARGENT RECU A JOUR: ',compte_recu.ps003morant)

                    benefice_cinit = (montant_destinateur*frais)/100

                    if groupe_promo:
                        compte_recu.ps003morant = compte_recu.ps003morant + benefice_cinit/2
                        compte_cinit.ps003morant = compte_cinit.ps003morant + benefice_cinit/2
                        compte_cinit.save()
                        compte_recu.save()

                    compte_cinit.ps003morant = compte_cinit.ps003morant + benefice_cinit
                    compte_cinit.save()

                    transaction = Pg100()
                    transaction.pg100somme_initial = montant_destinateur
                    transaction.pg101numTransaction = "{}{}".format(genererIdentifiant("TST"),generate_otp(4))
                    transaction.pg100somme = argent_transferer
                    transaction.pg100frais = frais

                    transaction.ps003codeEnvoi = compte_envoi
                    transaction.ps003codeRecu = compte_recu
                    transaction.save()
                
                    return retour(200, data)
                else:
                    return retour(470, data)
            else:
                    return retour(460, data)
        else:
            return retour(450, data)
    else:
        return retour(400, data)


"""
@api_view(['POST'])
def transfertdm(request):
    data = []
    if verification_author(request):
        if expiration_author(request):
            if verification_token(request):
                if expiration_token(request):
                    if get_id_by_token(request) == False:
                        return retour(300,data)

                    acteur = get_id_by_token(request)
                    groupe_promo = False

                    ######### récupération des données du récepteur
                    montant = float(request.data['montant'])
                    id = request.data['id']
                    test = request.data['test']
                    type = request.data['type']

                    ##################Frais
                    frais = 0.6
                    if montant < 15000:
                        frais = FRAIS_1
                    elif montant > 15000:
                        frais = FRAIS_2

                    ################### Vérification des acteurs/groupes    
                    if not acteur.is_active or acteur.pg002test== True:
                        return retour(300,data)

                    compte_recu = ""
                    if type ==11:
                        if not Pg001.objects.filter(pk=id, pg001id=test ,pg001compte_valide = True, pg001test=False):
                            return retour(302,data)
                        destination = Pg001.objects.get(pk=id,pg001id=test)
                        compte_recu = Ps003.objects.get(pg001_id=destination,ps003compte_groupe=True)
                        if destination.pg001identifie == True:
                            groupe_promo = True


                    elif type ==10:
                        if not Pg002.objects.filter(pk=id,pg002id=test ,is_active = True, pg002test=False):
                            return retour(303,data)
                        destination = Pg002.objects.get(pk=id,pg002id=test)
                        compte_recu = Ps003.objects.get(pg002_id=destination)
                    
                    compte_envoi = Ps003.objects.get(pg002_id=acteur)
                    compte_cinit = Ps003.objects.get(ps003compte_cinit=True)

                    ############## vérification du temps
                    b = time.time()
                    diff = int(b) - int(compte_envoi.ps003timetransaction)
                    if diff > 2592000:
                        compte_envoi.ps003timetransaction = time.time()
                        compte_envoi.ps003timesomme = 0
                        compte_envoi.save()

                    ############## Vérification des plafonds et contraintes de l'envoyé
                    if compte_envoi.ps003morant < montant :
                        return retour(400,data)
    
                    verifa = compte_envoi.ps003timesomme + montant
                    if verifa > MAXITRANSACTIONS:
                        return retour(401,data)

                    ############## Transfert d'argent
                    
                    djekoua = montant-(montant*frais)/100
                    print("djekoua")
                    print(djekoua)
                    argent = djekoua + compte_recu.ps003morant
                    print(argent," arge")
                    ####Plafond 
                    if argent > compte_recu.ps003plafond:
                        return retour(402,data)

                    compte_envoi.ps003morant = compte_envoi.ps003morant-djekoua
                    compte_envoi.ps003timesomme = compte_envoi.ps003timesomme + djekoua
                    compte_envoi.save()
                    print('ENVOYEUR ARGENT:',compte_envoi.ps003morant )
                    
                    compte_recu.ps003morant = djekoua + compte_recu.ps003morant
                    compte_recu.save()
                    print('RECEPTEUR ARGENT:',compte_recu.ps003morant)

                    cinit_djai = (montant*frais)/100
                    print('CINIT ARGENT:',cinit_djai)
                    if groupe_promo:
                        compte_recu.ps003morant = compte_recu.ps003morant + cinit_djai/2
                        compte_cinit.ps003morant = compte_cinit.ps003morant + cinit_djai/2
                        compte_cinit.save()
                        compte_recu.save()

                    compte_cinit.ps003morant = compte_cinit.ps003morant + cinit_djai
                    compte_cinit.save()

                    transaction = Pg100()
                    transaction.pg100somme_initial = montant
                    transaction.pg101numTransaction = "{}{}".format(genererIdentifiant("TST"),generate_otp(4))
                    transaction.pg100somme = argent
                    transaction.pg100frais = frais

                    transaction.ps003codeEnvoi = compte_envoi
                    transaction.ps003codeRecu = compte_recu
                    transaction.save()
                
                    return retour(200, data)
                else:
                    return retour(470, data)
            else:
                    return retour(460, data)
        else:
            return retour(450, data)
    else:
        return retour(400, data)
"""