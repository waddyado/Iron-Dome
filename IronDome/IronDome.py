
from twilio.rest import Client
import os
import time

def globalVariableIKnow():
    global counter
    counter = 0

def notifyMe():
    client = Client("API code", "API Code")
    client.messages.create(to="+Your Number",
                        from_="+Twilio number",
                        body="Your Computer is being used by some dumbass")

def menu():
    print('Greetings! Please enter the password or this computer will lock')

    passwordShit()

def passwordShit():
    global counter
    content = input('Password:>')
    passwd = 'test'
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
