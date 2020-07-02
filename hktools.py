#!/usr/bin/python

import os
import sys, traceback


if os.getuid() != 0:
	print "Desculpe, esse script requer previlegios de administrador (sudo)"
	sys.exit()
def main():
	try:
		print ('''
\$$
 |$$  |$$  |$$   $$| |$$$$$$$|  |$$$          |$$$      |$$      |$$$$$
 |$$__|$$  |$$ $$|      |$$    |$$  $$      |$$   $$    |$$      |$    
 |$$$$$$$  |$$$$|       |$$  |$$      $$  |$$       $$  |$$      |$$$$$     
 |$$  |$$  |$$ $$|      |$$    |$$  $$      |$$   $$    |$$          |$
 |$$  |$$  |$$   $$|    |$$      |$$$         |$$$      |$$$$$$  |$$$$$

 \033[1;32mHktools - Instalador de ferramentas Kali \033[1;m

 \033[1;32m+ -- -- +=[ Author: Elton C. Nascimento | eltnas@outlook.com \033[1;m
 \033[1;32m+ -- -- +=[ 331 Ferramentas \033[1;m


\033[1;91m[W] Apos atualizar seu sistema e instalar os programas desejados, nao se esqueca de remover os repositorios do Kali .\033[1;m
		''')
		def inicio1():
			while True:
				print ('''
1) Add Repositorios Kali & Atualizar 
2) Categorias
3) Instalar Ferramentas Essenciais Kali
4) Instalar todas as ferramentas kali linux
5) Ajuda

			''')

				opcion0 = raw_input("\033[1;36mhkt > \033[1;m")
			
				while opcion0 == "1":
					print ('''
1) Add Repositorios Kali
2) Atualizar
3) Remover Repositorios Kali
4) Ver o arquivo sources.list

					''')
					repo = raw_input("\033[1;32mDigite a opcao desejada ou 98 para voltar ?> \033[1;m")
					if repo == "1":
						cmd1 = os.system("apt-key adv --keyserver pool.sks-keyservers.net --recv-keys ED444FF07D8D0BF6")
						cmd2 = os.system("echo '# Kali linux repositories |$$ Added by hktools\ndeb http://http.kali.org/kali kali-rolling main contrib non-free' >> /etc/apt/sources.list")
					elif repo == "2":
						cmd3 = os.system("apt update -m")
					elif repo == "3":
						infile = "/etc/apt/sources.list"
						outfile = "/etc/apt/sources.list"

						delete_list = ["# Kali linux repositories |$$ Added by hktools\n", "deb http://http.kali.org/kali kali-rolling main contrib non-free\n"]
						fin = open(infile)
						os.remove("/etc/apt/sources.list")
						fout = open(outfile, "w+")
						for line in fin:
						    for word in delete_list:
						        line = line.replace(word, "")
						    fout.write(line)
						fin.close()
						fout.close()
						print ("\033[1;31m\nTodos os repositorios do kali linux foram deletados !\n\033[1;m")
					elif repo == "98":
						inicio1()
					elif repo == "99":
						inicio1()
					elif repo == "4":
						file = open('/etc/apt/sources.list', 'r')

						print (file.read())

					else:
						print ("\033[1;31mComando invalido!\033[1;m") 					
						

				if opcion0 == "3":
					print (''' 
					\033[1;36m****************** Instalacao de ferramentas essenciais do kali. *******************\033[1;m
 

Nesse menu, instala de forma automatica algumas ferramentas essenciais, como o nmap por exemplo, para um ataque hacker. Estao listadas ferramentas para Coleta de informacao e analise de Vulnerabilidade (Nmap, setoolkit, DNSenum e Cisco-Tourch), para Aplicacoes Web (Parsero, Wapiti3, Owasp Zap, Wireshark), para Violacao de Senhas (John the Ripper e crunch), para Engenharia Reversa (APKTool), para Ataque Wireles (Aircrack-ng, Fern-Wifi-Crack e Bully). Essa e a primeira versao, na proxima irei adicionar mais ferramentas.

Aconselho a antes de usar, tentar entender a ferramenta antes. Isso pode ser feito com o comando man antes do ferramenta (ex.: man nmap), isso ira mostrar um pequeno manual da mesma com os comandos mais usados e ate um exemplo de uso.


''')


					repo = raw_input("\033[1;32mDeseja instalar essas ferramentas ? [s/n]> \033[1;m")
					if repo == "s":
						cmd = os.system("apt install git python3-pyqt5 nmap set dnsenum cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch parsero zaproxy wireshark crunch john apktool android-sdk aircrack-ng fern-wifi-cracker bully dumpzilla volatility -y && wget https://ufpr.dl.sourceforge.net/project/wapiti/wapiti/wapiti-3.0.3/wapiti3-3.0.3.tar.gz && -tar xzvf wapiti3-3.0.3.tar.gz")

				elif opcion0 == "4"	:
					repo = raw_input("\033[1;32mVoce desej instalar todas as ferramentas do Kali Linux ? [s/n]> \033[1;m")
					if repo == "s":
						cmd1 = os.system("apt -f install acccheck ace-voip amap automater braa casefile cdpsnarf cisco-torch cookie-cadger copy-router-config dmitry dnmap dnsenum dnsmap dnsrecon dnstracer dnswalk dotdotpwn enum4linux enumiax exploitdb fierce firewalk fragroute fragrouter ghost-phisher golismero goofile lbd maltego-teeth masscan metagoofil miranda nmap p0f parsero recon-ng set smtp-user-enum snmpcheck sslcaudit sslsplit sslstrip sslyze thc-ipv6 theharvester tlssled twofi urlcrazy wireshark wol-e xplico ismtp intrace hping3 bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap wifite apache-users arachni bbqsql blindelephant burpsuite cutycapt davtest deblaze dirb dirbuster fimap funkload grabber jboss-autopwn joomscan jsql maltego-teeth padbuster paros parsero plecost powerfuzzer proxystrike recon-ng skipfish sqlmap sqlninja sqlsus ua-tester uniscan vega w3af webscarab websploit wfuzz wpscan xsser zaproxy burpsuite dnschef fiked hamster-sidejack hexinject iaxflood inviteflood ismtp mitmproxy ohrwurm protos-sip rebind responder rtpbreak rtpinsertsound rtpmixsound sctpscan siparmyknife sipp sipvicious sniffjoke sslsplit sslstrip thc-ipv6 voiphopper webscarab wifi-honey wireshark xspy yersinia zaproxy cryptcat cymothoa dbd dns2tcp http-tunnel httptunnel intersect nishang polenum powersploit pwnat ridenum sbd u3-pwn webshells weevely casefile cutycapt dos2unix dradis keepnote magictree metagoofil nipper-ng pipal armitage backdoor-factory cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn linux-exploit-suggester maltego-teeth set shellnoob sqlmap thc-ipv6 yersinia beef-xss binwalk bulk-extractor chntpw cuckoo dc3dd ddrescue dumpzilla extundelete foremost galleta guymager iphone-backup-analyzer p0f pdf-parser pdfid pdgmail peepdf volatility xplico dhcpig funkload iaxflood inviteflood ipv6-toolkit mdk3 reaver rtpflood slowhttptest t50 termineter thc-ipv6 thc-ssl-dos acccheck burpsuite cewl chntpw cisco-auditing-tool cmospwd creddump crunch findmyhash gpp-decrypt hash-identifier hexorbase john johnny keimpx maltego-teeth maskprocessor multiforcer ncrack oclgausscrack pack patator polenum rainbowcrack rcracki-mt rsmangler statsprocessor thc-pptp-bruter truecrack webscarab wordlists zaproxy apktool dex2jar python-distorm3 edb-debugger jad javasnoop jd ollydbg smali valgrind yara android-sdk apktool arduino dex2jar sakis3g smali && wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")

				elif opcion0 == "5":
					print (''' 
****************** Comandos ******************


\033[1;32m98\033[1;m 	\033[1;33mVolta para a opcao anterior\033[1;m

\033[1;32m99\033[1;m	\033[1;33mVolta pro menu principal\033[1;m

		''')


				def inicio():
					while opcion0 == "2":
						print ('''
\033[1;36m**************************** Todas as categorias *****************************\033[1;m

1) Coleta de Informacoes        |$$   8) Ferramantas de exploracao
2) Analise de Vulnerabilidade   |$$   9) Ferramentas forenses
3) Ataque wirelles              |$$   10) Teste de estresse
4) Aplicacoes web               |$$   11) Ataque de senhas
5) Sniffing & Spoofing          |$$   12) Engenharia reversa
6) Manutencao de acesso         |$$   13) Hardware Hacking
7) Ferramentas de relatorios    |$$   14) Extra
									
0) Todas

			 ''')
						print ("\033[1;32mSelecione uma categoria ou selecione 98 para voltar e 99 para ir ao inicio .\n\033[1;m")

						opcion1 = raw_input("\033[1;36mhkt > \033[1;m")
						if opcion1 == "98":
							inicio1()
						elif opcion1 == "99":
							inicio1()
						elif opcion1 == "0":
							cmd = os.system("apt -f install acccheck ace-voip amap automater braa casefile cdpsnarf cisco-torch cookie-cadger copy-router-config dmitry dnmap dnsenum dnsmap dnsrecon dnstracer dnswalk dotdotpwn enum4linux enumiax exploitdb fierce firewalk fragroute fragrouter ghost-phisher golismero goofile lbd maltego-teeth masscan metagoofil miranda nmap p0f parsero recon-ng set smtp-user-enum snmpcheck sslcaudit sslsplit sslstrip sslyze thc-ipv6 theharvester tlssled twofi urlcrazy wireshark wol-e xplico ismtp intrace hping3 bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap wifite apache-users arachni bbqsql blindelephant burpsuite cutycapt davtest deblaze dirb dirbuster fimap funkload grabber jboss-autopwn joomscan jsql maltego-teeth padbuster paros parsero plecost powerfuzzer proxystrike recon-ng skipfish sqlmap sqlninja sqlsus ua-tester uniscan vega w3af webscarab websploit wfuzz wpscan xsser zaproxy burpsuite dnschef fiked hamster-sidejack hexinject iaxflood inviteflood ismtp mitmproxy ohrwurm protos-sip rebind responder rtpbreak rtpinsertsound rtpmixsound sctpscan siparmyknife sipp sipvicious sniffjoke sslsplit sslstrip thc-ipv6 voiphopper webscarab wifi-honey wireshark xspy yersinia zaproxy cryptcat cymothoa dbd dns2tcp http-tunnel httptunnel intersect nishang polenum powersploit pwnat ridenum sbd u3-pwn webshells weevely casefile cutycapt dos2unix dradis keepnote magictree metagoofil nipper-ng pipal armitage backdoor-factory cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn linux-exploit-suggester maltego-teeth set shellnoob sqlmap thc-ipv6 yersinia beef-xss binwalk bulk-extractor chntpw cuckoo dc3dd ddrescue dumpzilla extundelete foremost galleta guymager iphone-backup-analyzer p0f pdf-parser pdfid pdgmail peepdf volatility xplico dhcpig funkload iaxflood inviteflood ipv6-toolkit mdk3 reaver rtpflood slowhttptest t50 termineter thc-ipv6 thc-ssl-dos acccheck burpsuite cewl chntpw cisco-auditing-tool cmospwd creddump crunch findmyhash gpp-decrypt hash-identifier hexorbase john johnny keimpx maltego-teeth maskprocessor multiforcer ncrack oclgausscrack pack patator polenum rainbowcrack rcracki-mt rsmangler statsprocessor thc-pptp-bruter truecrack webscarab wordlists zaproxy apktool dex2jar python-distorm3 edb-debugger jad javasnoop jd ollydbg smali valgrind yara android-sdk apktool arduino dex2jar sakis3g smali && wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")	
						while opcion1 == "1":
							print ('''
\033[1;36m=+[ Coleta de informacao\033[1;m

 1) acccheck				|$$	30) lbd
 2) ace-voip				|$$	31) Maltego Teeth
 3) Amap				|$$	32) masscan
 4) Automater				|$$	33) Metagoofil
 5) bing-ip2hosts			|$$	34) Miranda
 6) braa				|$$	35) Nmap
 7) CaseFile					36) ntop
 8) CDPSnarf					37) p0f
 9) cisco-torch					38) Parsero
10) Cookie Cadger				39) Recon-ng
11) copy-router-config				40) SET
12) DMitry					41) smtp-user-enum
13) dnmap					42) snmpcheck
14) dnsenum					43) sslcaudit
15) dnsmap					44) SSLsplit
16) DNSRecon					45) sslstrip
17) dnstracer					46) SSLyze
18) dnswalk					47) THC-IPV6
19) DotDotPwn					48) theHarvester
20) enum4linux					49) TLSSLed
21) enumIAX					50) twofi
22) exploitdb					51) URLCrazy
23) Fierce					52) Wireshark
24) Firewalk					53) WOL-E
25) fragroute					54) Xplico
26) fragrouter					55) iSMTP
27) Ghost Phisher				56) InTrace
28) GoLismero					57) hping3
29) goofile

0) Instalar todas as ferramentas?
				 
						''')
							print ("\033[1;32mSelecione uma opcao ou selecione 98 para voltar e 99 para ir ao inicio .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mhkt > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt install acccheck")

							elif opcion2 == "2":
								cmd = os.system("apt install ace-voip")

							elif opcion2 == "3":
								cmd = os.system("apt install amap")
							elif opcion2 == "4":
								cmd = os.system("apt install automater")
							elif opcion2 == "5":
								cmd = os.system("wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")
							elif opcion2 == "6":
								cmd = os.system("apt install braa")
							elif opcion2 == "7":
								cmd = os.system("apt install casefile")
							elif opcion2 == "8":
								cmd = os.system("apt install cdpsnarf")
							elif opcion2 == "9":
								cmd = os.system("apt install cisco-torch")
							elif opcion2 == "10":
								cmd = os.system("apt install cookie-cadger")
							elif opcion2 == "11":
								cmd = os.system("apt install copy-router-config")
							elif opcion2 == "12":
								cmd = os.system("apt install dmitry")
							elif opcion2 == "13":
								cmd = os.system("apt install dnmap")
							elif opcion2 == "14":
								cmd = os.system("apt install dnsenum")
							elif opcion2 == "15":
								cmd = os.system("apt install dnsmap")
							elif opcion2 == "16":
								cmd = os.system("apt install dnsrecon")
							elif opcion2 == "17":
								cmd = os.system("apt install dnstracer")
							elif opcion2 == "18":
								cmd = os.system("apt install dnswalk")
							elif opcion2 == "19":
								cmd = os.system("apt install dotdotpwn")
							elif opcion2 == "20":
								cmd = os.system("apt install enum4linux")
							elif opcion2 == "21":
								cmd = os.system("apt install enumiax")
							elif opcion2 == "22":
								cmd = os.system("apt install exploitdb")
							elif opcion2 == "23":
								cmd = os.system("apt install fierce")
							elif opcion2 == "24":
								cmd = os.system("apt install firewalk")
							elif opcion2 == "25":
								cmd = os.system("apt install fragroute")
							elif opcion2 == "26":
								cmd = os.system("apt install fragrouter")
							elif opcion2 == "27":
								cmd = os.system("apt install ghost-phisher")
							elif opcion2 == "28":
								cmd = os.system("apt install golismero")
							elif opcion2 == "29":
								cmd = os.system("apt install goofile")
							elif opcion2 == "30":
								cmd = os.system("apt install lbd")
							elif opcion2 == "31":
								cmd = os.system("apt install maltego-teeth")
							elif opcion2 == "32":
								cmd = os.system("apt install masscan")
							elif opcion2 == "33":
								cmd = os.system("apt install metagoofil")
							elif opcion2 == "34":
								cmd = os.system("apt install miranda")
							elif opcion2 == "35":
								cmd = os.system("apt install nmap")
							elif opcion2 == "36":
								print ('ntop is unavailable')
							elif opcion2 == "37":
								cmd = os.system("apt install p0f")
							elif opcion2 == "38":
								cmd = os.system("apt install parsero")
							elif opcion2 == "39":
								cmd = os.system("apt install recon-ng")
							elif opcion2 == "40":
								cmd = os.system("apt install set")
							elif opcion2 == "41":
								cmd = os.system("apt install smtp-user-enum")
							elif opcion2 == "42":
								cmd = os.system("apt install snmpcheck")
							elif opcion2 == "43":
								cmd = os.system("apt install sslcaudit")
							elif opcion2 == "44":
								cmd = os.system("apt install sslsplit")
							elif opcion2 == "45":
								cmd = os.system("apt install sslstrip")
							elif opcion2 == "46":
								cmd = os.system("apt install sslyze")
							elif opcion2 == "47":
								cmd = os.system("apt install thc-ipv6")
							elif opcion2 == "48":
								cmd = os.system("apt install theharvester")
							elif opcion2 == "49":
								cmd = os.system("apt install tlssled")
							elif opcion2 == "50":
								cmd = os.system("apt install twofi")
							elif opcion2 == "51":
								cmd = os.system("apt install urlcrazy")
							elif opcion2 == "52":
								cmd = os.system("apt install wireshark")
							elif opcion2 == "53":
								cmd = os.system("apt install wol-e")
							elif opcion2 == "54":
								cmd = os.system("apt install xplico")
							elif opcion2 == "55":
								cmd = os.system("apt install ismtp")
							elif opcion2 == "56":
								cmd = os.system("apt install intrace")
							elif opcion2 == "57":
								cmd = os.system("apt install hping3")
							elif opcion2 == "98":
								inicio()
							elif opcion2 == "99":
								inicio1()		
							elif opcion2 == "0":
								cmd = os.system("apt install -y acccheck ace-voip amap automater braa casefile cdpsnarf cisco-torch cookie-cadger copy-router-config dmitry dnmap dnsenum dnsmap dnsrecon dnstracer dnswalk dotdotpwn enum4linux enumiax exploitdb fierce firewalk fragroute fragrouter ghost-phisher golismero goofile lbd maltego-teeth masscan metagoofil miranda nmap p0f parsero recon-ng set smtp-user-enum snmpcheck sslcaudit sslsplit sslstrip sslyze thc-ipv6 theharvester tlssled twofi urlcrazy wireshark wol-e xplico ismtp intrace hping3 && wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")				
							else:
								print ("\033[1;31mComando invalido!\033[1;m")



						while opcion1 == "2":
							print ('''
\033[1;36m=+[ Analise de Vulnerabilidades\033[1;m

 1) BBQSQL				18) Nmap
 2) BED					19)ohrwurm
 3) cisco-auditing-tool			20) openvas-administrator
 4) cisco-global-exploiter		21) openvas-cli
 5) cisco-ocs				22) openvas-manager
 6) cisco-torch				23) openvas-scanner
 7) copy-router-config			24) Oscanner
 8) commix				25) Powerfuzzer
 9) DBPwAudit				26) sfuzz
10) DoonaDot				27) SidGuesser
11) DotPwn				28) SIPArmyKnife
12) Greenbone Security Assistant 	29) sqlmap
13) GSD					30) Sqlninja
14) HexorBase				31) sqlsus
15) Inguma				32) THC-IPV6
16) jSQL				33) tnscmd10g
17) Lynis				34) unix-privesc-check
					35) Yersinia

0) Instalar todas as ferramentas?
				 
						''')
							print ("\033[1;32mSelecione uma opcao ou selecione 98 para voltar e 99 para ir ao inicio .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mhkt > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt install bbqsql")

							elif opcion2 == "2":
								cmd = os.system("apt install bed")

							elif opcion2 == "3":
								cmd = os.system("apt install cisco-auditing-tool")
							elif opcion2 == "4":
								cmd = os.system("apt install cisco-global-exploiter")
							elif opcion2 == "5":
								cmd = os.system("apt install cisco-ocs")
							elif opcion2 == "6":
								cmd = os.system("apt install cisco-torch")
							elif opcion2 == "7":
								cmd = os.system("apt install copy-router-config")
							elif opcion2 == "8":
								cmd = os.system("apt install git && git clone https://github.com/stasinopoulos/commix.git commix && cd commix && python ./commix.py --install")
							elif opcion2 == "9":
								cmd = os.system("echo 'download page : http://www.cqure.net/wp/tools/database/dbpwaudit/'")
							elif opcion2 == "10":
								cmd = os.system("apt install doona")
							elif opcion2 == "11":
								cmd = os.system("apt install dotdotpwn")
							elif opcion2 == "12":
								cmd = os.system("apt install greenbone-security-assistant")
							elif opcion2 == "13":
								cmd = os.system("apt install git && git clone git://git.kali.org/packages/gsd.git")
							elif opcion2 == "14":
								cmd = os.system("apt install hexorbase")
							elif opcion2 == "15":
								print ("Please download inguma from : http://inguma.sourceforge.net")
							elif opcion2 == "16":
								cmd = os.system("apt install jsql")
							elif opcion2 == "17":
								cmd = os.system("apt install lynis")
							elif opcion2 == "18":
								cmd = os.system("apt install nmap")
							elif opcion2 == "19":
								cmd = os.system("apt install ohrwurm")
							elif opcion2 == "20":
								cmd = os.system("apt install openvas-administrator")
							elif opcion2 == "21":
								cmd = os.system("apt install openvas-cli")
							elif opcion2 == "22":
								cmd = os.system("apt install openvas-manager")
							elif opcion2 == "23":
								cmd = os.system("apt install openvas-scanner")
							elif opcion2 == "24":
								cmd = os.system("apt install oscanner")
							elif opcion2 == "25":
								cmd = os.system("apt install powerfuzzer")
							elif opcion2 == "26":
								cmd = os.system("apt install sfuzz")
							elif opcion2 == "27":
								cmd = os.system("apt install sidguesser")
							elif opcion2 == "28":
								cmd = os.system("apt install siparmyknife")
							elif opcion2 == "29":
								cmd = os.system("apt install sqlmap")
							elif opcion2 == "30":
								cmd = os.system("apt install sqlninja")
							elif opcion2 == "31":
								cmd = os.system("apt install sqlsus")
							elif opcion2 == "32":
								cmd = os.system("apt install thc-ipv6")
							elif opcion2 == "33":
								cmd = os.system("apt install tnscmd10g")
							elif opcion2 == "34":
								cmd = os.system("apt install unix-privesc-check")
							elif opcion2 == "35":
								cmd = os.system("apt install yersinia")
							elif opcion2 == "98":
								inicio()
							elif opcion2 == "99":
								inicio1()						
							elif opcion2 == "0":
								cmd = os.system("apt install -y bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia")						
							else:
								print ("\033[1;31mComando invalido!\033[1;m")

						while opcion1 == "3":
							print ('''
		\033[1;36m=+[ Wifi\033[1;m

 1) Aircrack-ng				17) kalibrate-rtl
 2) Asleap				18) KillerBee
 3) Bluelog				19) Kismet
 4) BlueMaho				20) mdk3
 5) Bluepot				21) mfcuk
 6) BlueRanger				22) mfoc
 7) Bluesnarfer				23) mfterm
 8) Bully				24) Multimon-NG
 9) coWPAtty				25) PixieWPS
10) crackle				26) Reaver
11) eapmd5pass				27) redfang
12) Fern Wifi Cracker			28) RTLSDR Scanner
13) Ghost Phisher			29) Spooftooph
14) GISKismet				30) Wifi Honey				31) Wifitap
16) gr-scan				32) Wifite 

0) Instalar todas as ferramentas?
				 
						''')
							print ("\033[1;32mSelecione uma opcao ou selecione 98 para voltar e 99 para ir ao inicio .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mhkt > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt install aircrack-ng")

							elif opcion2 == "2":
								cmd = os.system("apt install asleap")

							elif opcion2 == "3":
								cmd = os.system("apt install bluelog")
							elif opcion2 == "4":
								cmd = os.system("apt install git && git clone git://git.kali.org/packages/bluemaho.git")
							elif opcion2 == "5":
								cmd = os.system("apt install git && git clone git://git.kali.org/packages/bluepot.git")
							elif opcion2 == "6":
								cmd = os.system("apt install blueranger")
							elif opcion2 == "7":
								cmd = os.system("apt install bluesnarfer")
							elif opcion2 == "8":
								cmd = os.system("apt install bully")
							elif opcion2 == "9":
								cmd = os.system("apt install cowpatty")
							elif opcion2 == "10":
								cmd = os.system("apt install crackle")
							elif opcion2 == "11":
								cmd = os.system("apt install eapmd5pass")
							elif opcion2 == "12":
								cmd = os.system("apt install fern-wifi-cracker")
							elif opcion2 == "13":
								cmd = os.system("apt install ghost-phisher")
							elif opcion2 == "14":
								cmd = os.system("apt install giskismet")
							elif opcion2 == "16":
								cmd = os.system("apt install git && git clone git://git.kali.org/packages/gr-scan.git")
							elif opcion2 == "17":
								cmd = os.system("apt install kalibrate-rtl")
							elif opcion2 == "18":
								cmd = os.system("apt install killerbee")
							elif opcion2 == "19":
								cmd = os.system("apt install kismet")
							elif opcion2 == "20":
								cmd = os.system("apt install mdk3")
							elif opcion2 == "21":
								cmd = os.system("apt install mfcuk")
							elif opcion2 == "22":
								cmd = os.system("apt install mfoc")
							elif opcion2 == "23":
								cmd = os.system("apt install mfterm")
							elif opcion2 == "24":
								cmd = os.system("apt install multimon-ng")
							elif opcion2 == "25":
								cmd = os.system("apt install pixiewps")
							elif opcion2 == "26":
								cmd = os.system("apt install reaver")
							elif opcion2 == "27":
								cmd = os.system("apt install redfang")
							elif opcion2 == "28":
								cmd = os.system("apt install rtlsdr-scanner")
							elif opcion2 == "29":
								cmd = os.system("apt install spooftooph")
							elif opcion2 == "30":
								cmd = os.system("apt install wifi-honey")
							elif opcion2 == "31":
								cmd = os.system("apt install wifitap")
							elif opcion2 == "32":
								cmd = os.system("apt install wifite")
							elif opcion2 == "0":
								cmd = os.system("apt install -y aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap wifite")
							elif opcion2 == "98":
								inicio()
							elif opcion2 == "99":
								inicio1()						
							else:
								print ("\033[1;31mComando invalido!\033[1;m")
						while opcion1 == "4":
							print ('''
\033[1;36m=+[ Aplicacoes web\033[1;m

 1) apache-users			21) Parsero
 2) Arachni				22) plecost
 3) BBQSQL				23) Powerfuzzer
 4) BlindElephant			24) ProxyStrike
 5) Burp Suite				25) Recon-ng
 6) commix				26) Skipfish
 7) CutyCapt				27) sqlmap
 8) DAVTest				28) Sqlninja
 9) deblaze				29) sqlsus
10) DIRB				30) ua-tester
11) DirBuster				31) Uniscan
12) fimap				32) Vega
13) FunkLoad				33) w3af
14) Grabber				34) WebScarab
15) jboss-autopwn			35) Webshag
16) joomscan				36) WebSlayer
17) jSQL				37) WebSploit
18) Maltego Teeth			38) Wfuzz
19) PadBuster				39) WPScan
20) Paros				40) XSSer
					41) zaproxy

0) Instalar todas as ferramentas?
				 
						''')
							print ("\033[1;32mSelecione uma opcao ou selecione 98 para voltar e 99 para ir ao inicio .\n\033[1;m")

							
							opcion2 = raw_input("\033[1;36mhkt > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt install apache-users")

							elif opcion2 == "2":
								cmd = os.system("apt install arachni")

							elif opcion2 == "3":
								cmd = os.system("apt install bbqsql")
							elif opcion2 == "4":
								cmd = os.system("apt install blindelephant")
							elif opcion2 == "5":
								cmd = os.system("apt install burpsuite")
							elif opcion2 == "6":
								cmd = os.system("apt install cutycapt")
							elif opcion2 == "7":
								cmd = os.system("apt install git && git clone https://github.com/stasinopoulos/commix.git commix && cd commix && python ./commix.py --install")
							elif opcion2 == "8":
								cmd = os.system("apt install davtest")
							elif opcion2 == "9":
								cmd = os.system("apt install deblaze")
							elif opcion2 == "10":
								cmd = os.system("apt install dirb")
							elif opcion2 == "11":
								cmd = os.system("apt install dirbuster")
							elif opcion2 == "12":
								cmd = os.system("apt install fimap")
							elif opcion2 == "13":
								cmd = os.system("apt install funkload")
							elif opcion2 == "14":
								cmd = os.system("apt install grabber")
							elif opcion2 == "15":
								cmd = os.system("apt install jboss-autopwn")
							elif opcion2 == "16":
								cmd = os.system("apt install joomscan")
							elif opcion2 == "17":
								cmd = os.system("apt install jsql")
							elif opcion2 == "18":
								cmd = os.system("apt install maltego-teeth")
							elif opcion2 == "19":
								cmd = os.system("apt install padbuster")
							elif opcion2 == "20":
								cmd = os.system("apt install paros")
							elif opcion2 == "21":
								cmd = os.system("apt install parsero")
							elif opcion2 == "22":
								cmd = os.system("apt install plecost")
							elif opcion2 == "23":
								cmd = os.system("apt install powerfuzzer")
							elif opcion2 == "24":
								cmd = os.system("apt install proxystrike")
							elif opcion2 == "25":
								cmd = os.system("apt install recon-ng")
							elif opcion2 == "26":
								cmd = os.system("apt install skipfish")
							elif opcion2 == "27":
								cmd = os.system("apt install sqlmap")
							elif opcion2 == "28":
								cmd = os.system("apt install sqlninja")
							elif opcion2 == "29":
								cmd = os.system("apt install sqlsus")
							elif opcion2 == "30":
								cmd = os.system("apt install ua-tester")
							elif opcion2 == "31":
								cmd = os.system("apt install uniscan")
							elif opcion2 == "32":
								cmd = os.system("apt install vega")
							elif opcion2 == "33":
								cmd = os.system("apt install w3af")
							elif opcion2 == "34":
								cmd = os.system("apt install webscarab")
							elif opcion2 == "35":
								print ("Webshag is unavailable")
							elif opcion2 == "36":
								cmd = os.system("apt install git && git clone git://git.kali.org/packages/webslayer.git")
							elif opcion2 == "37":
								cmd = os.system("apt install websploit")
							elif opcion2 == "38":
								cmd = os.system("apt install wfuzz")
							elif opcion2 == "39":
								cmd = os.system("apt install wpscan")
							elif opcion2 == "40":
								cmd = os.system("apt install xsser")
							elif opcion2 == "41":
								cmd = os.system("apt install zaproxy")										
							elif opcion2 == "98":
								inicio()
							elif opcion2 == "99":
								inicio1()	
							elif opcion2 == "0":
								cmd = os.system("apt install -y apache-users arachni bbqsql blindelephant burpsuite cutycapt davtest deblaze dirb dirbuster fimap funkload grabber jboss-autopwn joomscan jsql maltego-teeth padbuster paros parsero plecost powerfuzzer proxystrike recon-ng skipfish sqlmap sqlninja sqlsus ua-tester uniscan vega w3af webscarab websploit wfuzz wpscan xsser zaproxy")												
							else:
								print ("\033[1;31mComando invalido!\033[1;m")
						while opcion1 == "5":
							print ('''
\033[1;36m=+[ Sniffing & Spoofing\033[1;m

 1) Burp Suite				17) rtpmixsound
 2) DNSChef				18) sctpscan
 3) fiked				19) SIPArmyKnife
 4) hamster-sidejack			20) SIPp
 5) HexInject				21) SIPVicious
 6) iaxflood				22) SniffJoke
 7) inviteflood				23) SSLsplit
 8) iSMTP				24) sslstrip
 9) isr-evilgrade			25) THC-IPV6
10) mitmproxy				26) VoIPHopper
11) ohrwurm				27) WebScarab
12) protos-sip				28) Wifi Honey
13) rebind				29) Wireshark
14) responder				30) xspy
15) rtpbreak				31) Yersinia
16) rtpinsertsound			32) zaproxy 

0) Instalar todas as ferramentas?
				 
						''')
							print ("\033[1;32mSelecione uma opcao ou selecione 98 para voltar e 99 para ir ao inicio .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mhkt > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt install burpsuite")

							elif opcion2 == "2":
								cmd = os.system("apt install dnschef")

							elif opcion2 == "3":
								cmd = os.system("apt install fiked")
							elif opcion2 == "4":
								cmd = os.system("apt install hamster-sidejack")
							elif opcion2 == "5":
								cmd = os.system("apt install hexinject")
							elif opcion2 == "6":
								cmd = os.system("apt install iaxflood")
							elif opcion2 == "7":
								cmd = os.system("apt install inviteflood")
							elif opcion2 == "8":
								cmd = os.system("apt install ismtp")
							elif opcion2 == "9":
								cmd = os.system("apt install git && git clone git://git.kali.org/packages/isr-evilgrade.git")
							elif opcion2 == "10":
								cmd = os.system("apt install mitmproxy")
							elif opcion2 == "11":
								cmd = os.system("apt install ohrwurm")
							elif opcion2 == "12":
								cmd = os.system("apt install protos-sip")
							elif opcion2 == "13":
								cmd = os.system("apt install rebind")
							elif opcion2 == "14":
								cmd = os.system("apt install responder")
							elif opcion2 == "15":
								cmd = os.system("apt install rtpbreak")
							elif opcion2 == "16":
								cmd = os.system("apt install rtpinsertsound")
							elif opcion2 == "17":
								cmd = os.system("apt install rtpmixsound")
							elif opcion2 == "18":
								cmd = os.system("apt install sctpscan")
							elif opcion2 == "19":
								cmd = os.system("apt install siparmyknife")
							elif opcion2 == "20":
								cmd = os.system("apt install sipp")
							elif opcion2 == "21":
								cmd = os.system("apt install sipvicious")
							elif opcion2 == "22":
								cmd = os.system("apt install sniffjoke")
							elif opcion2 == "23":
								cmd = os.system("apt install sslsplit")
							elif opcion2 == "24":
								cmd = os.system("apt install sslstrip")
							elif opcion2 == "25":
								cmd = os.system("apt install thc-ipv6")
							elif opcion2 == "26":
								cmd = os.system("apt install voiphopper")
							elif opcion2 == "27":
								cmd = os.system("apt install webscarab")
							elif opcion2 == "28":
								cmd = os.system("apt install wifi-honey")
							elif opcion2 == "29":
								cmd = os.system("apt install wireshark")
							elif opcion2 == "30":
								cmd = os.system("apt install xspy")
							elif opcion2 == "31":
								cmd = os.system("apt install yersinia")
							elif opcion2 == "32":
								cmd = os.system("apt install zaproxy")
							elif opcion2 == "98":
								inicio()
							elif opcion2 == "99":
								inicio1()


							elif opcion2 == "0":
								cmd = os.system("apt install -y burpsuite dnschef fiked hamster-sidejack hexinject iaxflood inviteflood ismtp mitmproxy ohrwurm protos-sip rebind responder rtpbreak rtpinsertsound rtpmixsound sctpscan siparmyknife sipp sipvicious sniffjoke sslsplit sslstrip thc-ipv6 voiphopper webscarab wifi-honey wireshark xspy yersinia zaproxy")  
							else:
								print ("\033[1;31mComando invalido!\033[1;m")

						while opcion1 == "6":
							print ('''
\033[1;36m=+[ Manutencao de acesso\033[1;m

 1) CryptCat			9) polenum
 2) Cymothoa			10) PowerSploit
 3) dbd					11) pwnat
 4) dns2tcp				12) RidEnum
 5) http-tunnel			13) sbd
 6) HTTPTunnel			14) U3-Pwn
 7) Intersect			15) Webshells
 8) Nishang				16) Weevely


0) Instalar todas as ferramentas?
				 
						''')
							print ("\033[1;32mSelecione uma opcao ou selecione 98 para voltar e 99 para ir ao inicio .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mhkt > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt install cryptcat")

							elif opcion2 == "2":
								cmd = os.system("apt install cymothoa")

							elif opcion2 == "3":
								cmd = os.system("apt install dbd")
							elif opcion2 == "4":
								cmd = os.system("apt install dns2tcp")
							elif opcion2 == "5":
								cmd = os.system("apt install http-tunnel")
							elif opcion2 == "6":
								cmd = os.system("apt install httptunnel")
							elif opcion2 == "7":
								cmd = os.system("apt install intersect")
							elif opcion2 == "8":
								cmd = os.system("apt install nishang")
							elif opcion2 == "9":
								cmd = os.system("apt install polenum")
							elif opcion2 == "10":
								cmd = os.system("apt install powersploit")
							elif opcion2 == "11":
								cmd = os.system("apt install pwnat")
							elif opcion2 == "12":
								cmd = os.system("apt install ridenum")
							elif opcion2 == "13":
								cmd = os.system("apt install sbd")
							elif opcion2 == "14":
								cmd = os.system("apt install u3-pwn")
							elif opcion2 == "15":
								cmd = os.system("apt install webshells")
							elif opcion2 == "16":
								cmd = os.system("apt install weevely")
							elif opcion2 == "98":
								inicio()
							elif opcion2 == "99":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt install -y cryptcat cymothoa dbd dns2tcp http-tunnel httptunnel intersect nishang polenum powersploit pwnat ridenum sbd u3-pwn webshells weevely")
							else:
								print ("\033[1;31mComando invalido!\033[1;m")
						while opcion1 == "7":
							print ('''
\033[1;36m=+[ Reporting Tools\033[1;m

1) CaseFile
2) CutyCapt
3) dos2unix
4) Dradis
5) KeepNote	
6) MagicTree
7) Metagoofil
8) Nipper-ng
9) pipal

0) Instalar todas as ferramentas?
				 
						''')
							print ("\033[1;32mSelecione uma opcao ou selecione 98 para voltar e 99 para ir ao inicio .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mhkt > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt install casefile")

							elif opcion2 == "2":
								cmd = os.system("apt install cutycapt")

							elif opcion2 == "3":
								cmd = os.system("apt install dos2unix")
							elif opcion2 == "4":
								cmd = os.system("apt install dradis")
							elif opcion2 == "5":
								cmd = os.system("apt install keepnote")
							elif opcion2 == "6":
								cmd = os.system("apt install magictree")
							elif opcion2 == "7":
								cmd = os.system("apt install metagoofil")
							elif opcion2 == "8":
								cmd = os.system("apt install nipper-ng")
							elif opcion2 == "9":
								cmd = os.system("apt install pipal")
							elif opcion2 == "98":
								inicio()
							elif opcion2 == "99":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt install -y casefile cutycapt dos2unix dradis keepnote magictree metagoofil nipper-ng pipal")  
							else:
								print ("\033[1;31mComando invalido!\033[1;m")

						while opcion1 == "8":
							print ('''
\033[1;36m=+[ Exploitation Tools\033[1;m

 1) Armitage
 2) Backdoor Factory
 3) BeEF
 4) cisco-auditing-tool
 5) cisco-global-exploiter	
 6) cisco-ocs
 7) cisco-torch
 8) commix
 9) crackle
10) jboss-autopwn
11) Linux Exploit Suggester
12) Maltego Teeth
13) SET
14) ShellNoob
15) sqlmap
16) THC-IPV6
17) Yersinia

0) Instalar todas as ferramentas?
				 
						''')
							print ("\033[1;32mSelecione uma opcao ou selecione 98 para voltar e 99 para ir ao inicio .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mhkt > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt install armitage")

							elif opcion2 == "2":
								cmd = os.system("apt install backdoor-factory")

							elif opcion2 == "3":
								cmd = os.system("apt install beef-xss")
							elif opcion2 == "4":
								cmd = os.system("apt install cisco-auditing-tool")
							elif opcion2 == "5":
								cmd = os.system("apt install cisco-global-exploiter")
							elif opcion2 == "6":
								cmd = os.system("apt install cisco-ocs")
							elif opcion2 == "7":
								cmd = os.system("apt install cisco-torch")
							elif opcion2 == "8":
								cmd = os.system("apt install git && git clone https://github.com/stasinopoulos/commix.git commix && cd commix && python ./commix.py --install")
							elif opcion2 == "9":
								cmd = os.system("apt install crackle")
							elif opcion2 == "10":
								cmd = os.system("apt install jboss-autopwn")
							elif opcion2 == "11":
								cmd = os.system("apt install linux-exploit-suggester")
							elif opcion2 == "12":
								cmd = os.system("apt install maltego-teeth")
							elif opcion2 == "13":
								cmd = os.system("apt install set")
							elif opcion2 == "14":
								cmd = os.system("apt install shellnoob")
							elif opcion2 == "15":
								cmd = os.system("apt install sqlmap")
							elif opcion2 == "16":
								cmd = os.system("apt install thc-ipv6")
							elif opcion2 == "17":
								cmd = os.system("apt install yersinia")
							elif opcion2 == "98":
								inicio()
							elif opcion2 == "99":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt install -y armitage backdoor-factory cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn linux-exploit-suggester maltego-teeth set shellnoob sqlmap thc-ipv6 yersinia beef-xss")  						
							else:
								print ("\033[1;31mComando invalido!\033[1;m")

						while opcion1 == "9":
							print ('''
\033[1;36m=+[ Forensics Tools\033[1;m

 1) Binwalk				11) extundelete
 2) bulk-extractor			12) Foremost
 3) Capstone				13) Galleta
 4) chntpw				14) Guymager
 5) Cuckoo				15) iPhone Backup Analyzer
 6) dc3dd				16) p0f
 7) ddrescue				17) pdf-parser
 8) DFF					18) pdfid
 9) diStorm3				19) pdgmail
10) Dumpzilla				20) peepdf
					21) RegRipper
					22) Volatility
					23) Xplico

0) Instalar todas as ferramentas?
				 
						''')
							print ("\033[1;32mSelecione uma opcao ou selecione 98 para voltar e 99 para ir ao inicio .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mhkt > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt install binwalk")

							elif opcion2 == "2":
								cmd = os.system("apt install bulk-extractor")

							elif opcion2 == "3":
								cmd = os.system("apt install git && git clone git://git.kali.org/packages/capstone.git")
							elif opcion2 == "4":
								cmd = os.system("apt install chntpw")
							elif opcion2 == "5":
								cmd = os.system("apt install cuckoo")
							elif opcion2 == "6":
								cmd = os.system("apt install dc3dd")
							elif opcion2 == "7":
								cmd = os.system("apt install ddrescue")
							elif opcion2 == "8":
								print ('dff is unavailable')
							elif opcion2 == "9":
								cmd = os.system("apt install git && git clone git://git.kali.org/packages/distorm3.git")
							elif opcion2 == "10":
								cmd = os.system("apt install dumpzilla")
							elif opcion2 == "11":
								cmd = os.system("apt install extundelete")
							elif opcion2 == "12":
								cmd = os.system("apt install foremost")
							elif opcion2 == "13":
								cmd = os.system("apt install galleta")
							elif opcion2 == "14":
								cmd = os.system("apt install guymager")
							elif opcion2 == "15":
								cmd = os.system("apt install iphone-backup-analyzer")
							elif opcion2 == "16":
								cmd = os.system("apt install p0f")
							elif opcion2 == "17":
								cmd = os.system("apt install pdf-parser")
							elif opcion2 == "18":
								cmd = os.system("apt install pdfid")
							elif opcion2 == "19":
								cmd = os.system("apt install pdgmail")
							elif opcion2 == "20":
								cmd = os.system("apt install peepdf")
							elif opcion2 == "21":
								print ("Regripper is unavailable")
							elif opcion2 == "22":
								cmd = os.system("apt install volatility")
							elif opcion2 == "23":
								cmd = os.system("apt install xplico")
							elif opcion2 == "98":
								inicio()
							elif opcion2 == "99":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt install -y binwalk bulk-extractor chntpw cuckoo dc3dd ddrescue dumpzilla extundelete foremost galleta guymager iphone-backup-analyzer p0f pdf-parser pdfid pdgmail peepdf volatility xplico")						
							else:
								print ("\033[1;31mComando invalido!\033[1;m")
						while opcion1 == "10":
							print ('''
\033[1;36m=+[ Stress Testing\033[1;m

 1) DHCPig
 2) FunkLoad
 3) iaxflood
 4) Inundator
 5) inviteflood	
 6) ipv6-toolkit
 7) mdk3
 8) Reaver
 9) rtpflood
10) SlowHTTPTest
11) t50
12) Termineter
13) THC-IPV6
14) THC-SSL-DOS 		

0) Instalar todas as ferramentas?
				 
						''')
							print ("\033[1;32mSelecione uma opcao ou selecione 98 para voltar e 99 para ir ao inicio .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mhkt > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt install dhcpig")

							elif opcion2 == "2":
								cmd = os.system("apt install funkload")

							elif opcion2 == "3":
								cmd = os.system("apt install iaxflood")
							elif opcion2 == "4":
								cmd = os.system("apt install git && git clone git://git.kali.org/packages/inundator.git")
							elif opcion2 == "5":
								cmd = os.system("apt install inviteflood")
							elif opcion2 == "6":
								cmd = os.system("apt install ipv6-toolkit")
							elif opcion2 == "7":
								cmd = os.system("apt install mdk3")
							elif opcion2 == "8":
								cmd = os.system("apt install reaver")
							elif opcion2 == "9":
								cmd = os.system("apt install rtpflood")
							elif opcion2 == "10":
								cmd = os.system("apt install slowhttptest")
							elif opcion2 == "11":
								cmd = os.system("apt install t50")
							elif opcion2 == "12":
								cmd = os.system("apt install termineter")
							elif opcion2 == "13":
								cmd = os.system("apt install thc-ipv6")
							elif opcion2 == "14":
								cmd = os.system("apt install thc-ssl-dos ")    				             										
							elif opcion2 == "98":
								inicio()
							elif opcion2 == "99":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt install -y dhcpig funkload iaxflood inviteflood ipv6-toolkit mdk3 reaver rtpflood slowhttptest t50 termineter thc-ipv6 thc-ssl-dos")
							else:
								print ("\033[1;31mComando invalido!\033[1;m")
						while opcion1 == "11":
							print ('''
\033[1;36m=+[ Password Attacks\033[1;m

 1) acccheck				19) Maskprocessor
 2) Burp Suite				20) multiforcer
 3) CeWL				21) Ncrack
 4) chntpw				22) oclgausscrack
 5) cisco-auditing-tool			23) PACK
 6) CmosPwd				24) patator
 7) creddump				25) phrasendrescher
 8) crunch				26) polenum
 9) DBPwAudit				27) RainbowCrack
10) findmyhash				28) rcracki-mt
11) gpp-decrypt				29) RSMangler
12) hash-identifier			30) SQLdict
13) HexorBase				31) Statsprocessor
14) THC-Hydra				32) THC-pptp-bruter
15) John the Ripper			33) TrueCrack
16) Johnny				34) WebScarab 
17) keimpx				35) wordlists 
18) Maltego Teeth			36) zaproxy 

0) Instalar todas as ferramentas?
				 
						''')
							print ("\033[1;32mSelecione uma opcao ou selecione 98 para voltar e 99 para ir ao inicio .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mhkt > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt install acccheck")

							elif opcion2 == "2":
								cmd = os.system("apt install burpsuite")

							elif opcion2 == "3":
								cmd = os.system("apt install cewl")
							elif opcion2 == "4":
								cmd = os.system("apt install chntpw")
							elif opcion2 == "5":
								cmd = os.system("apt install cisco-auditing-tool")
							elif opcion2 == "6":
								cmd = os.system("apt install cmospwd")
							elif opcion2 == "7":
								cmd = os.system("apt install creddump")
							elif opcion2 == "8":
								cmd = os.system("apt install crunch")
							elif opcion2 == "9":
								cmd = os.system("apt install git && git clone git://git.kali.org/packages/dbpwaudit.git")
							elif opcion2 == "10":
								cmd = os.system("apt install findmyhash")
							elif opcion2 == "11":
								cmd = os.system("apt install gpp-decrypt")
							elif opcion2 == "12":
								cmd = os.system("apt install hash-identifier")
							elif opcion2 == "13":
								cmd = os.system("apt install hexorbase")
							elif opcion2 == "14":
								cmd = os.system("echo 'please visit : https://www.thc.org/thc-hydra/' ")
							elif opcion2 == "15":
								cmd = os.system("apt install john")
							elif opcion2 == "16":
								cmd = os.system("apt install johnny")
							elif opcion2 == "17":
								cmd = os.system("apt install keimpx")
							elif opcion2 == "18":
								cmd = os.system("apt install maltego-teeth")
							elif opcion2 == "19":
								cmd = os.system("apt install maskprocessor")
							elif opcion2 == "20":
								cmd = os.system("apt install multiforcer")
							elif opcion2 == "21":
								cmd = os.system("apt install ncrack")
							elif opcion2 == "22":
								cmd = os.system("apt install oclgausscrack")
							elif opcion2 == "23":
								cmd = os.system("apt install pack")
							elif opcion2 == "24":
								cmd = os.system("apt install patator")
							elif opcion2 == "25":
								cmd = os.system("echo 'please visit : http://www.leidecker.info/projects/phrasendrescher/index.shtml' ")
							elif opcion2 == "26":
								cmd = os.system("apt install polenum")
							elif opcion2 == "27":
								cmd = os.system("apt install rainbowcrack")
							elif opcion2 == "28":
								cmd = os.system("apt install rcracki-mt")
							elif opcion2 == "29":
								cmd = os.system("apt install rsmangler")
							elif opcion2 == "30":
								print ("Sqldict is unavailable")
							elif opcion2 == "31":
								cmd = os.system("apt install statsprocessor")
							elif opcion2 == "32":
								cmd = os.system("apt install thc-pptp-bruter")
							elif opcion2 == "33":
								cmd = os.system("apt install truecrack")
							elif opcion2 == "34":
								cmd = os.system("apt install webscarab")
							elif opcion2 == "35":
								cmd = os.system("apt install wordlists")
							elif opcion2 == "36":
								cmd = os.system("apt install zaproxy")
							elif opcion2 == "98":
								inicio()
							elif opcion2 == "99":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt install -y acccheck burpsuite cewl chntpw cisco-auditing-tool cmospwd creddump crunch findmyhash gpp-decrypt hash-identifier hexorbase john johnny keimpx maltego-teeth maskprocessor multiforcer ncrack oclgausscrack pack patator polenum rainbowcrack rcracki-mt rsmangler statsprocessor thc-pptp-bruter truecrack webscarab wordlists zaproxy")
							else:
								print ("\033[1;31mComando invalido!\033[1;m")
						while opcion1 == "12" :
							print ('''
\033[1;36m=+[ Reverse Engineering\033[1;m

 1) apktool
 2) dex2jar
 3) diStorm3
 4) edb-debugger
 5) jad	
 6) javasnoop
 7) JD-GUI
 8) OllyDbg
 9) smali
10) Valgrind
11) YARA

0) Instalar todas as ferramentas?
				 
						''')
							print ("\033[1;32mSelecione uma opcao ou selecione 98 para voltar e 99 para ir ao inicio .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mhkt > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt install apktool")

							elif opcion2 == "2":
								cmd = os.system("apt install dex2jar")

							elif opcion2 == "3":
								cmd = os.system("apt install python-diStorm3")
							elif opcion2 == "4":
								cmd = os.system("apt install edb-debugger")
							elif opcion2 == "5":
								cmd = os.system("apt install jad")
							elif opcion2 == "6":
								cmd = os.system("apt install javasnoop")
							elif opcion2 == "7":
								cmd = os.system("apt install JD")
							elif opcion2 == "8":
								cmd = os.system("apt install OllyDbg")
							elif opcion2 == "9":
								cmd = os.system("apt install smali")
							elif opcion2 == "10":
								cmd = os.system("apt install Valgrind")
							elif opcion2 == "11":
								cmd = os.system("apt install YARA")
							elif opcion2 == "98":
								inicio()
							elif opcion2 == "99":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt install -y apktool dex2jar python-diStorm3 edb-debugger jad javasnoop JD OllyDbg smali Valgrind YARA")
							else:
								print ("\033[1;31mComando invalido!\033[1;m")
						while opcion1 == "13" :
							print ('''
\033[1;36m=+[ Hardware Hacking\033[1;m

 1) android-sdk
 2) apktool
 3) Arduino
 4) dex2jar
 5) Sakis3G	
 6) smali

0) Instalar todas as ferramentas?
				 
						''')
							print ("\033[1;32mSelecione uma opcao ou selecione 98 para voltar e 99 para ir ao inicio .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mhkt > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt install android-sdk")

							elif opcion2 == "2":
								cmd = os.system("apt install apktool")

							elif opcion2 == "3":
								cmd = os.system("apt install arduino")
							elif opcion2 == "4":
								cmd = os.system("apt install dex2jar")
							elif opcion2 == "5":
								cmd = os.system("apt install sakis3g")
							elif opcion2 == "6":
								cmd = os.system("apt install smali")

							elif opcion2 == "98":
								inicio()
							elif opcion2 == "99":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt install -y android-sdk apktool arduino dex2jar sakis3g smali")
							else:
								print ("\033[1;31mComando invalido!\033[1;m")
						while opcion1 == "14" :
							print ('''
\033[1;36m=+[ Extra\033[1;m

1) Wifresti		4) Nikto2
2) Squid3
3) Wifite
				''')
							print ("\033[1;32mSelecione uma opcao ou selecione 98 para voltar e 99 para ir ao inicio .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mhkt > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("git clone https://github.com/LionSec/wifresti.git && cp wifresti/wifresti.py /usr/bin/wifresti && chmod +x /usr/bin/wifresti && wifresti")
								print (" ")
							elif opcion2 == "2":
								cmd = os.system("apt install squid3")
								print (" ")
							elif opcion2 == "3"
							 	cmd = os.system("wget https://ufpr.dl.sourceforge.net/project/wapiti/wapiti/wapiti-3.0.3/wapiti3-3.0.3.tar.gz && -tar xzvf wapiti3-3.0.3.tar.gz")
							 elif opcion2 == "4"
								cmd = os.system("wget https://codeload.github.com/sullo/nikto/zip/master && unzip nikto-master.zip")
							elif opcion2 == "98":
								inicio()
							elif opcion2 == "99":
								inicio1()

				inicio()
		inicio1()
	except KeyboardInterrupt:
		print ("Shutdown requested...Goodbye...")
	except Exception:
		traceback.print_exc(file=sys.stdout)
	sys.exit(0)

if __name__ == "__main__":
    main()
