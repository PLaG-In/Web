import metalTracker


class Controller:
    BASE_URL = 'http://www.metal-tracker.com/'
    AUTH_URL = 'http://www.metal-tracker.com/user/login.html'
    CHAT_URL = 'http://www.metal-tracker.com/chat/'
    MESSAGE_URL = 'http://www.metal-tracker.com/messages/send.html'
    PROFILE_URL = 'http://www.metal-tracker.com/profile/'
    FORUM_URL = 'http://www.metal-tracker.com/forum/'
    metal = metalTracker.MetalTracker()

    def __init__(self):  # , login, password):
        self.log, self.pas = self.metal.connect_form()
        # self.log = login
        # self.pas = password
        self.auth(self.log, self.pas)

    def auth(self, login, password):
        pf = {
            'UserLogin[username]': login,
            'UserLogin[password]': password,
            'submit': 'Войти'
        }
        self.metal.connect(self.AUTH_URL, self.AUTH_URL, pf)

    def sendMessageToChat(self, msg):
        pf = {
            'lastID': '',
            'text': msg + self.metal.defineLastChatUser(self.CHAT_URL + '?ajax=true',  self.CHAT_URL + 'index.php')
        }
        self.metal.connect(self.CHAT_URL + '?ajax=true', self.CHAT_URL + 'index.php', pf)

    def sendMessageToAnotherUser(self, msg, profile):
        pf = {
            'user': profile,
            'text': msg
        }
        self.metal.connect(self.MESSAGE_URL, self.PROFILE_URL + profile + '.html', pf)

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
        self.metal.connect(self.FORUM_URL + 'newreply.php?ajax=1', self.FORUM_URL + 'showthread.php?tid=3314&pid=55194',
                           pf)
