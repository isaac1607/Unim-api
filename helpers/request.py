from cryptography.fernet import Fernet

key_const = b'bEo9YC9DBzyQquobva5EeBwsyzuCSHtPLUr0YOPStQk='

def chiffre_jeton(key_const,message):
	f = Fernet(key_const)
	messag = str(message)
	token = f.encrypt(str.encode(messag))
	ab = token.decode()
	#ab = f.decrypt(token).decode()
	return ab

def dechiffrer_jeton(key_const,token):
	e = token.encode()
	f = Fernet(key_const)
	ab = f.decrypt(e).decode()
	return ab

def create_key():
	key = Fernet.generate_key()
	f = key.decode()
	return f


def crypter_dico(jsone):
	dic = {}
	for cle, valeur in jsone.items():
		if cle == '':
			b = ''
		else:
			b = chiffre_jeton(key_const,cle)

		if type(valeur) == dict:
			dic[b]=crypter_dico(valeur)
		else:
			if valeur == '':
				a = ''
			else:
				a = chiffre_jeton(key_const,valeur)
			dic[b]=a
	return dic

def decrypter_dico(jsone):
	dic = {}
	for cle, valeur in jsone.items():
		if cle == '':
			b = ''
		else:
			b = dechiffrer_jeton(key_const,cle)

		if type(valeur) == dict:
			dic[b]=decrypter_dico(valeur)
		else:
			if valeur == '':
				a = ''
			else:
				a = dechiffrer_jeton(key_const,valeur)
			dic[b]=a
	return dic
