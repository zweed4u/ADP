import json, time, requests, getpass, BeautifulSoup
session=requests.session()
username=str(raw_input('Username: '))
passwd=getpass.getpass()
headers={
	'host':                'mobile2.adp.com',
	'Content-Type':        'application/json',
	'Accept':              'application/json',
	'Proxy-Connection':    'close',
	'Accept-Charset':      'UTF-8',
	'Lang-Locale':         'en-US',
	'Accept-Language':     'en-US',
	'Accept-Encoding':     'gzip',
	'consumerappoid':      'ADPMOBILE',
	'Requested-Language':  'en-US',
	'User-Agent':          'ADPTablet/2.5.0 (iPhone6,1; iPhone OS 7_1_2 like Mac OS X) Build/1862 sw/320 GPS/1',
	'Connection':          'close'
}
data={
	'USER':username.upper(),
	'password':passwd,
	'TARGET':'https://mobile2.adp.com/api/auth/v1/serverSession'
}
#https://mobile2.adp.com/siteminderagent/forms/login.fcc
loginRes=session.post('https://mobile2.adp.com/api/auth/v1/serverSession',data=data,headers=headers)
headers['Content-Type']=loginRes.content.split('ENCTYPE="')[1].split('"')[0]
postLogUrl='https://mobile2.adp.com'+loginRes.content.split('ACTION="')[1].split('"')[0]
data={loginRes.content.split('" NAME="')[1].split('" ')[0]:loginRes.content.split('" VALUE="')[1].split('">')[0]}
postLogRes=session.post(postLogUrl,data=data,headers=headers)

''' 
print postLogRes.status_code
print postLogRes.url
print postLogRes.content
'''

headers={
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Accept-Encoding':'gzip, deflate',
	'Accept-Language':'en-US,en;q=0.8',
	'Cache-Control':'max-age=0',
	'Connection':'keep-alive',
	'Content-Type':'application/x-www-form-urlencoded',
	'Host':'mobile2.adp.com',
	'Origin':'https://mobile2.adp.com',
	'Referer':postLogRes.url,
	'Upgrade-Insecure-Requests':'1',
	'User-Agent':'ADPTablet/2.5.0 (iPhone6,1; iPhone OS 7_1_2 like Mac OS X) Build/1862 sw/320 GPS/1'
}
data={
	'username':username,
	'g':'1'
}

nameLog=session.post('https://mobile2.adp.com/public/login',data=data,headers=headers)

headers['Referer']='https://mobile2.adp.com/public/login'

data={
	'TARGET':'https://mobile2.adp.com/springboard/s',
	'USER':username,
	'password':passwd
}


passLog=session.post('https://mobile2.adp.com/siteminderagent/forms/login.fcc',data=data,headers=headers)
sRes=session.get('https://mobile2.adp.com/springboard/s',headers=headers)

headers['Referer']=sRes.url
payLog=session.get('https://mobile2.adp.com/payroll/',headers=headers)
soup=BeautifulSoup.BeautifulSoup(payLog.content)
payChecks=soup.findAll("ul",{"class":"tableview amts m-top"})[0]
print payChecks
