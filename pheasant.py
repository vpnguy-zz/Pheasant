import mechanize
import urllib
import sys
if len(sys.argv) < 6 or len(sys.argv) > 6:
	print 'Error: Invalid quanity of parameters'
	print 'Exiting...'
	sys.exit(1)
ip = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
dns1 = sys.argv[4]
dns2 = sys.argv[5]
url = "http://" + ip + "/"
br = mechanize.Browser()
br.add_password(url,username,password)
br.set_handle_robots(False) # ignore robots
mydata=[('dynIPHostName',''),('macAddr','000000000000'),('DNSMode','1'),('dns1',dns1),('dns2',dns2),('pppEnTtl','0'),('submit-url','%2Fwan.asp'),('wanMode','0'),('isApply','ok')]    #The first is the var name the second is the value
mydata=urllib.urlencode(mydata)
res = br.open(url + "/goform/formWanTcpipSetup",mydata)
mydata = [('submit-url',''),('KeyID','')]
mydata=urllib.urlencode(mydata)
res = br.open(url + "goform/formApply",mydata)