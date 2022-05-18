from django.shortcuts import render
from django.shortcuts import render
from .tests import *
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
import time
from helpers.remplirbd import *
from helpers.serializers import *
from django.contrib.auth.hashers import check_password, make_password
# Create your views here.

@api_view(['POST'])
def create_groupe(request):
    data = []
    if verification_author(request):
        if expiration_author(request):
            if Pg001.objects.filter(pg001identifiant=request.data['identifiant']):
                return retour(305,data)
            try:
                ab = int(request.data['telephone'])
            except:
                return retour(300, data)

            if not len(request.data['telephone']) == 10:
                return retour(301, data)

            acteur = Pg002.objects.filter(username=request.data['telephone'], is_active=True)
            if not acteur:
                return retour(302, data)
            acteur = Pg002.objects.get(username=request.data['telephone'],is_active=True)
            request.data['pg001id'] = genererIdentifiant("GROUPE")
            serializer = GroupeSerializer(data=request.data)
            if not serializer.is_valid():
                data.append(serializer.errors)
                return retour(303, data)
            serializer.save()
            groupe = Pg001.objects.get(pg001id=serializer.data['pg001id'])
            if Pg003.objects.filter(pg001_id = groupe,pg002_id = acteur):
                return retour(304,data)
            
            lien = Pg003()
            lien.pg003id = genererIdentifiant("GRUSER")
            lien.pg001_id = groupe
            lien.pg002_id = acteur
            lien.pg003admin = True
            lien.pg003retrait = True
            otp = generate_otp(6)
            lien.pg003otp = otp
            lien.pg003otp_expired = time.time()
            lien.save()

            compte = Ps003()
            compte.ps003id = genererIdentifiant('COMPTE_GROUPE'.format(generate_otp(2)))
            compte.ps003numero_compte = genererIdentifiant('{}'.format(generate_otp(3)))
            compte.ps003timetransaction=0
            compte.ps003timesomme=0
            compte.ps003plafond = 2000000
            compte.pg001_id = groupe
            compte.save()
            data.append({"id":lien.pk,"groupe":groupe.pg001raisonSocial,"identifiant":groupe.pg001identifiant,"groupe_id":groupe.pk,"acteur_id":acteur.pk,"nom":acteur.first_name,"prenoms":acteur.last_name})
            return retour(200,data)
        else:
            return retour(450, data)
    else:
        return retour(400, data)

@api_view(['POST'])
def generer_otp_groupe(request):
    try:
        data = []
        if verification_author(request):
            if expiration_author(request):
                id = request.data['id']
                if not Pg003.objects.filter(pk=id):
                    return retour(300, data)
                acteur = Pg003.objects.get(pk=id)
                otp = generate_otp(6)
                acteur.pg003otp = otp
                acteur.pg003otp_expired = time.time()
                acteur.save()
                ####Appel d'api de SMS
                data.append(dict({"id": acteur.pk, "otp":otp}))
                return retour(200, data)
            else:
                return retour(450, data)
        else:
            return retour(400, data)
    except:
        return retour(505, data)

@api_view(['POST'])
def validation_groupe(request):
    try:
        data = []
        if verification_author(request):
            if expiration_author(request):
                otp = request.data['otp']
                id = request.data['id']
                if Pg003.objects.filter(pk=id):
                    acteur = Pg003.objects.get(pk=id)
                    if acteur.pg003otp == otp:
                        if evaluate_time(acteur.pg003otp_expired, 120):
                            ab = generate_otp(6)
                            acteur.pg003otp = ab
                            acteur.pg003otp_expired = time.time()
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


@api_view(['POST'])
def enregistrer_password(request):
    data = []
    if verification_author(request):
        if expiration_author(request):
            id = request.data['id']
            mdp = request.data['toi']
            if Pg003.objects.filter(pk=id):
                acteur = Pg003.objects.get(pk=id)
                mdu = "{}{}".format(mdp,acteur.pg003id)
                acteur.pg003mdp = make_password(mdu)
                acteur.pg003estbloque = False
                acteur.save()
                ##############Table connexion
                pm = Ps111.objects.filter(pg003_id=acteur, ps111statut_connexion=True)
                if pm :
                    for i in pm:
                        i.delete()
                connexion = Ps111()
                connexion.ps111id = genererIdentifiant('LOGINGROUPE')
                connexion.ps111telephone = create_key()
                connexion.ps111statut_connexion = True
                connexion.pg003_id = acteur
                connexion.save()
                token = generer_token(acteur,connexion)
                tokenR = generer_tokenR(acteur,connexion)
                data.append(dict({"id": acteur.pk,"authUser":token,"refreshUser":tokenR}))    
                return retour(200, data)
            else:
                return retour(301, data)
        else:
            return retour(450, data)
    else:
        return retour(400, data)


@api_view(['POST'])
def newinformation(request):
    data = []
    if verification_author(request):
        if expiration_author(request):
            if verification_token(request):
                if expiration_token(request):
                    try:
                        ab = int(request.data['numero'])
                    except:
                        return retour(300, data)

                    if not len(request.data['numero']) == 10:
                        return retour(301, data)

                    if get_id_by_token(request) == False:
                        return retour(302,data)

                    acteur = get_id_by_token(request)
                    groupe = Pg001.objects.get(pk=acteur.pg001_id.pk)
                    if not groupe.pg001telephone == None:
                        return retour(303,data)
                    ab = generate_otp(6)
                    groupe.pg001otp = ab
                    groupe.pg001otp_expired = time.time()
                    groupe.pg001telephone = request.data['numero']
                    groupe.save()
                    d = dict()
                    d['numero'] = groupe.pg001telephone
                    d['id'] = acteur.pk
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


@api_view(['GET'])
def generer_otp_retrait(request):
    try:
        data = []
        if verification_author(request):
            if expiration_author(request):
                if verification_token(request):
                    if expiration_token(request): 
                        acteur = get_id_by_token(request)
                        groupe = Pg001.objects.get(pk=acteur.pg001_id.pk)
                        if groupe.pg001telephone == None:
                            return retour(303,data)
                        ab = generate_otp(6)
                        groupe.pg001otp = ab
                        groupe.pg001otp_expired = time.time()
                        groupe.save()
                        ####Appel d'api de SMS
                        data.append(dict({"id": acteur.pk, "otp":ab}))
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

@api_view(['POST'])
def validation_retrait(request):
    try:
        data = []
        if verification_author(request):
            if expiration_author(request):
                if verification_token(request):
                    if expiration_token(request):
                        otp = request.data['otp']
                        acteur = get_id_by_token(request)
                        groupe = Pg001.objects.get(pk=acteur.pg001_id.pk)
                        if groupe.pg001otp == otp:
                            if evaluate_time(groupe.pg001otp_expired, 120):
                                ab = generate_otp(6)
                                groupe.pg001otp = ab
                                groupe.pg001otp_expired = time.time()
                                groupe.save()
                                return retour(200, data)
                            else:
                                return retour(300, data)
                        else:
                            return retour(301, data)
                    else:
                        return retour(470, data)
                else:
                    return retour(460, data)
            else:
                return retour(450, data)
        else:
            return retour(400, data, )
    except:
        return retour(505, data)

@api_view(['POST'])
def connexion(request):
    try:
        data = []
        if verification_author(request):
            if expiration_author(request):
                identifiant = request.data['identifiant']
                numero = request.data['numero']
                pwd = request.data['password']
                if Pg003.objects.filter(pg001_id__pg001identifiant=identifiant,pg002_id__username=numero,pg003estbloque=False):
                    acteur = Pg003.objects.get(pg001_id__pg001identifiant=identifiant,pg002_id__username=numero,pg003estbloque=False)
                    mdu = "{}{}".format(pwd,acteur.pg003id)
                    if check_password(mdu,acteur.pg003mdp):
                        pm = Ps111.objects.filter(pg003_id=acteur, ps111statut_connexion=True)
                        if pm :
                            for i in pm:
                                i.delete()
                        connexion = Ps111()
                        connexion.ps111id = genererIdentifiant('LOGINGROUPE')
                        connexion.ps111telephone = create_key()
                        connexion.ps111statut_connexion = True
                        connexion.pg003_id = acteur
                        connexion.save()
                        token = generer_token(acteur,connexion)
                        tokenR = generer_tokenR(acteur,connexion)
                        data.append(dict({"id": acteur.pk,"authUser":token,"refreshUser":tokenR}))
                        return retour(200, data)
                    else:
                        return retour(300, data)
                return retour(301, data)
            else:
                return retour(450, data)
        else:
            return retour(400, data)
    except:
        return retour(505, data)

@api_view(['POST'])
def refresh_user(request):
    data = []
    if verification_author(request):
        if expiration_author(request):
            ab = verification_tokenR(request)
            if ab == False:
                return retour(300, data)
            ac = ab.get("bool")
            if ac:
                pd = Pg003.objects.get(pk=ab.get("acteur"))
                connexion = Ps111.objects.get(pk=ab.get("connexion"))
                token = generer_token(pd,connexion)
                data.append({"auth_user": token})
                return retour(200, data)
            else:
                return retour(301, data)
        else:
            return retour(450, data)
    else:
        return retour(400, data)


#****************** CRUD NEW AGENT

@api_view(['POST'])
def newmember(request):
    data = []
    if verification_author(request):
        if expiration_author(request):
            if verification_token(request):
                if expiration_token(request):
                    acteur = get_id_by_token(request)
                    try:
                        ab = int(request.data['telephone'])
                    except:
                        return retour(300, data)

                    if not len(request.data['telephone']) == 10:
                        return retour(301, data)

                    if not Pg002.objects.filter(username=request.data['telephone'],is_active=True):
                        return retour(302, data)

                    member = Pg002.objects.get(username=request.data['telephone'],is_active=True)
            
                    groupe = Pg001.objects.get(pg001id=acteur.pg001_id.pg001id)
                    if Pg003.objects.filter(pg001_id = groupe,pg002_id = member):
                        return retour(304,data)
            
                    lien = Pg003()
                    lien.pg003id = genererIdentifiant("GRUSER")
                    lien.pg001_id = groupe
                    lien.pg002_id = member
                    lien.pg003admin = False
                    lien.pg003retrait = False
                    lien.pg003estbloque=False
                    otp = gen()
                    lien.pg003mdp = otp
                    lien.save()
                    data.append({"id":lien.pk,"acteur_id":member.pk,"nom":member.first_name,"prenoms":member.last_name,"mdp":otp})
                    return retour(200,data)
                else:
                    return retour(470,data)
            else:
                return retour(460,data)
        else:
            return retour(450, data)
    else:
        return retour(400, data)

##### Mdp id=2 : de09FFe1

@api_view(['DELETE'])
def delmember(request):
    data = []
    if verification_author(request):
        if expiration_author(request):
            if verification_token(request):
                if expiration_token(request):
        
                    if Pg003.objects.filter(pk = request.data['groupe_id'],pg003estbloque=False):
                        groupe = Pg003.objects.get(pk = request.data['groupe_id'])
                        groupe.pg003estbloque = True
                        groupe.save()
                        return retour(200,data)
                    return retour(300,data)
                else:
                    return retour(470,data)
            else:
                return retour(460,data)
        else:
            return retour(450, data)
    else:
        return retour(400, data)

@api_view(['PUT'])
def accordermember(request):
    data = []
    if verification_author(request):
        if expiration_author(request):
            if verification_token(request):
                if expiration_token(request):
                    if Pg003.objects.filter(pk = request.data['groupe_id'],pg003estbloque=False):
                        groupe = Pg003.objects.get(pk = request.data['groupe_id'])
                        groupe.pg003admin = True
                        groupe.pg003retrait = True
                        groupe.save()
                        return retour(200,data)
                    return retour(300,data)
                else:
                    return retour(470,data)
            else:
                return retour(460,data)
        else:
            return retour(450, data)
    else:
        return retour(400, data)

@api_view(['PUT'])
def desaccordermember(request):
    data = []
    if verification_author(request):
        if expiration_author(request):
            if verification_token(request):
                if expiration_token(request):
                    if Pg003.objects.filter(pk = request.data['groupe_id'],pg003estbloque=False):
                        groupe = Pg003.objects.get(pk = request.data['groupe_id'])
                        groupe.pg003admin = False
                        groupe.pg003retrait = False
                        groupe.save()
                        return retour(200,data)
                    return retour(300,data)
                else:
                    return retour(470,data)
            else:
                return retour(460,data)
        else:
            return retour(450, data)
    else:
        return retour(400, data)

@api_view(['GET'])
def readmember(request):
    data = []
    if verification_author(request):
        if expiration_author(request):
            if verification_token(request):
                if expiration_token(request):
                    acteur = get_id_by_token(request)
                    if not acteur.pg003admin:
                        return retour(300,data)
                    alle = Pg003.objects.filter(pg001_id=acteur.pg001_id,pg003estbloque=False).exclude(pk=acteur.pk)
                    for i in alle:
                        d = dict()
                        d['nom']= i.pg002_id.first_name
                        d['prenoms']= i.pg002_id.last_name
                        if i.pg003admin:
                            d['droit'] = "Administrateur"
                        else:
                            d['droit'] = "Agent"
                        d['numero'] = i.pg002_id.username
                        data.append(d)
                    return retour(200,data)                    
                else:
                    return retour(470,data)
            else:
                return retour(460,data)
        else:
            return retour(450, data)
    else:
        return retour(400, data)


#****************** HOME

@api_view(['GET'])
def solde(request):
    data = []
    if verification_author(request):
        if expiration_author(request):
            if verification_token(request):
                if expiration_token(request):
                    acteur = get_id_by_token(request)
                    groupe = Pg001.objects.get(pk=acteur.pg001_id.pk)
                    if not Ps003.objects.filter(pg001_id=groupe):
                        return retour(300,data)
                    compte = Ps003.objects.get(pg001_id=groupe)
                    d = dict()
                    d['solde'] = compte.ps003morant
                    return retour(200,d)                    
                else:
                    return retour(470,data)
            else:
                return retour(460,data)
        else:
            return retour(450, data)
    else:
        return retour(400, data)

@api_view(['GET'])
def historiquepaiement(request):
    try:
        data = []
        if verification_author(request):
            if expiration_author(request):
                if verification_token(request):
                    if expiration_token(request):
                        if get_id_by_token(request) == False:
                            return retour(300,data)
                        acteur = get_id_by_token(request)
                        groupe = Pg001.objects.get(pk=acteur.pg001_id.pk)
                        if not Ps003.objects.filter(pg001_id=groupe):
                            return retour(300,data)
                        compte = Ps003.objects.get(pg001_id=groupe)
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
                        groupe = Pg001.objects.get(pk=acteur.pg001_id.pk)
                        qrcode = code_qr(groupe.pk,True)
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


@api_view(['PUT'])
def new_password(request):
    data = []
    if verification_author(request):
        if expiration_author(request):
            if verification_token(request):
                if expiration_token(request):
                    acteu = get_id_by_token(request)
                    acteur = Pg003.objects.get(pk=acteu.pk)
                    if len(request.data['oldpassword']) < 1:
                        return retour(300, data)
                    mdu = "{}{}".format(request.data['oldpassword'],acteur.pg003id)
                    if not check_password(mdu,acteur.pg003mdp):
                        return retour(301, data)
                       
                    mpu = "{}{}".format(request.data['newpassword'],acteur.pg003id)
                    acteur.pg003mdp= make_password(mpu)
                    acteur.save()
                    return retour(200, data)
                else:
                    return retour(465, data)
            else:
                return retour(460, data)
        else:
            return retour(450, data)
    else:
        return retour(400, data)