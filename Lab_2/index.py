# -*- coding: cp1251 -*-
import io
import urllib
import requests
import pycurl
import os
from grab import Grab


class MetalTracker:
    BASE_URL = 'http://www.metal-tracker.com/'

    def auth(self):
        session = requests.Session()
        url = self.BASE_URL + 'user/login.html'
        params = {
            'UserLogin[username]': 'Plag_test',
            'UserLogin[password]': 'asdfghjkl',
            'submit': 'Войти'
        }
        r = session.post(url, params)
        # print(r.text)

    def sendMessage(self):
        session = requests.Session()
        url = self.BASE_URL + 'chat.html'
        params = {
            'ajax': 'True',
            'text': 'smth'
        }
        r = session.get(url, data=params)
        print(r.text)


def main():
 '''  metal = MetalTracker()  # requests(session)
    # metal.auth()
    #metal.sendMessage()
    g = Grab()  # grab
    g.setup(log_file='log.txt', url='http://www.metal-tracker.com')
    if (os.path.getsize('cookie.txt') > 0):
        try:
            g.cookies.load_from_file('cookie.txt')
        except:
            print('empty cookie')
    else:
        g.go('http://www.metal-tracker.com/user/login.html')
        g.doc.set_input('UserLogin[username]', 'Plag_test')
        g.doc.set_input('UserLogin[password]', 'asdfghjkl')
        g.doc.submit()
        g.cookies.save_to_file('cookie.txt')'''


"Plag_test"
'qwerty7'
def test(debug_type, debug_msg):
    if len(debug_msg) < 300:
        print ("debug(%d): %s" % (debug_type, debug_msg.strip()))

def connect(base_url, ref_url , pf):
    fields = urllib.parse.urlencode(pf)
    pageBody = io.BytesIO()
    pageHead = io.BytesIO()
    p = pycurl.Curl()
    p.setopt(pycurl.URL, base_url)
    p.setopt(pycurl.REFERER, ref_url)
    p.setopt(pycurl.FOLLOWLOCATION, 1)
    p.setopt(pycurl.COOKIEFILE, './cookie_test.txt')
    p.setopt(pycurl.COOKIEJAR, './cookie_test.txt')
    p.setopt(pycurl.POST, 1)
    p.setopt(pycurl.POSTFIELDS, fields)
    p.setopt(pycurl.HEADERFUNCTION, pageHead.write)
    p.setopt(pycurl.WRITEFUNCTION, pageBody.write)
    p.setopt(pycurl.VERBOSE, True)
    p.setopt(pycurl.DEBUGFUNCTION, test)
    p.perform()

    p.close() # This is mandatory.
    pageBody.seek(0)
    pageHead.seek(0)
    print(pageHead.readlines())
    print (pageBody.readlines())

#def sendMessage(base_url, ref_url , pf):


if __name__ == "__main__":
    pf = {'UserLogin[username]' : 'Plag_test',
          'UserLogin[password]' : 'asdfghjkl',
          'submit' : 'Войти'}
    connect('http://www.metal-tracker.com/user/login.html', 'http://www.metal-tracker.com/user/login.html', pf)
    pf2 = {'lastID' : '',
           'text' : 'Hello! Plag was here!'}
    connect('http://www.metal-tracker.com/chat/?ajax=true', 'http://www.metal-tracker.com/chat/index.php', pf2)
    pf3 = {'user' : '926252989',
           'text' : "<p>Hello! It's just a test message.</p>"}
    connect('http://www.metal-tracker.com/messages/send.html', 'http://www.metal-tracker.com/profile/926252989.html', pf3)
    pf4 = {'my_post_key' : '7ea8dc2c7ad448fbe1aeefabb4ea46ff',
           'subject' : 'RE: Progressive Metal Bands indication pleaseee',
           'action' : 'do_newreply',
           'posthash' : '',
           'quoted_ids' : '',
           'lastpid' : '55194',
           'from_page' : '1',
           'tid' : '3314',
           'method' : 'quickreply',
           'message' : 'Plag was here!',
           'previewpost' : 'Предварительный просмотр'
           }
    connect('http://www.metal-tracker.com/forum/newreply.php?ajax=1', 'http://www.metal-tracker.com/forum/showthread.php?tid=3314&pid=55194', pf4)
    main()