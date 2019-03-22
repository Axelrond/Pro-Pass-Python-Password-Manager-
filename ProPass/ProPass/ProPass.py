import string
import random
import winsound
import sys
import math
import os
import colorama
from colorama import Fore, Back, Style

winsound.Beep(300,200)
winsound.Beep(500,200)

colorama.init()

text = '''
         ____                   ____                 
    / __ \_________        / __ \____ ___________
   / /_/ / ___/ __ \______/ /_/ / __ `/ ___/ ___/
  / ____/ /  / /_/ /_____/ ____/ /_/ (__  |__  ) 
 /_/   /_/   \____/     /_/    \__,_/____/____/  
 P Y T H O N    P A S S W O R D    M A N A G E R 
                                            v.1
   '''
print(Fore.BLUE + text + Style.RESET_ALL)


print ('''
    Type "add" to create a new password

    Type "list" to see all of your password(s)

    Type "help" to display help text

    Type "exit" to close program                 
                                            ''')
print()



master_list = []

def new_password():

    website = input('What is the website? ')

    username = input('What is the username? ')

    password = input('What is the password? ')

    if password == 'random':

        ordinal = int(input('How many characters long should the password be? '))
        random_password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(ordinal))
        print(f'Here is the random password: {random_password}')
        password = random_password
        pass

        def save():
            if choice == 'save':
                print("Saved!")
                winsound.Beep(500,200)
                string = str (masterlist)
                myfile = open('music.txt', 'w')
                myfile.write(string)
                myfile.close()
                (...)
                os.system("PAUSE")
    else:

        pass

    

    website_entry = dict([("website", website), ("username", username), ("password", password)]) 
    master_list.append(website_entry)
    print(master_list)


#load
def list_password():
    web_query = input('What website is it for? ')
    anything_found = False
    for entry in master_list:
        if web_query == entry['website']:

            text = '''
            Password list:
            '''
            print(Fore.BLUE + text + Style.RESET_ALL)
            print('Username is:' + entry['username'])
            print('Password is:' + entry['password'])
            anything_found = True

    if not(anything_found):
        print("Website doesn't exist")
        pass

def exit():
      if exit == 'exit':
          text = '''
          Goodbye!
          '''
          print(Fore.BLUE + text + Style.RESET_ALL)
      winsound.Beep(500,200)
      winsound.Beep(300,200)
      sys.exit()
      pass
                       
while True:
    print('''
    \n
   ''')

    user_input = input('Choose an option... ')

    if user_input == 'add':
        winsound.Beep(500,200)
        new_password()

    elif user_input == 'list':
        winsound.Beep(500,200)
        list_password()

    elif user_input == 'help':
         winsound.Beep(500,200)
         text = '''
         Remember to type "save" after you have entered your data!"
         All of your files will be saved in .txt format
         '''
         print(Fore.BLUE + text + Style.RESET_ALL)
         (...)
         os.system("PAUSE")
         pass

    elif user_input == 'exit':
        exit()