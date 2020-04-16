
from twilio.rest import Client
import os
import time

def globalVariableIKnow():
    global counter
    counter = 0

def notifyMe():
    client = Client("AC6aab50d8783956d39774870c22c2fa3b", "ad8da443c161de8fdbd11e2606db852b")
    client.messages.create(to="+17272409660",
                        from_="+13392290104",
                        body="Your Computer is being used by some dumbass")

def menu():
    print('Greetings! Please enter the password or this computer will lock')

    passwordShit()

def passwordShit():
    global counter
    content = input('Password:>')
    passwd = 'fuck'
    if content == passwd:
        unlock()
    if content != passwd:
        counter = counter + 1
        print('you have', 3 - counter, ' tries left')
        notifyMe()
        if counter == 3:
            print('Computer Locking time')
            time.sleep(1)
            os.system("shutdown /s /t 1");
    menu()

def unlock():
    os.system('taskkill /F checker.exe')
    os.system('taskkill /F locker.exe')
    print('You are free to go')
    time.sleep(1)
    exit()

def eventLocker():
    with keyboard.Listener(on_press = on_press,) as listener:
        listener.join()


globalVariableIKnow()
menu()
