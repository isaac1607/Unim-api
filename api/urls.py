from django.urls import path
from .views import *


urlpatterns = [
	path('demande/', demande, name='demande'),
	path('refresh/', refresh, name='refresh'),
	# path('bdd', bdd, name='bdd'),
	path('verification_numero/', verifa, name='verifa'),
	path('generer_otp/', generer_otp, name='generer_otp'),

	####******************************* PROCESSUS INSCRIPTION
	path('verification_otp/', validation, name='validation'),
	path('new_mot_passe/', enregistrer_password, name='enregistrer_password'),
	path('informations_personnelles/', newinformation, name='newinformation'),

	################### CONNEXION AFTER DECONNEXION
	path('verification_password/', verification_password, name='verification_password'),
	path('validation_afterconnexion/', validation_afterconnexion, name='validation_afterconnexion'),

	################### CONNEXION 
	path('password/', verification_password_connexion, name='verification_password_connexion'),

	################################" APPLICATION"
	path('historique/paiement', historiquepaiements, name='historiquepaiements'),
	path('qrcode', qrcode, name='qrcode'),

	#####################  Processus de paiement
	path('scanqrcode', scanqrcode, name='scanqrcode'),
	path('transfert', transfertdm, name='transfertdm'),
	

]
