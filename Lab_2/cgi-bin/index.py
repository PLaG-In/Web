#!/usr/bin/python
# import webbrowser
import controller

'''login  = Another_user, pass = qwerty7'''
#LOGIN = 'Plag_test'
#PASSWORD = 'asdfghjkl'
TEST_USER = '926252989'
MESSAGE = 'Hello '

def main():
    print("Content-type: text/html\n")
    control = controller.Controller()
    control.sendMessageToChat(MESSAGE)
    control.sendMessageToAnotherUser(MESSAGE, TEST_USER)
    print("Done")
    #metal.sendMessageToForum(MESSAGE) #not universal
    #webbrowser.open('http://www.metal-tracker.com/')


if __name__ == "__main__":
    main()