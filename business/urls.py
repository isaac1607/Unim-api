from django.urls import path
from .views import *


urlpatterns = [
	#Processus de création d'un groupe
	path('create_groupe/',create_groupe, name='create_groupe'),
	path('verification_otp/',validation_groupe, name='validation_groupe'),
	path('generer_otp/',generer_otp_groupe, name='generer_otp_groupe'),
	path('new_mot_passe/',enregistrer_password, name='enregistrer_password'),
	path('new_information/',newinformation, name='new_information'),
	path('generer_otp_retrait/',generer_otp_retrait, name='generer_otp_retrait'),
	path('validation_retrait/',validation_retrait, name='validation_retrait'),
	path('connexion/',connexion, name='connexion'),
	path('refresh_user/',refresh_user, name='refresh_user'),
	path('new_member/',newmember, name='newmember'),
	path('del_member/',delmember, name='delmember'),
	path('accorder_member/',accordermember, name='accordermember'),
	path('desaccorder_member/',desaccordermember, name='accordermember'),
	path('read_member/',readmember, name='readmember'),
	path('solde/',solde, name='solde'),
	path('historique_transaction/',historiquepaiement, name='historiquepaiement'),
	path('qrcode', qrcode, name='qrcode'),
	path('scanqrcode', scanqrcode, name='scanqrcode'),
	path('changepassword/', new_password, name='new_password'),
	
]
