import subprocess
import requests

"""
Ce script téléchargera les iso de Scientific Linux et les enverra directement sur GDrive (dans mon cas vous avez juste a modifier le endpoint), Afin d'envoyer ses derniere
sur Archive.org à des fin de préservation, il téléchargera les iso via le mirror de Distrib Coffee (Herberger par l'IPSL)
Les liste des liens et versions sont récupéré sur le repo github en RAW, les liens sont librement consultable.
"""

#Définition du dossier principal
FOLDER="Scientific Linux"
#Définition des sources des fichiers à téléchager (A modifier par votre Repo si clone)
URL="https://raw.githubusercontent.com/VoXaN24/Download-to-Archive/refs/heads/main/Scientific%20Linux/"

def get_version(url_base):
	url=url_base+"ver"
	response = requests.get(url)
	return response.text.splitlines()

def get_link(url_base,ver):
	url=url_base+ver
	response = requests.get(url)
	return response.text.splitlines()


list_ver=get_version(URL)
for ver in list_ver:
	list_link=get_link(URL,ver)
	for link in list_link :
		Folder_ver='2tb:'+FOLDER+'/'+ver+'/'
		subprocess.run(["rclone","copyurl",link,Folder_ver,"-a",'--progress'])