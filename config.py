import requests

class Config:
	def loadCookie(self):
		try:
			file = open('log/cookies.log','r')
			cookie = file.read()
			file.close()
			return cookie.strip()
		except IOError:
			return False

	def banner(self):
		return '''\n
\033[0;96m▒█▀▄▀█ █▀▀█ █▀▀▄ ░░ █▀▀▄ █▀▀ \033[0m|| Author : Dullah ID
\033[0;96m▒█▒█▒█ █▄▄█ █░░█ ▀▀ █▀▀▄ █▀▀ \033[0m|| Recode : Hilman XD 
\033[0;96m▒█░░▒█ ▀░░▀ ▀░░▀ ░░ ▀▀▀░ ▀░░ \033[0;91mv2.0 \033[0m|| FB.me/xxx.hilmanxd'''

	def httpRequest(self, url, cookies):
		try:
			return requests.get(url, cookies = {'cookie': cookies}).text
		except requests.exceptions.RequestException:
			exit('\n\n\033[0;91mConnection error, check your connection!!\033[0m')

	def httpRequestPost(self, url, cookies, params):
		try:
			return requests.post(url, data = params, cookies = {'cookie': cookies}).text
		except requests.exceptions.RequestException:
			exit('\n\n\033[0;91mConnection error, check your connection!!\033[0m')
