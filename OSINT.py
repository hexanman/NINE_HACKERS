def osint():
	#
	import socket

	G = '\x1b[1;32m'
	R = '\x1b[31m'

	host=input (G+"put your host  :") or "127.0.0.1"
	ip   = socket.gethostbyname(host)
	hint="hint : nano /etc/resolv.conf # 208.67.222.222|208.67.220.220\n____________________________________________________ "+G


	dig="""
	nano /etc/resolv.conf
	------------------------
	dig +noall +answer {0} A
	dig +noall +answer {0} NS
	dig +noall +answer {0} MX
	dig +noall +answer {0} ANY
	dig +noall +answer @8.8.8.8 {0} ANY
	dig +noall +answer +norecurse {0} A
	dig +noall +answer @8.8.8.8 {0} AXFR
	-----------------
	zone transfer
	--------------
	dig +noall +answer {0} NS
	dig +noall +answer @8.8.8.8 {0} AXFR
	dig +noall +answer -x {1} #YOUR IP

	""".format(host,ip)

	dnsrecon='''
	dnsrecon -d {0}
	dnsrecon -d {0} -n “8.8.8.8 | 8.8.4.4”

	#get all dns and try all one by one 
	-----------------
	zone transfer
	--------------
	dnsrecon -d {0} -t axfr
	___________________________
	dnsrecon -r 127.0.0.1-{1} 
	dnsrecon -r {1}/16

	DNSRecon
	dnsrecon -t brt -d {0} -D /usr/share/dnsrecon/namelist.txt


	'''.format(host,ip)

	####################

	TheHarvester='''
	FindSubDomains
	----------------
	theharvester -d {0} -b google,bing,yahoo,netcraft,virustotal

	Find Emails
	----------------
	theharvester -d {0} -b hunter > result.txt

	Get Hunter API Key
	https://hunter.io/api_keys
	nano /usr/share/theharvester/discovery/huntersearch.py

	Find Users
	----------------
	theharvester -d {0} -b linkedin
	theharvester -d {0} -b twitter

	'''.format(host)


	sites='''
	curl ipinfo.io/{0}
	----------------
	https://findsubdomains.com/subdomains-of/microsoft.com

	rawojo3693@fft-mail.com
	rawojo3693@fft-mail.com
	----------------------------------------
	Get Network Ranges

	http://whois.domaintools.com
	----------------------------
	https://findsubdomains.com/subdomains-of/{0}
	--------------------------

	'''.format(host)


	Google_Dorks  ='''
	site:{0} -www.{0}
	-------
	inurl:"linkedin.com/in/" "{0}"
	-------
	Find Sub-Domains
	****************
	site:{0} -www.{0}
	--------
	Collect Files
	--------
	site:{0} filetype:pdf
	------
	Search For Specific Word
	______________________

	site:{0} "hackers"
	-----
	Search For Specific Files
	__________________________

	site:{0} intitle:"index of"
	-------
	site:{0} inurl:phpinfo
	----
	site:{0} intext:password
	----
	Google Dorks (Collect Files)
	_____________________________
	site:{0} filetype:pdf

	Search For Company Users
	-------------------------
	inurl:"linkedin.com/in/" "{0}"
	'''.format(host)


	Recon_NG ='''


	1-install marketplace
	---------------------

	marketplace install all
	marketplace search who

	2- creat your workspaces
	-----------------------

	workspaces list

	workspaces  install


	3-modules
	--------------
	modules search

	modules loads  .......

	options set SOURCE #you site xxxxxxx


	4- api
	--------

	keys add  #your api name xxxxx ...

	Show keys


	5-db
	----------
	db schema
	db delet hosts 40

	db quary select ip_adress from hosts 

	-------------------
	 web interfaec
	-------------
	#type this and you can use gui

	recon-web

	---------
	workspaces creat   xxxx naser

	workspaces select  xxxx naser

	###############################


	work space location in your pc

	cd /root/.recon-ng/workspaces/# your work space name xxxxx

	ls -alh

	-------------------
	*******************
	sub domains _Modules:
	********************
	-------------------
	recon/domains-hosts/bing_domain_web
	recon/domains-hosts/findsubdomains
	recon/domains-hosts/google_site_web
	recon/domains-hosts/netcraft
	recon/domains-hosts/bing_domain_api

	#########################################

	------------------------
	Recon-NG BRUTE FORCE
	---------------------
	recon/domains-hosts/brute_hosts

	Resolve and Extract Sub-Domains

	_____________________________________
	Recon-NG (Find Antivirus Programs) 
	_____________________________________

	discovery/info_disclosure/cache_snoop

	______________________________________
	------host to ip -----
	_______________________________
	recon/hosts-hosts/resolve


	----------------
	reporting/list


	Recon-NG EXAMPLE
	----------------------

	show modules
	use recon/domains-hosts/findsubdomains
	show info
	set source {0}
	run
	show hosts
	back
	###############

	https://github.com/lanmaster53/recon-ng-marketplace/wiki/API-Keys

	'''.format(host)


	ipinfo='''curl ipinfo.io/{0}'''.format(host)

	##########

	Metagoofil='''
	apt-get install metagoofil
	metagoofil -d {0} -t pdf,doc,xls,ppt -l 100 -n 10 -o metapdf -f result.html'''.format(host)




	options=['1-dig','2-dnsrecon','3-TheHarvester',"4-sites",'5-Google_Dorks','6-Recon_NG',"7-ipinfo","*"]
	for i in options:    print(i)


	while 1:
		opt=input (R+"put your option pls :"+G) ;print(hint)
		if opt == "1":
			print(dig)
		elif opt=="2":
			print(dnsrecon)
		elif opt=="3":
			print(TheHarvester)
		elif opt=="4":
			print(sites)
		elif opt=="5":
			print(Google_Dorks)
		elif opt=="6":
			print(Recon_NG)
		elif opt=="7":
				print(ipinfo)
		elif opt=="*":
				exit()
