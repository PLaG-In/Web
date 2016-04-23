import metalTracker

'''login  = Another_user, pass = qwerty7'''
LOGIN = 'Plag_test'
PASSWORD = 'asdfghjkl'
TEST_USER = '926252989'
MESSAGE = 'Plag was here!'

def main():
    metal = metalTracker.MetalTracker(LOGIN, PASSWORD)
    metal.sendMessageToChat(MESSAGE)
    metal.sendMessageToAnotherUser(MESSAGE, TEST_USER)
    #metal.sendMessageToForum(MESSAGE) #not universal


if __name__ == "__main__":
    main()