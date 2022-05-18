# Generated by Django 4.0.3 on 2022-05-03 00:51

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pg001',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pg001id', models.CharField(max_length=500, unique=True)),
                ('pg001raisonSocial', models.CharField(max_length=5000, verbose_name='Nom du groupe')),
                ('pg001sigle', models.CharField(blank=True, max_length=5000, null=True, verbose_name='SIGLE')),
                ('pg001capitalsocial', models.PositiveIntegerField(blank=True, null=True, verbose_name='Capital social')),
                ('pg001siegeSocial', models.CharField(blank=True, max_length=5000, null=True, verbose_name='Siège social')),
                ('pg001anneeCreation', models.DateField(blank=True, null=True, verbose_name='Année Creation')),
                ('pg001adresse', models.CharField(blank=True, max_length=500, null=True, verbose_name='Adresse')),
                ('pg001email', models.EmailField(blank=True, max_length=500, null=True, verbose_name='Mail')),
                ('pg001siteWeb', models.CharField(blank=True, max_length=250, null=True, verbose_name='Site web')),
                ('pg001numeroRegistreCommerce', models.CharField(blank=True, max_length=500, null=True, verbose_name='Numero registre commerce')),
                ('pg001numeroEntreprise', models.CharField(blank=True, max_length=500, null=True, verbose_name='Numero entreprise')),
                ('pg001photo', models.ImageField(blank=True, null=True, upload_to='groupe/%Y/%m/%d/', verbose_name="Lien d'image")),
                ('pg001identifie', models.BooleanField(blank=True, default=False, null=True, verbose_name='Identifié ?')),
                ('pg001test', models.BooleanField(default=False, verbose_name='Test')),
                ('pg001compte_valide', models.BooleanField(default=True, verbose_name='Test')),
                ('dateCreation', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
                ('dateModification', models.DateTimeField(auto_now=True, verbose_name='Date de modification')),
            ],
            options={
                'verbose_name': 'Entreprise',
                'ordering': ['pg001raisonSocial'],
            },
        ),
        migrations.CreateModel(
            name='Pg002',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('pg002id', models.CharField(max_length=500, unique=True)),
                ('pg002sexe', models.CharField(choices=[('M', 'MASCULIN'), ('F', 'FEMININ')], max_length=500, verbose_name='Sexe')),
                ('pg002photo', models.ImageField(blank=True, null=True, upload_to='personne/%Y/%m/%d/', verbose_name="Lien d'image")),
                ('pg002date_naissance', models.DateField(blank=True, null=True, verbose_name='Date de naissance')),
                ('pg002lieu_naissance', models.CharField(blank=True, max_length=500, null=True, verbose_name='Lieu de naissance')),
                ('pg002numeroidentification', models.CharField(blank=True, max_length=500, null=True, verbose_name='Numéro identification')),
                ('pg002typiece', models.CharField(blank=True, choices=[('CNI', 'CNI'), ('PASSEPORT', 'PASSEPORT'), ('PDC', 'PERMIS DE CONDUIRE'), ('AUTRES', 'AUTRES')], max_length=500, null=True, verbose_name='Numéro identification')),
                ('pg002photo_identification', models.ImageField(blank=True, null=True, upload_to='identification/%Y/%m/%d/', verbose_name="Lien d'image")),
                ('pg002identifie', models.BooleanField(default=False, verbose_name='Identifié ?')),
                ('pg002auth', models.CharField(blank=True, max_length=5000, null=True, verbose_name='Auth')),
                ('pg002qrcode', models.CharField(blank=True, max_length=5000, null=True, verbose_name='Qr code')),
                ('pg002otp', models.CharField(blank=True, max_length=5000, null=True, verbose_name='Code OTP')),
                ('pg002otp_expired', models.IntegerField(blank=True, null=True, verbose_name='Temps expiration')),
                ('pg002test', models.BooleanField(default=False, verbose_name='Test')),
                ('pg002compte_valide', models.BooleanField(default=True, verbose_name='Test')),
                ('dateCreation', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
                ('dateModification', models.DateTimeField(auto_now=True, verbose_name='Date de modification')),
            ],
            options={
                'verbose_name': 'Personne',
                'ordering': ['username'],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Pg103',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pg103libele', models.CharField(max_length=500, unique=True)),
                ('dateCreation', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
                ('dateModification', models.DateTimeField(auto_now=True, verbose_name='Date de modification')),
            ],
            options={
                'verbose_name': 'Forme Juridique',
                'ordering': ['pg103libele'],
            },
        ),
        migrations.CreateModel(
            name='Pg104',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pg104libele', models.CharField(max_length=500, unique=True)),
                ('dateCreation', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
                ('dateModification', models.DateTimeField(auto_now=True, verbose_name='Date de modification')),
            ],
            options={
                'verbose_name': "Secteur d'activité",
                'ordering': ['pg104libele'],
            },
        ),
        migrations.CreateModel(
            name='Pg105',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pg105tranche', models.IntegerField(verbose_name='tranche')),
                ('pg105frais', models.FloatField(verbose_name='frais')),
                ('dateCreation', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
                ('dateModification', models.DateTimeField(auto_now=True, verbose_name='Date de modification')),
            ],
            options={
                'verbose_name': 'Frais',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='Ps111',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ps111id', models.CharField(max_length=500, unique=True)),
                ('ps111telephone', models.CharField(max_length=500, verbose_name='Marque')),
                ('ps111imei', models.CharField(blank=True, max_length=500, null=True, unique=True, verbose_name='Imei')),
                ('ps111auth', models.CharField(blank=True, max_length=5000, null=True, verbose_name='Auth')),
                ('ps111code', models.CharField(blank=True, max_length=500, null=True, verbose_name='Code')),
                ('ps111statut_connexion', models.BooleanField(default=False, verbose_name='Connecté ?')),
                ('ps111statut_enregistre', models.BooleanField(default=False, verbose_name='Enregistré ?')),
                ('ps111statut_valide', models.BooleanField(default=False, verbose_name='Valide ou pas')),
                ('dateCreation', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
                ('dateModification', models.DateTimeField(auto_now=True, verbose_name='Date de modification')),
                ('pg002_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.pg002', verbose_name='Personne')),
            ],
            options={
                'verbose_name': 'Personne',
                'ordering': ['ps111id'],
            },
        ),
        migrations.CreateModel(
            name='Ps110',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ps110id', models.CharField(max_length=500, unique=True)),
                ('ps110telephone', models.CharField(max_length=500, verbose_name='Marque')),
                ('ps110imei', models.CharField(blank=True, max_length=500, null=True, unique=True, verbose_name='Imei')),
                ('ps110auth', models.CharField(blank=True, max_length=5000, null=True, verbose_name='Auth')),
                ('ps110code', models.CharField(blank=True, max_length=500, null=True, verbose_name='Code')),
                ('ps110statut_connexion', models.BooleanField(default=False, verbose_name='Connecté ?')),
                ('ps110statut_enregistre', models.BooleanField(default=False, verbose_name='Enregistré ?')),
                ('ps110statut_valide', models.BooleanField(default=False, verbose_name='Valide ou pas')),
                ('dateCreation', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
                ('dateModification', models.DateTimeField(auto_now=True, verbose_name='Date de modification')),
                ('pg002_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.pg002', verbose_name='Personne')),
            ],
            options={
                'verbose_name': 'Personne',
                'ordering': ['ps110id'],
            },
        ),
        migrations.CreateModel(
            name='Ps003',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ps003id', models.CharField(max_length=500, unique=True)),
                ('ps003numero_compte', models.IntegerField(unique=True, verbose_name='Numéro de compte')),
                ('ps003morant', models.FloatField(verbose_name='Morant')),
                ('ps003auth_recep', models.CharField(max_length=500, verbose_name='clé reception statique')),
                ('ps003auth_recepStatique', models.CharField(max_length=500, verbose_name='clé réception statique')),
                ('ps003auth_pay', models.CharField(blank=True, max_length=5, null=True, verbose_name='Dépassement accepté')),
                ('ps003estbloque', models.BooleanField(default=False, verbose_name='Bloquer le compte')),
                ('ps003compte_groupe', models.BooleanField(default=False, verbose_name='Valide ou pas')),
                ('statut_valide', models.BooleanField(default=True, verbose_name='Valide ou pas')),
                ('compte_test', models.BooleanField(default=False, verbose_name='Test ou pas')),
                ('dateCreation', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
                ('dateModification', models.DateTimeField(auto_now=True, verbose_name='Date de modification')),
                ('pg001_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='api.pg001', verbose_name='Groupe')),
                ('pg002_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='api.pg002', verbose_name='Personne')),
            ],
            options={
                'verbose_name': 'Compte',
                'ordering': ['ps003numero_compte'],
            },
        ),
        migrations.CreateModel(
            name='Pg101',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pg101id', models.CharField(max_length=500, verbose_name='Identifiant')),
                ('pg101numTransaction', models.CharField(max_length=500, verbose_name='numéro transaction')),
                ('pg101somme_initial', models.FloatField(verbose_name='somme')),
                ('pg101somme', models.FloatField(verbose_name='somme')),
                ('pg101frais', models.FloatField(verbose_name='frais_api')),
                ('pg101info_api', models.CharField(blank=True, max_length=500, null=True, verbose_name='Info API')),
                ('pg101info_api2', models.CharField(blank=True, max_length=500, null=True, verbose_name='Info API 2')),
                ('pg101info_api3', models.CharField(blank=True, max_length=500, null=True, verbose_name='Info API 3')),
                ('pg101state', models.BooleanField(verbose_name='Etat de la recharge')),
                ('dateCreation', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
                ('dateModification', models.DateTimeField(auto_now=True, verbose_name='Date de modification')),
                ('ps003code', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.ps003', verbose_name='Compte')),
            ],
            options={
                'verbose_name': 'Historique des rechargements',
                'ordering': ['pg101id'],
            },
        ),
        migrations.CreateModel(
            name='Pg100',
            fields=[
                ('pg100id', models.AutoField(primary_key=True, serialize=False)),
                ('pg101numTransaction', models.CharField(max_length=500, unique=True, verbose_name='numéro transaction')),
                ('pg100somme_initial', models.FloatField(max_length=500, verbose_name='somme initial')),
                ('pg100somme', models.FloatField(max_length=500, verbose_name='solde_envoye')),
                ('pg100state', models.BooleanField(default=True, verbose_name='Etat')),
                ('dateCreation', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
                ('dateModification', models.DateTimeField(auto_now=True, verbose_name='Date de modification')),
                ('pg105_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='Envoi', to='api.pg105', verbose_name='Frais')),
                ('ps003codeEnvoi', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='Envoi', to='api.ps003', verbose_name='Compte envoi')),
                ('ps003codeRecu', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='Recu', to='api.ps003', verbose_name='Compte reçu')),
            ],
            options={
                'verbose_name': 'Historique de rechargement',
                'ordering': ['pg100id'],
            },
        ),
        migrations.CreateModel(
            name='Pg003',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pg003id', models.CharField(max_length=500, unique=True)),
                ('pg003mdp', models.IntegerField(verbose_name='Mot de passe')),
                ('pg003plafond', models.IntegerField(verbose_name='Plafond')),
                ('pg003depot', models.BooleanField(default=False, verbose_name='Droit de depot')),
                ('pg003retrait', models.BooleanField(default=False, verbose_name='Droit de retrait')),
                ('pg003payer', models.BooleanField(default=False, verbose_name='Droit de payer')),
                ('pg003recevoir', models.BooleanField(default=False, verbose_name='Droit de réception')),
                ('pg003admin', models.BooleanField(default=False, verbose_name='Administrateur')),
                ('pg003estbloque', models.BooleanField(default=False, verbose_name='Bloquer le compte')),
                ('state_valide', models.BooleanField(default=True, verbose_name='Suppression')),
                ('dateCreation', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
                ('dateModification', models.DateTimeField(auto_now=True, verbose_name='Date de modification')),
                ('pg001_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.pg001', verbose_name='Groupe')),
                ('pg002_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.pg002', verbose_name='Personne')),
            ],
            options={
                'verbose_name': 'Groupe_Personne',
                'ordering': ['pg003id'],
            },
        ),
        migrations.AddField(
            model_name='pg002',
            name='pg001_id',
            field=models.ManyToManyField(blank=True, related_name='Relation', through='api.Pg003', to='api.pg001'),
        ),
        migrations.AddField(
            model_name='pg001',
            name='pg103_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.pg103', verbose_name='Forme juridique'),
        ),
        migrations.AddField(
            model_name='pg001',
            name='pg104_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.pg104', verbose_name="Secteur d'activité"),
        ),
    ]