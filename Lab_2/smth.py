'''class CollectUser:
    SLEEP = 1
    COOKIE_FILE = "cookie.txt"
    AUTH_URL = "http://www.metal-tracker.com/user/login.html"
    COMMENTS_URL = "http://qiqru.org/a2/addcom.php?"
    MAIN_URL = "http://www.metal-tracker.com/"
    ATTEMPTS = 5

    def login(login):
        return login;
    def construct(login, password):
        return login

    form_data = {'UserLogin_username': 'Plag_test', 'UserLogin_password': 'asdfghjkl'}
    params = urlencode(form_data)
    print(params)
    response = urlopen(AUTH_URL)
    data = response.read()
    #print(data)
    #html = urlopen(MAIN_URL)
    webbrowser.open('http://www.metal-tracker.com/user/login.html')
    x = requests.post(AUTH_URL, data=data)
    print(x.text)


        auth = ['Plag_test', 'asdfghjkl']
        curl = pycurl.Curl()
        data = io.StringIO()
        curl.setopt(pycurl.URL, "http://www.metal-tracker.com/user/login.html")
        curl.setopt(pycurl.WRITEFUNCTION, data.write)
        curl.setopt(pycurl.FOLLOWLOCATION, 1)
        curl.setopt(pycurl.COOKIEJAR, COOKIE_FILE)
        curl.setopt(pycurl.COOKIEFILE, COOKIE_FILE)
        curl.setopt(pycurl.POSTFIELDS, 'auth_token=' + hash + '&UserLogin_username=' + auth[0] + '&UserLogin_password=' + auth[1])
        curl.setopt(pycurl.POST, 1)
        curl.perform()
        print(data.getvalue())

   c = pycurl.Curl()
    s = io.StringIO()
    c.setopt(pycurl.URL, AUTH_URL)
    c.setopt(pycurl.HEADER, True)
    c.setopt(pycurl.NOBODY, True)
    c.setopt(pycurl.WRITEFUNCTION, s.write)
    c.perform()

   # print(s.getvalue())
   # for i in range(50):
  #      buf = io.StringIO()
   #     c = pycurl.Curl()
  #      c.setopt(c.URL, AUTH_URL)
  #  #    c.setopt(c.WRITEFUNCTION, buf.write)
  #      c.perform()
   #     #print (buf.getvalue())
   #     buf.close()
    params = {
        'arg1': 'UserLogin_username',
        'arg2': 'UserLogin_password',
        #'arg3': 'demo@gmail.com',
        # И так далее.
        }
    auth = ('Plag_test', 'asdfghjkl')
    r = requests.post(AUTH_URL, params=params, auth=auth)
    if r.text == 0:
        print('OK')
    else:
print('Error code: %s' % r.text)'''

def write_data( buf ):
    global wr_buf
    wr_buf += buf


def main():
    c = pycurl.Curl()
    c.setopt( pycurl.URL, 'http://www.exampledomain.com' )
    c.setopt(pycurl.WRITEFUNCTION,write_data())
    c.perform()
    c.close()
    sys.stdout.write(wr_buf)
    print(wr_buf)