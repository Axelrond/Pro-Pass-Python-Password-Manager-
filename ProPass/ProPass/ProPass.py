import string
import random
import winsound
import sys

masterlist = []

winsound.Beep(300,200)
winsound.Beep(500,200)

# menu entry
print('''
    
    
         ____                   ____                 
    / __ \_________        / __ \____ ___________
   / /_/ / ___/ __ \______/ /_/ / __ `/ ___/ ___/
  / ____/ /  / /_/ /_____/ ____/ /_/ (__  |__  ) 
 /_/   /_/   \____/     /_/    \__,_/____/____/  
 P Y T H O N    P A S S W O R D    M A N A G E R 
                                            v.1
    
    Hello!


    

    Type "add" to create a new password

    Type "list" to see all of your password(s)

    Type "help" to display help text

    Type "exit" to close program

   ''')
pass


def new_password():
    choice = input('What do you want to do? ')
if choice == 'add':


        print("Please enter information: ")

        winsound.Beep(500,200)

        website = input('Enter Website ')

        username = input('Enter Username ')

        password = input('Enter Password ')

        secret_question = input('Enter Secret Question (if there is no secret question, type "none") ')

        # function for randomized password input
        if password == 'random':
            num_of_digits = int(input('Character length of password? '))
            random_password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range (num_of_digits))
            print (f'Here is the random password: {random_password}')
            password = random_password
        else:
            pass
        website_entry = dict([("website", website), ("username", username), ("password", password)]) 
        password_list.append(website_entry)
        print(password_list)
        if len(masterlist) <=999:

            masterlist.append(new)
        else:
            print(masterlist)
        website_entry
        print ("\nYou cannot exceed 999 entries! ")
        pass
      
# function for launching main file assets
def list_passwords():

    if choice == 'list':

        pass

    else:

        print("Error!")
        winsound.Beep(500,200)
        for thing in masterlist:

            print('''beep beep boop...
            
            
           OK! here's the list! ''')

            for key, value in thing.items():

                print(f'{key} is {value}')

try:
   
    with open('passwords.txt', 'r') as myfile:

     mastertext = myfile.read()

     passwords.masterlist = eval(mastertext)

     print(masterlist)

except:

    masterlist = []
    pass
   


    def save():

        if choice == 'save':

         print("Saved!")

        winsound.Beep(500,200)

        string = str (masterlist)

        myfile = open('music.txt', 'w')

        myfile.write(string)

        myfile.close()
        pass

    def help():

        if choice == 'help':

         winsound.Beep(500,200)

        print('\n Remember to type "save" after you have entered your data!')

        print('\n All of your files will be saved in .txt format')
        pass


# exit function
    def exit():

        if choice == 'exit':

         print('\n Goodbye!')

        winsound.Beep(500,200)
        winsound.Beep(300,200)
        sys.exit()
        pass


