# -*- coding:UTF-8 -*-
'''
======================================
此程序根据 http://www.oschina.net/code/snippet_148170_10661 内容改编
Adapted BY: bepcao
Mail:peterc9511@gmail.com
======================================
'''
from sgmllib import SGMLParser
import sys, urllib2, urllib, cookielib
import datetime
import time
'''
reload(sys)
sys.setdefaultencoding('gbk')
print sys.getdefaultencoding()

sys.setdefaultencoding('utf-8')
print sys.getdefaultencoding()
'''
class spider(SGMLParser):
    def __init__(self, email, password):
        SGMLParser.__init__(self)
        self.h3 = False
        self.h3_is_ready = False
        self.div = False
        self.h3_and_div = False
        self.a = False
        self.depth = 0
        self.names = ""
        self.dic = {}   
         
        self.email = email
        self.password = password
        self.domain = 'renren.com'
        
        try:
            cookie = cookielib.CookieJar()
            cookieProc = urllib2.HTTPCookieProcessor(cookie)
        except:
            raise
        else:
            proxy_handler = urllib2.ProxyHandler({'http':'http://10.17.75.253:3128'})
            proxy_auth_handler = urllib2.ProxyBasicAuthHandler()
#            opener = urllib2.build_opener(proxy_handler, proxy_auth_handler)
            opener = urllib2.build_opener(cookieProc, proxy_handler, proxy_auth_handler)
            urllib2.install_opener(opener)       

    def login(self):
        print '开始登录'
        url = 'http://www.renren.com/PLogin.do'
        postdata = {
                  'email':self.email,
                  'password':self.password,
                  'domain':self.domain  
                  }
        req = urllib2.Request(
                            url,
                            urllib.urlencode(postdata)            
                            )
        
        self.file = urllib2.urlopen(req).read()
        idPos = self.file.index("'id':'")
        self.id = self.file[idPos + 6:idPos + 15]
        tokPos = self.file.index("get_check:'")
        self.tok = self.file[tokPos + 11:tokPos + 21]
        rtkPos = self.file.index("get_check_x:'")
        self.rtk = self.file[rtkPos + 13:rtkPos + 21]
    


    def publish(self, content):
        url1 = 'http://shell.renren.com/' + self.id + '/status'
        postdata = {
                  'content':content,
                  'hostid':self.id,
                  'requestToken':self.tok,
                  '_rtk':self.rtk,
                  'channel':'renren',
                  }
        req1 = urllib2.Request(
                            url1,
                            urllib.urlencode(postdata)      
                            )
        self.file1 = urllib2.urlopen(req1).read()
        print '%s:\n刚才使用你的人人账号 %s 发了一条状态\n内容为：(%s)' % (datetime.datetime.now(), self.email, postdata.get('content', ''))



renrenspider = spider('740230215@qq.com', '123456Qw')
renrenspider.login()
content = raw_input('请输入状态的内容：')
renrenspider.publish(content)

