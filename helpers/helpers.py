from django.shortcuts import render
from django.http import JsonResponse
import json
import hashlib
import random
from cryptography.fernet import Fernet


def generate_qr(messag):
    key = Fernet.generate_key()
    f = Fernet(key)
    token = f.encrypt(str.encode(messag))
    ab = f.decrypt(token).decode()
    data = {"key": key.decode(), "token": token.decode()}
    return data


def melange(s):
    ab = ''.join(random.sample(s, len(s)))
    return ab


def retour(numero, donnee):
    data = dict({"status": numero, "data": donnee})
    return JsonResponse(data)


def genererIdentifiant(identifiant):
    from datetime import datetime
    timeToday = datetime.now()
    strTimeToday = timeToday.strftime('%y%m%d%I%M%S')
    identifiantgenere = "{}{}".format(identifiant, strTimeToday)
    return identifiantgenere


def generate_otp(number):
    import random
    import string
    length = number
    str = string.digits
    return ''.join(random.choice(str) for i in range(length))


def gen():
    import random
    import string
    length = 8
    str = string.hexdigits
    return ''.join(random.choice(str) for i in range(length))


def genererMotPasse(b):
    import random
    import string
    listeDesElementsDuMotDePasse = list(string.printable)
    motDePass = []
    for elt in range(b):
        motDePass.append(random.choice(list(string.printable)))
    motDePass = "".join(motDePass)
    return motDePass


def crypterMotPasse(motPasse):
    motPasseEncode = motPasse.encode()
    motPassChiffre = hashlib.sha512(motPasseEncode).hexdigest()
    return motPassChiffre

def evaluate_time(a, choix):
    import time
    b = time.time()
    diff = int(b) - int(a)
    if diff <= choix:
        return True
    else:
        return False


URL_BASE = "https://qr.unim.com"


def dictionnaire_i():
    d = dict()
    d['p'] = 0
    d['W'] = 1
    d['z'] = 2
    d['!'] = 3
    d['$'] = 4
    d['k'] = 5
    d['Z'] = 6
    d['g'] = 7
    d['Q'] = 8
    d['n'] = 9
    d['N'] = 10
    d['K'] = 11
    d['L'] = 12
    d['x'] = 13
    d['b'] = 14
    d['P'] = 15
    d['y'] = 16
    d['A'] = 17
    d['a'] = 18
    d['I'] = 19
    d['X'] = 20
    d['w'] = 21
    d['e'] = 22
    d[')'] = 23
    d['('] = 24
    d['i'] = 25
    d['c'] = 26
    return d

#################################"  HELPERS
def correspondance(val):
    d= dictionnaire_i()
    keys = [k for k, v in d.items() if v == val]
    if keys:
        return keys[0]
    return False

def conversion(num):
    d = dictionnaire_i()
    try:
        return d[num]
    except:
        return False


def Convert(string):
    L = []
    for i in string:
        L.append(i)
    return L
#####################
    

def generate_element(id,typez):
    ide = str(id)

    position_id = random.randint(3, 13)
    position_finid = position_id + len(ide)-1
    position_type = position_finid + 1

    a = correspondance(position_id)
    b = correspondance(position_finid)
    c = correspondance(position_type)
    L= [a,b,c]

    i = 3
    if i == position_id:
        for ab in ide:

            L.append(correspondance(int(ab)))       
    else:
        while i<position_id:
            laya = genererMotPasse(1)
            L.append(laya)
            i = i + 1 
        for ab in ide:
            L.append(correspondance(int(ab)))

    ################### groupe = True        
    if typez:
        L.append(correspondance(11))
    L.append(correspondance(10))

    if len(L)<15 :
        af = 15 - len(L)
        i = 0
        while i < af:
            laya = genererMotPasse(1)
            L.append(laya)
            i = i + 1 
    else:
        i=0
        while i < 5:
            laya = genererMotPasse(1)
            L.append(laya)
            i = i + 1 
    str1 = ''.join(L)
    return str1



def retrouve_element(el):
    element = Convert(el)
    position_id = conversion(element[0])
    position_finid = conversion(element[1])
    position_type = conversion(element[2])

    L= element[position_id:position_finid+1]
    B= element[position_finid+1]

    B = [conversion(B[0])]
    type = ''.join(str(e) for e in B)
    id = []
    for i in L:
        id.append(conversion(i))
    
    numero = ''.join(str(e) for e in id)

    num = int(numero)
    typ = int(type)
    er = dict({"id":num,"type":typ})
    return er

def genererMotPasse(b):
    import random, string
    motDePass = []
    for elt in range(b): 
        motDePass.append(random.choice(list(string.ascii_letters + string.digits)))
    motDePass = "".join(motDePass)
    return motDePass


def generate_url(element):
    messag = genererMotPasse(10)
    url = "{}/{}/{}".format(URL_BASE,element,messag)
    return url

def separe_url(url):
    L = url[len(URL_BASE)+1:]
    string = ''.join(L)
    ab = string.split("/")
    e = ab[0]
    return e

