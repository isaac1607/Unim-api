from rest_framework.serializers import ModelSerializer
from rest_framework import serializers 
from api.models import *

class HistoriqueSerializer(ModelSerializer):
	somme = serializers.CharField(source="pg100somme")
	somme = serializers.CharField(source="pg100somme")
	class Meta:
		model = Pg100
		fields = ['somme', 'prenoms', 'id', 'telephone',
				  'type', 'groupe_id', 'password']


class GroupeSerializer(ModelSerializer):
	raisonSocial = serializers.CharField(source="pg001raisonSocial")
	secteur = serializers.CharField(source="pg001secteur")
	type = serializers.CharField(source="pg001type")
	siege = serializers.CharField(source="pg001siegeSocial")
	identifiant = serializers.CharField(source="pg001identifiant")

	class Meta:
		model = Pg001
		fields = ['raisonSocial', 'secteur', 'siege','type', 'pg001id','identifiant']
