import socket
import random
import requests
from colorama import Fore
print(Fore.RED + '''


 `7MMF'   `7MF'`7MM"""YMM  `7MN.   `7MF' .g8""8q. `7MMM.     ,MMF'
   `MA     ,V    MM    `7    MMN.    M .dP'    `YM. MMMb    dPMM  
    VM:   ,V     MM   d      M YMb   M dM'      `MM M YM   ,M MM  
     MM.  M'     MMmmMM      M  `MN. M MM        MM M  Mb  M' MM  
     `MM A'      MM   Y  ,   M   `MM.M MM.      ,MP M  YM.P'  MM  
      :MM;       MM     ,M   M     YMM `Mb.    ,dP' M  `YM'   MM  
       VF      .JMMmmmmMMM .JML.    YM   `"bmmd"' .JML. `'  .JMML.


 ''')
print(Fore.RED + '''
--------------------------------------------------------------------------------------------------------------------------
[00] ABOUT
------------
[01] DOS
------------
[02] GENERATE PASSWORD
------------
[03] CHECK IP OF URL
------------
[04] CHECK YOUR HOSTNAME
------------
[05] GENERATE USENAMES
------------
VERSION 0.01
--------------------------------------------------------------------------------------------------------------------------
''')
chinput = input(Fore.GREEN + "[-] SELECT OPTION --> : ")
if chinput == "00":
  print(Fore.YELLOW + '''
--------------------------------------------------------------------------------------------------------------------------

HELLO! 

THE TOOL IS FOR FUNNY

POWERD BY [Z]

 VERSION 0.01

 ITS FUNNY TOOL
  ''')

def DDOS():
  while True:

      host = input(Fore.GREEN + "[-] ENTER HOST --> : ")
      port = int(input(Fore.GREEN + "[-] ENTER PORT --> : "))
      print(Fore.YELLOW + "[+] DDOSING HOST")
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((host, port))
      
  url = input(Fore.GREEN + "[-] ENTER YOUR URL ---> : ")
  r = requests.get(url)
  if [r.status_code == 200]:
    print(Fore.RED + f"[+] FROM HOST --> :  {host} THROUGH PORT --> : {port}")
  else:
    print(Fore.RED + "[-] FAILED TO DDOS")

if chinput == "01":
  DDOS()

def generatepassword():
  while True:
    length = int(input(Fore.GREEN + "[-] ENTER LENGTH OF PASSWORD --> : "))
    print(Fore.YELLOW + "[+] GENERATING PASSWORD")
    password = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()') for i in range(length))
    print(Fore.GREEN + "[+] PASSWORD GENERATED")
    print(Fore.YELLOW + "[+] SENDING PASSWORD")
    print(Fore.GREEN + "[+] PASSWORD SENT")
    print(Fore.YELLOW + "[+] CHECKING PASSWORD")
    print(Fore.GREEN + "[+] PASSWORD CHECKED")
    print(Fore.YELLOW + "[+] SENDING PASSWORD TO SERVER")
    print(Fore.GREEN + "[+] PASSWORD SENT TO SERVER")
    print(Fore.YELLOW + "[+] CHECKING PASSWORD")
    print(Fore.GREEN + "[+] PASSWORD CHECKED")
    print(Fore.YELLOW + "[+] SENDING PASSWORD TO SERVER")
    print(Fore.GREEN + "[+] PASSWORD SENT TO SERVER")
    print(Fore.YELLOW + "[+] CHECKING PASSWORD")
    print(Fore.GREEN + "[+] PASSWORD CHECKED")
    print(password)
    def chechostname():
      hostname = socket.gethostname()
      print(Fore.YELLOW + "[+] CHECKING HOSTNAME")
      print(Fore.GREEN + "[+] HOSTNAME CHECKED")
      print(hostname)
      


def checkurlofip():
  while True:
    url = input(Fore.GREEN + "[-] ENTER URL --> : ")
    print(Fore.YELLOW + "[+] CHECKING URL")
    print(Fore.GREEN + "[+] URL CHECKED")
    print(url)
    ip = socket.gethostbyname(url)
    print(Fore.YELLOW + "[+] CHECKING IP")
    print(Fore.GREEN + "[+] IP CHECKED")
    print(ip)

def generateusername():
  while True:
    length = int(input(Fore.GREEN + "[-] ENTER LENGTH OF USERNAME --> : "))
    print(Fore.YELLOW + "[+] GENERATING USERNAME")
    username = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for i in range(length))
    print(Fore.GREEN + "[+] USERNAME GENERATED")
    print(Fore.YELLOW + "[+] SENDING USERNAME")
    print(Fore.GREEN + "[+] USERNAME SENT")
    print(Fore.YELLOW + "[+] CHECKING USERNAME")
    print(Fore.GREEN + "[+] USERNAME CHECKED")
    print(username)


if chinput == "2":
  generatepassword()
if chinput == "3":
  checkurlofip()
if chinput == "5":
  generateusername()
if chinput == "4":
  chechostname()
else:
  print(Fore.RED + "[-] INVALID OPTION")
