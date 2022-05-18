from api.models import *
from .helpers import *
from django.contrib.auth.hashers import make_password

"""
class Dcbr:
	def remplirbd(self):
		fonction = ['SOCIETE INDIVIDUELLE (SI)', 'SOCIETE ANONYME (SA)', 'SARL','AUTRES']
		for i in range(len(fonction)):
			Pg103.objects.create(pg103libele = fonction[i])

		secteurDactivite = ['INDUSTRIE', 'TRANSPORT', 'AGRICULTURE','FINANCE','SANTE','TIC','AUTRES']
		for i in range(len(secteurDactivite)):
			Pg104.objects.create(pg104libele = secteurDactivite[i])

		name = crypterMotPasse("devenir_number1")
		mdp = make_password("testercocamenthe")
		Bac17.objects.create(bac17username=name, bac17mdp=mdp,bac17refresh=genererIdentifiant("MOINE"))

		nam = crypterMotPasse("deveweb_number1")
		md = make_password("webtestercocamentheweb")
		Bac17.objects.create(bac17username=nam, bac17mdp=md,bac17refresh=genererIdentifiant("MOINE"))


def compte_cinit():
	Ps003.objects.create(ps003id = genererIdentifiant('CINIT'),ps003numero_compte = generate_otp(6),ps003plafond=0,ps003compte_cinit = True,ps003timetransaction=0,ps003timesomme=0)

"""