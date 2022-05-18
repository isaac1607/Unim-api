from typing import final
from django.shortcuts import render
from api.models import *
from django.http import JsonResponse
from datetime import datetime
from helpers.helpers import *
import jwt
import time
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from helpers.request import *

################################## Access User ####################

def generer_token(pd,mars):
    secret = "cr7ne!çhsiusghusèTZjkZ5(')--uz"
    d= dict({})
    d['id'] = pd.pk
    d['tel'] = mars.ps111telephone
    d['porm'] = mars.ps111id
    d['time'] = int(time.time())
    der = crypter_dico(d)
    encoded_jwt = jwt.encode(der, secret, algorithm='HS256')
    be = str(encoded_jwt)
    return be


def decoder_token(tokene):
    try:
        secret = "cr7ne!çhsiusghusèTZjkZ5(')--uz"
        decod = jwt.decode(tokene, secret, algorithms=['HS256'])
        be = dict(decod)
        return be
    except:
        return False


def verification_token(request):
    token = request.headers.get("tokenBusiness")
    inf = decoder_token(token)
    if inf == False:
        return False
    
    info = decrypter_dico(inf)

    id = int(info.get('id'))
    tel = info.get('tel')
    porm = info.get('porm')
    if Pg003.objects.filter(pk=id,pg003estbloque=False) :
        try :
            acteur = Pg003.objects.get(pk=id,pg003estbloque=False)
            print('a')
        except:
            return False
        connexion = Ps111.objects.filter(pg003_id=acteur,ps111telephone=tel,ps111id=porm,ps111statut_connexion=True)
        if connexion:
            return True
        return False
    else:
        return False

def expiration_token(request):
    timep = 3600
    token = request.headers.get("tokenBusiness")
    inf = decoder_token(token)
    if inf == False:
        return False

    info = decrypter_dico(inf)
    porm = info.get('time')
    b = time.time()
    diff = int(b) - int(porm)
    if diff <= timep:
        return True
    else:
        return False


############################# Refresh Token #################################

def generer_tokenR(pd,mars):
    secret = "cr7neymarkTyudb071017sq"
    d= dict({})
    d['id'] = pd.pk
    d['porm'] = mars.ps111id
    z = crypterMotPasse(generate_otp(2))
    mars.ps111auth = z
    mars.save()
    d['refresh'] = z
    der = crypter_dico(d)
    encoded_jwt = jwt.encode(der, secret, algorithm='HS256')
    be = str(encoded_jwt)
    return be

def decode_tokenR(token):
    a = dict({"user":"10"})
    try:
        secret = "cr7neymarkTyudb071017sq"
        decod = jwt.decode(token, secret, algorithms=['HS256'])
        be = dict(decod)
        return be
    except:
        return a

def verification_tokenR(request):
    token = request.headers.get("tokenUserR")
    inf = decode_tokenR(token)
    if inf == False:
        return False
    
    info = decrypter_dico(inf)
    id = int(info.get('id'))
    porm = info.get('porm')
    refresh = info.get('refresh')
    if Pg003.objects.filter(pk=id,pg003estbloque=False) :
        try :
            
            acteur = Pg003.objects.get(pk=id,pg003estbloque=False)
            
        except:
            return False
        connexion = Ps111.objects.filter(pg003_id=acteur,ps111auth=refresh,ps111id=porm,ps111statut_connexion=True)
        if connexion:
            pd = Ps111.objects.get(pg003_id=acteur,ps111auth=refresh,ps111id=porm,ps111statut_connexion=True)
            return dict({"acteur":acteur.pk,"connexion": pd.pk, "bool": True})
        return False
    else:
        return False

def get_id_by_token(request):
    token = request.headers.get("tokenBusiness")
    inf = decoder_token(token)
    if inf == False:
        return False

    info = decrypter_dico(inf)

    id = int(info.get('id'))
    if Pg003.objects.filter(pk=id) :
        try :
            acteur = Pg003.objects.get(pk=id)
        except:
            return False
        return acteur
    else:
        return False


#####################################""""

def code_qr(id,static):
    element = generate_element(id,static)
    url = generate_url(element)
    return url

def verif_qr(url):
    try:
        separe = separe_url(url)
        r = retrouve_element(separe)
        return r
    except:
        return False


############################# Autorisation application #################################
def generer_author(pd):
    user = pd.bac17username
    alea = crypterMotPasse(pd.bac17mdp)
    secret = "mypmdfgghidnjdsjnds{klsl~l#'à^_"
    encoded_jwt = jwt.encode({"bete":user,"stack":int(time.time()),"bonheur":alea},secret, algorithm='HS256')
    be = str(encoded_jwt)
    return be


def decode_author(token):
    try:
        secret = "mypmdfgghidnjdsjnds{klsl~l#'à^_"
        decod = jwt.decode(token, secret, algorithms=['HS256'])
        be = dict(decod)
        return be
    except:
        return False

def verification_author(request):
    token = request.headers.get("token")
    info = decode_author(token)
    if info == False:
        return False
    user = info.get('bete')
    alea = info.get('bonheur')
    kl = Bac17.objects.filter(bac17username=user)
    if kl:
        pd =  Bac17.objects.get(bac17username=user)
        if crypterMotPasse(pd.bac17mdp) == alea:
            return True
        return False
    else:
        return False

def expiration_author(request):
    TEMPS = 3600
    token = request.headers.get("token")
    info = decode_author(token)
    b = time.time()
    diff = int(b) - int(info.get("stack"))
    if diff <= TEMPS:
        return True
    else:
        return False

############################# Refresh application #################################
def generer_authorR(pd):
    user = pd.bac17username
    alea = crypterMotPasse(pd.bac17refresh)
    pd.save()
    secret = "mlzekdrhrhjjhjfjreuikreuk"
    encoded_jwt = jwt.encode({"user":user,"bonheur":alea},secret, algorithm='HS256')
    be = str(encoded_jwt)
    return be

def decode_authorR(token):
    try:
        secret = "mlzekdrhrhjjhjfjreuikreuk"
        decod = jwt.decode(token, secret, algorithms=['HS256'])
        be = dict(decod)
        return be
    except:
        return False

def verification_authorR(request):
    pd = 0
    token = request.headers.get("tokenR")
    info = decode_authorR(token)
    if info == False:
        return dict({"user":pd,"bool":False})
    user = info.get('user')
    alea = info.get('bonheur')

    if not Bac17.objects.filter(bac17username=user):
        return dict({"user":pd,"bool":False})
    kl = Bac17.objects.get(bac17username=user)
    if crypterMotPasse(kl.bac17refresh) == alea:
        pd = Bac17.objects.get(bac17username=user)
        return dict({"user":pd.bac17username,"bool":True})
    else:
        return dict({"user":pd,"bool":False})

