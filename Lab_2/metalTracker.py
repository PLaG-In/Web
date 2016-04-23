# -*- coding: cp1251 -*-
import io
from urllib import parse
import pycurl

class MetalTracker:
    BASE_URL = 'http://www.metal-tracker.com/'
    AUTH_URL = 'http://www.metal-tracker.com/user/login.html'
    CHAT_URL = 'http://www.metal-tracker.com/chat/'
    MESSAGE_URL = 'http://www.metal-tracker.com/messages/send.html'
    PROFILE_URL = 'http://www.metal-tracker.com/profile/'
    FORUM_URL = 'http://www.metal-tracker.com/forum/'
    COOKIE_FILE = './cookie_test.txt'

    def __init__(self, login, password):
        self.log = login
        self.pas = password
        self.auth(login, password)


    def test(self, debug_type, debug_msg):
        if len(debug_msg) < 300:
            print("debug(%d): %s" % (debug_type, debug_msg.strip()))


    def connect(self, base_url, ref_url, pf):
        fields = parse.urlencode(pf)

        pageBody = io.BytesIO()
        pageHead = io.BytesIO()

        p = pycurl.Curl()

        p.setopt(pycurl.URL, base_url)
        p.setopt(pycurl.REFERER, ref_url)
        p.setopt(pycurl.FOLLOWLOCATION, 1)
        p.setopt(pycurl.COOKIEFILE, self.COOKIE_FILE)
        p.setopt(pycurl.COOKIEJAR, self.COOKIE_FILE)
        p.setopt(pycurl.POST, 1)
        p.setopt(pycurl.POSTFIELDS, fields)
        p.setopt(pycurl.HEADERFUNCTION, pageHead.write)
        p.setopt(pycurl.WRITEFUNCTION, pageBody.write)
        p.setopt(pycurl.VERBOSE, True)
        #p.setopt(pycurl.DEBUGFUNCTION, MetalTracker.test) #for debugging
        p.perform()

        p.close()  # This is mandatory.
        pageBody.seek(0)
        pageHead.seek(0)
        #print(pageHead.readlines())
        #print(pageBody.readlines())


    def auth(self, login, password):
        pf = {
            'UserLogin[username]' : login,
            'UserLogin[password]' : password,
            'submit': 'Войти'
        }
        self.connect(self.AUTH_URL, self.AUTH_URL, pf)


    def sendMessageToChat(self, msg):
        pf = {
            'lastID' : '',
            'text' : msg
        }
        self.connect(self.CHAT_URL + '?ajax=true', self.CHAT_URL + 'index.php', pf)


    def sendMessageToAnotherUser(self, msg, profile):
        pf = {
            'user': profile,
            'text': msg
        }
        self.connect(self.MESSAGE_URL, self.PROFILE_URL + profile + '.html', pf)


    def sendMessageToForum(self, msg):
        pf = {
         'my_post_key': '7ea8dc2c7ad448fbe1aeefabb4ea46ff',
         'subject': 'RE: Progressive Metal Bands indication pleaseee',
         'action': 'do_newreply',
         'posthash': '',
         'quoted_ids': '',
         'lastpid': '55194',
         'from_page': '1',
         'tid': '3314',
         'method': 'quickreply',
         'message': msg,
         'previewpost': 'Предварительный просмотр'
         }
        self.connect(self.FORUM_URL + 'newreply.php?ajax=1' , self.FORUM_URL + 'showthread.php?tid=3314&pid=55194', pf)

    '''Grab realisation --- failed
    metal = MetalTracker()  # requests(session)
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