##########thelinuxuxer-choice#################
#############subodha prabash ##########
###########covid19 tracker v 1 ######
# importing the necessary packages 
import time 
import sys 
import os 
  
# Function for implementing the loading animation 
def load_animation(): 
  
    # String to be displayed when the application is loading 
    load_str = "loading covid-tracker..."
    ls_len = len(load_str) 
  
  
    # String for creating the rotating line 
    animation = "|/-\\"
    anicount = 0
      
    # used to keep the track of 
    # the duration of animation 
    counttime = 0        
      
    # pointer for travelling the loading string 
    i = 0                     
  
    while (counttime != 20): 
          
        # used to change the animation speed 
        # smaller the value, faster will be the animation 
        time.sleep(0.075)  
                              
        # converting the string to list 
        # as string is immutable 
        load_str_list = list(load_str)  
          
        # x->obtaining the ASCII code 
        x = ord(load_str_list[i]) 
          
        # y->for storing altered ASCII code 
        y = 0                             
  
        # if the character is "." or " ", keep it unaltered 
        # switch uppercase to lowercase and vice-versa  
        if x != 32 and x != 46:              
            if x>90: 
                y = x-32
            else: 
                y = x + 32
            load_str_list[i]= chr(y) 
          
        # for storing the resultant string 
        res =''              
        for j in range(ls_len): 
            res = res + load_str_list[j] 
              
        # displaying the resultant string 
        sys.stdout.write("\r"+res + animation[anicount]) 
        sys.stdout.flush() 
  
        # Assigning loading string 
        # to the resultant string 
        load_str = res 
  
          
        anicount = (anicount + 1)% 4
        i =(i + 1)% ls_len 
        counttime = counttime + 1
      
    # for windows OS 
    if os.name =="nt": 
        os.system("cls") 
          
    # for linux / Mac OS 
    else: 
        os.system("clear") 
  
# Driver program 
if __name__ == '__main__':  
    load_animation() 
#####end loding######

def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 



############banner

banner = r'''                                                                                          
   ███▄ ▄███▓ ▄▄▄        ██████  ██ ▄█▀  ██████     ▒█████   ███▄    █ 
▓██▒▀█▀ ██▒▒████▄    ▒██    ▒  ██▄█▒ ▒██    ▒    ▒██▒  ██▒ ██ ▀█   █ 
▓██    ▓██░▒██  ▀█▄  ░ ▓██▄   ▓███▄░ ░ ▓██▄      ▒██░  ██▒▓██  ▀█ ██▒
▒██    ▒██ ░██▄▄▄▄██   ▒   ██▒▓██ █▄   ▒   ██▒   ▒██   ██░▓██▒  ▐▌██▒
▒██▒   ░██▒ ▓█   ▓██▒▒██████▒▒▒██▒ █▄▒██████▒▒   ░ ████▓▒░▒██░   ▓██░
░ ▒░   ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░▒ ▒▒ ▓▒▒ ▒▓▒ ▒ ░   ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
░  ░      ░  ▒   ▒▒ ░░ ░▒  ░ ░░ ░▒ ▒░░ ░▒  ░ ░     ░ ▒ ▒░ ░ ░░   ░ ▒░
░      ░     ░   ▒   ░  ░  ░  ░ ░░ ░ ░  ░  ░     ░ ░ ░ ▒     ░   ░ ░   v 1.0
       ░         ░  ░      ░  ░  ░         ░         ░ ░           ░   by thelinuxuser-choice
                                                                       please note sometimes it will take time or give errors
                                                                       because this api has lot of requests
'''

prRed(banner)

from time import sleep
import sys
line_1 = "Please use masks before going out ... "
for x in line_1:
    print(x, end='')
    sys.stdout.flush()
    sleep(0.1)

prCyan("\nmasks on dude!")





import COVID19Py
covid19 = COVID19Py.COVID19()

prCyan("Enter No 1 to get latest info about global covid 19 situation")
prCyan("Enter no 2 to get latest info about country covid 19 situation")


option = input(''' ┌─[ covid19-tracker@thelinuxuser-choice ]─[~]
 └──╼ # ''')



if option == "1":
      latest = covid19.getLatest()
      prYellow(latest)

elif option == "2" :
        c=input("country to track {ex :LK =srilanka(capital)} =")
        location = covid19.getLocationByCountryCode(f'{c}')       
        prYellow(location)
