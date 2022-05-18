from django.db import models
from django.contrib.auth.models import User



######### *******************************************  PREREQUIS  ************************************

class Pg103(models.Model): ### Forme juridique

    pg103libele = models.CharField(unique=True,max_length = 200)

    dateCreation = models.DateTimeField(auto_now_add = True, verbose_name = 'Date de création')
    dateModification = models.DateTimeField(auto_now = True, verbose_name = 'Date de modification')

    class Meta:
        verbose_name = "Forme Juridique"
        ordering = ['pg103libele']

    def __str__(self):
        return self.pg103libele


class Pg104(models.Model): ### Secteur d'activité

    pg104libele = models.CharField(unique=True,max_length = 200)

    dateCreation = models.DateTimeField(auto_now_add = True, verbose_name = 'Date de création')
    dateModification = models.DateTimeField(auto_now = True, verbose_name = 'Date de modification')

    class Meta:
        verbose_name = "Secteur d'activité"
        ordering = ['pg104libele']

    def __str__(self):
        return self.pg104libele


######### *******************************************  DEFINITION DES ACTEURS ************************************


class Pg001(models.Model): # Entreprise
    TYPE = [
    ('SI', 'SOCIETE INDIVIDUELLE'),
    ('SARL', 'SARL'),
    ('SA', 'SA'),
    ('AUTRES', 'AUTRES'),
    ]

    SECTEUR = [
    ('TRANSPORT', 'TRANSPORT'),
    ('INDUSTRIE', 'INDUSTRIE'),
    ('FINANCE', 'FINANCE'),
    ('SANTE', 'SANTE'),
    ('TIC', 'TIC'),
    ('AUTRES', 'AUTRES'),
    ]

    pg001id = models.CharField(unique=True,max_length = 200)
    pg001identifiant = models.CharField(unique=True,max_length = 200)

    pg001raisonSocial = models.CharField(max_length = 200, verbose_name = 'Nom du groupe')
    pg001sigle = models.CharField(max_length = 200, verbose_name = 'SIGLE',blank=True, null=True)
    pg001capitalsocial = models.PositiveIntegerField(verbose_name = 'Capital social',blank=True, null=True)
    pg001siegeSocial = models.CharField(max_length = 200, verbose_name = 'Siège social',blank=True, null=True)

    pg001anneeCreation = models.DateField(verbose_name='Année Creation', null=True, blank=True)
    pg001adresse = models.CharField(verbose_name="Adresse",blank = True, null = True,max_length = 200)
    pg001email = models.EmailField(max_length = 200, verbose_name = 'Mail',blank=True, null=True)

    pg001siteWeb = models.CharField(max_length=200, verbose_name='Site web', null=True, blank=True)


    pg001telephone = models.CharField(max_length=200, verbose_name='Retrait', null=True, blank=True)
    pg001otp = models.CharField(max_length = 200, verbose_name = 'Code OTP',blank=True, null=True)
    pg001otp_expired = models.IntegerField(verbose_name = 'Temps expiration',blank=True, null=True)

    pg001numeroRegistreCommerce = models.CharField(max_length = 200, verbose_name = 'Numero registre commerce',blank=True, null=True)
    pg001numeroEntreprise = models.CharField(max_length = 200, verbose_name = 'Numero entreprise',blank=True, null=True)

    pg001photo = models.ImageField(upload_to = 'groupe/%Y/%m/%d/', blank = True, null = True, verbose_name = "Lien d'image")
    pg001identifie = models.BooleanField(default=False,verbose_name="Identifié ?",blank = True, null = True,)

    pg001test = models.BooleanField(default=False,verbose_name="Test")
    pg001compte_valide = models.BooleanField(default=True,verbose_name="Test")

    pg001secteur = models.CharField(max_length = 200, verbose_name = 'Secteur',choices=SECTEUR)
    pg001type = models.CharField(max_length = 200, verbose_name = 'Type',choices=TYPE)

    dateCreation = models.DateTimeField(auto_now_add = True, verbose_name = 'Date de création')
    dateModification = models.DateTimeField(auto_now = True, verbose_name = 'Date de modification')

    class Meta:
        verbose_name = "Entreprise"
        ordering = ['pg001raisonSocial']

    def __str__(self):
        return self.pg001raisonSocial

class Pg002(User): #Personne
    SEXE = [
    ('M', 'MASCULIN'),
    ('F', 'FEMININ'),
    ]

    PIECE = [
    ('CNI', 'CNI'),
    ('PASSEPORT', 'PASSEPORT'),
    ('PDC', 'PERMIS DE CONDUIRE'),
    ('AUTRES', 'AUTRES'),
    ]

    pg002id = models.CharField(unique=True,max_length = 200)
    pg002ps = models.CharField(max_length = 200, verbose_name = 'ps',blank=True, null=True)
    ######################## Identifiants humains
    pg002sexe = models.CharField(max_length = 200, verbose_name = 'Sexe',choices=SEXE)
    pg002photo = models.ImageField(upload_to = 'personne/%Y/%m/%d/', blank = True, null = True, verbose_name = "Lien d'image")
    pg002date_naissance = models.DateField(verbose_name = 'Date de naissance',null = True, blank = True,)
    pg002lieu_naissance = models.CharField(max_length = 200, verbose_name = 'Lieu de naissance',blank=True, null=True)


    ############################ Identification
    pg002numeroidentification = models.CharField(max_length = 200, verbose_name = 'Numéro identification',blank=True, null=True)
    pg002typiece= models.CharField(max_length = 200, verbose_name = 'Numéro identification',blank=True, null=True, choices=PIECE)
    pg002photo_identification = models.ImageField(upload_to = 'identification/%Y/%m/%d/', blank = True, null = True, verbose_name = "Lien d'image")
    pg002identifie = models.BooleanField(default=False,verbose_name="Identifié ?")

    ############################################# Sécurité
    pg002auth = models.TextField(verbose_name = 'Auth',blank=True, null=True)
    pg002qrcode = models.TextField(verbose_name = 'Qr code',blank=True, null=True)
    pg002otp = models.CharField(max_length = 200, verbose_name = 'Code OTP',blank=True, null=True)
    pg002otp_expired = models.IntegerField(verbose_name = 'Temps expiration',blank=True, null=True)

    
    pg001_id = models.ManyToManyField("Pg001",through = 'Pg003',related_name="Relation",blank=True)

    pg002test = models.BooleanField(default=False,verbose_name="Test")

    dateCreation = models.DateTimeField(auto_now_add = True, verbose_name = 'Date de création')
    dateModification = models.DateTimeField(auto_now = True, verbose_name = 'Date de modification')

    class Meta:
        verbose_name = "Personne"
        ordering = ['username']

    def __str__(self):
        return self.username


class Pg003(models.Model): #Groupe_Personne
    
    pg003id = models.CharField(unique=True,max_length = 200)

    pg003mdp = models.CharField(verbose_name = 'Mot de passe',max_length = 200,blank=True, null=True)

    pg003otp = models.CharField(max_length = 200, verbose_name = 'Code OTP',blank=True, null=True)
    pg003otp_expired = models.IntegerField(verbose_name = 'Temps expiration',blank=True, null=True)

    ####################Plafond
    pg003plafond = models.IntegerField(verbose_name = 'Plafond',default=0)

    ############################# Droit
    pg003depot = models.BooleanField(default=False, verbose_name = 'Droit de depot')
    pg003retrait = models.BooleanField(default=False, verbose_name = 'Droit de retrait')
    pg003payer = models.BooleanField(default=False, verbose_name = 'Droit de payer')
    pg003recevoir = models.BooleanField(default=False, verbose_name = 'Droit de réception')

    #####################Administrateur
    pg003admin = models.BooleanField(default=False,verbose_name = 'Administrateur')

    pg003estbloque = models.BooleanField(default = True, verbose_name = 'Bloquer le compte')

    pg001_id = models.ForeignKey(Pg001, on_delete = models.RESTRICT, verbose_name = 'Groupe',)
    pg002_id = models.ForeignKey(Pg002, on_delete = models.RESTRICT, verbose_name = 'Personne')

    state_valide = models.BooleanField(default=True,verbose_name = 'Suppression')
    dateCreation = models.DateTimeField(auto_now_add = True, verbose_name = 'Date de création')
    dateModification = models.DateTimeField(auto_now = True, verbose_name = 'Date de modification')

    class Meta:
        verbose_name = "Groupe_Personne"
        ordering = ['pg003id']

    def __str__(self):
        return self.pg003id


######### *******************************************  PARAMETRES DE CONNEXION  ************************************

class Ps110(models.Model): # Connexion

    ps110id = models.CharField(unique=True,max_length = 200)

    ps110telephone = models.CharField(max_length = 200, verbose_name = 'Marque')

    ps110auth = models.TextField(verbose_name = 'Auth',blank=True, null=True)

    ps110statut_connexion = models.BooleanField(verbose_name="Connecté ?",default=False)

    pg002_id = models.ForeignKey(Pg002, on_delete = models.RESTRICT, verbose_name = 'Personne')

    dateCreation = models.DateTimeField(auto_now_add = True, verbose_name = 'Date de création')
    dateModification = models.DateTimeField(auto_now = True, verbose_name = 'Date de modification')

    class Meta:
        verbose_name = "Personne"
        ordering = ['ps110id']

    def __str__(self):
        return self.ps110id

class Ps111(models.Model): # Connexion Business

    ps111id = models.CharField(unique=True,max_length = 200)

    ps111telephone = models.CharField(max_length = 200, verbose_name = 'Marque')

    ps111auth = models.TextField(verbose_name = 'Auth',blank=True, null=True)

    ps111statut_connexion = models.BooleanField(verbose_name="Connecté ?",default=False)

    pg003_id = models.ForeignKey(Pg003, on_delete = models.RESTRICT, verbose_name = 'Business')

    dateCreation = models.DateTimeField(auto_now_add = True, verbose_name = 'Date de création')
    dateModification = models.DateTimeField(auto_now = True, verbose_name = 'Date de modification')

    class Meta:
        verbose_name = "Personne"
        ordering = ['ps111id']

    def __str__(self):
        return self.ps111id



######### *******************************************  COMPTE  ************************************

class Ps003(models.Model): #Compte

    ps003id = models.CharField(max_length = 200,unique = True)

    ps003numero_compte = models.BigIntegerField(unique = True, verbose_name = 'Numéro de compte')
    ps003morant = models.FloatField(verbose_name = 'Morant',default=0)

    ps003estbloque = models.BooleanField(default = False, verbose_name = 'Bloquer le compte')
    ps003plafond = models.IntegerField(verbose_name = 'Plafond')

    ps003compte_groupe = models.BooleanField(default=False,verbose_name="Valide ou pas")
    pg002_id = models.ForeignKey(Pg002, on_delete = models.RESTRICT, verbose_name = 'Personne',blank = True, null = True)
    pg001_id = models.ForeignKey(Pg001, on_delete = models.RESTRICT, verbose_name = 'Groupe',blank = True, null = True)

    ps003compte_cinit = models.BooleanField(default=False)
    statut_valide = models.BooleanField(default=True,verbose_name="Valide ou pas")

    ps003timetransaction = models.BigIntegerField(verbose_name = 'Plafond')
    ps003timesomme = models.FloatField(verbose_name = 'Plafond')

    dateCreation = models.DateTimeField(auto_now_add = True, verbose_name = 'Date de création')
    dateModification = models.DateTimeField(auto_now = True, verbose_name = 'Date de modification')

    def __str__(self):
        return self.ps003numero_compte

    class Meta:
        verbose_name = "Compte"
        ordering = ['ps003numero_compte']



class Pg100(models.Model): #historique des transactions


    pg100id = models.AutoField(primary_key = True)
    pg101numTransaction = models.CharField(unique=True, max_length = 200, verbose_name= "numéro transaction")

    pg100somme_initial = models.FloatField(max_length = 200, verbose_name = 'somme initial')    
    pg100somme = models.FloatField(verbose_name = 'solde_envoye')
    pg100state = models.BooleanField(verbose_name = 'Etat',default=True)

    ps003codeEnvoi = models.ForeignKey(Ps003, on_delete = models.RESTRICT, verbose_name = 'Compte envoi',related_name='Envoi')
    ps003codeRecu = models.ForeignKey(Ps003, on_delete = models.RESTRICT, verbose_name = 'Compte reçu',related_name = 'Recu')

    pg100frais = models.FloatField(verbose_name = 'Frais')

    dateCreation = models.DateTimeField(auto_now_add = True, verbose_name = 'Date de création')
    dateModification = models.DateTimeField(auto_now = True, verbose_name = 'Date de modification')

    class Meta:
        verbose_name = "Historique de rechargement"
        ordering = ['pg100id']

    def __str__(self):
        return self.pg100id


class Pg101(models.Model): #historique de rechargement du compte

    OPTION = [
    ('D', 'DEPOT'),
    ('R', 'RETRAIT'),
    ]

    pg101id = models.CharField(max_length=200, verbose_name="Identifiant")
    pg101numTransaction = models.CharField(max_length = 200, verbose_name= "numéro transaction")

    pg101somme_initial = models.FloatField(verbose_name = 'somme')
    pg101somme = models.FloatField(verbose_name = 'somme')
    pg101frais = models.FloatField( verbose_name = 'frais_api')
    
    pg101info_api= models.CharField(max_length = 200, verbose_name= "Info API",blank=True, null=True)
    pg101info_api2 = models.CharField(max_length = 200, verbose_name= "Info API 2",blank=True, null=True)
    pg101info_api3 = models.CharField(max_length = 200, verbose_name= "Info API 3",blank=True, null=True)

    pg101state = models.BooleanField(verbose_name = 'Etat de la recharge')

    ps003code = models.ForeignKey(Ps003, on_delete = models.RESTRICT, verbose_name = 'Compte')

    dateCreation = models.DateTimeField(auto_now_add = True, verbose_name = 'Date de création')
    dateModification = models.DateTimeField(auto_now = True, verbose_name = 'Date de modification')

    class Meta:
        verbose_name = "Historique des rechargements"
        ordering = ['pg101id']

    def __str__(self):
        return self.pg101id


class Bac17(models.Model): 


    bac17username = models.CharField(max_length=255, verbose_name="Identifiant")
    bac17mdp = models.CharField(max_length = 255, verbose_name= "numéro transaction")
    bac17refresh= models.CharField(max_length = 255, verbose_name= "Info API")


class Retrait(models.Model):
    somme_initiale = models.FloatField(verbose_name = 'Somme Initiale')
    somme = models.FloatField(verbose_name = 'Somme')
    frais = models.FloatField(verbose_name = 'Frais')
    caisse = models.FloatField(verbose_name = 'Caisse')
    dateCreation = models.DateTimeField(auto_now_add = True, verbose_name = 'Date de création')
    dateModification = models.DateTimeField(auto_now = True, verbose_name = 'Date de modification')