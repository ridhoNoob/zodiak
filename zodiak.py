#/usr/bin/python3.7
#-*- coding: utf-8 -*-
# Author : Ridho Gaming
# github : https://github.com/ridhoNoob
# whatsapp : 083113226393
# Ngapain ?, Mau recode ?
try:
	import time,os,json,sys
except Exception as E:
	print (E)
try:
	import requests
except:
	os.system('pip install requests')
m_bold = "\033[1;91m"
b_bold = "\033[1;94m"
h_bold = "\033[1;92m"
c_bold = "\033[1;96m"
k_bold = "\033[1;93m"
m = "\033[91m"
b = "\033[94m"
h = "\033[92m"
c = "\033[96m"
k = "\033[93m"
p = "\033[0m"
__author__='Ridho Gaming'
banner=f"""
 _____         ____  _       __
/__  /  ____  / __ \(_)___ _/ /__
  / /  / __ \/ / / / / __ `/ //_/ {h}Author {m}: {k_bold}{__author__}{p}
 / /__/ /_/ / /_/ / / /_/ / ,<    {h}created {m}: {k_bold}6-11-2019{p}
/____/\____/_____/_/\__,_/_/|_|
"""

class main(object):
	def __init__(self):
		try:
			os.system('clear')
			print (banner)
			try:
				nem=input("[+] Nama Anda : ")
				tgl=input("[+] Tanggal Lahir (ex:28 10 2003) : ").replace(' ','-')
			except KeyboardInterrupt:exit()
			print()
			r=requests.get("https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama="+nem+"&tanggal="+tgl)
			js=json.loads(r.text)
			if 'success' in js['status']:
				print (f"          {h_bold}[✓]{p} Status : {h}{js['status']}{p}")
			else:
				print (f"          {h_bold}[✓]{p} Status : {m}{js['status']}{p}")
			print ("*"*40)
			print()
			print ("[✓] Nama Kamu      : "+js['data'] ['nama'])
			print ("[✓] Tanggal Lahir  : "+js['data'] ['lahir'])
			print ("[✓] Umur           : "+js['data'] ['usia'])
			print ("[✓] Ultahmu Kurang : "+js['data'] ['ultah'])
			print ("[✓] Zodiak         : "+js['data'] ['zodiak'])
			print()
			print("*"*40)
		except:pass
while True:
	main()
	he=input("\n\n[?] Mulai Ulang (y/n) : ").lower()
	if he == 'y':
		main()
	elif he == 'n':
		exit("[*] Good Bye Bambank:*")
	else:
		exit("[*] Goblok :v ")
