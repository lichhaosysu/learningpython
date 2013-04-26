'''
Created on 2013-2-22

@author: Stefan
'''
import urllib2

proxy_handler = urllib2.ProxyHandler({'http':'http://10.17.75.253:3128'})
proxy_auth_handler = urllib2.ProxyBasicAuthHandler()
opener = urllib2.build_opener(proxy_handler, proxy_auth_handler)
urllib2.install_opener(opener)

f = urllib2.urlopen("http://www.baidu.com/")
print f.readlines()
