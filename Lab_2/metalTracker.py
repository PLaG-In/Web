# -*- coding: cp1251 -*-
import io
import cgi
from urllib import parse
import pycurl
import html


class MetalTracker:
    COOKIE_FILE = './cookie_test.txt'
    pageBody = io.BytesIO()
    pageHead = io.BytesIO()

    def test(self, debug_type, debug_msg):
        if len(debug_msg) < 300:
            print("debug(%d): %s" % (debug_type, debug_msg.strip()))

    def connect(self, base_url, ref_url, pf):
        fields = parse.urlencode(pf)

        p = pycurl.Curl()

        p.setopt(pycurl.URL, base_url)
        p.setopt(pycurl.REFERER, ref_url)
        p.setopt(pycurl.FOLLOWLOCATION, 1)
        p.setopt(pycurl.COOKIEFILE, self.COOKIE_FILE)
        p.setopt(pycurl.COOKIEJAR, self.COOKIE_FILE)
        p.setopt(pycurl.POST, 1)
        p.setopt(pycurl.POSTFIELDS, fields)
        p.setopt(pycurl.HEADERFUNCTION, self.pageHead.write)
        p.setopt(pycurl.WRITEFUNCTION, self.pageBody.write)
        p.setopt(pycurl.VERBOSE, True)
        # p.setopt(pycurl.DEBUGFUNCTION, MetalTracker.test) #for debugging
        p.perform()

        p.close()

    def connect_form(self):
        form = cgi.FieldStorage()
        text1 = form.getfirst("Login", "empty field")
        text2 = form.getfirst("Password", "empty field")
        text1 = html.escape(text1)
        text2 = html.escape(text2)
        return (text1, text2)

    def defineLastChatUser(self, base_url, ref_url):
        pf ={'':''}
        MetalTracker.connect(self, base_url, ref_url, pf)
        self.pageBody.seek(0)
        body = self.pageBody.getvalue()
        str = body.decode('iso-8859-1')
        i = str.rindex('<username><![CDATA[', 0, -1) + 19  # 19 symbols after substring index
        username = ''
        while (str[i] != ']'):
            username = username + str[i]
            i = i + 1
        return username
