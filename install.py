import os
os.system('clear')
try:    
    os.system('echo "\e[93m"')
    print("""
#############################################################
#   _______ ______ _____  __  __ _____            _     _   #
#  |__   __|  ____|  __ \|  \/  |  __ \          (_)   | |  #
#     | |  | |__  | |__) | \  / | |  | |_ __ ___  _  __| |  #
#     | |  |  __| |  _  /| |\/| | |  | | '__/ _ \| |/ _` |  #
#     | |  | |____| | \ \| |  | | |__| | | | (_) | | (_| |  #
#     |_|  |______|_|  \_\_|  |_|_____/|_|  \___/|_|\__,_|  #
#                                                           #
#       GUI Installer for Linux running on Termux (v2.0)    #
#                                                           #
#############################################################

         Note: Before using,please read README.md """)
    def list():
        os.system('echo "\e[92m"')
        print("""
#################################################################

--> Select your operating system for installation

1) Arch Linux
2) Kali Linux/Nethunter
3) Ubuntu
4) Debian
5) Parrot OS

99) Exit\n""")
    def l1():
        os.system('echo "\e[96m"')
        print("""
#################################################################

--> Choose which type of Desktop Environment

1) LXDE Desktop Environment
2) XFCE Desktop Environment
3) MATE Desktop Environment

99) Back to main menu\n""")
    list()
    def cho():
        q=input(">>> Select your choice: ")
        if q=="1":
            l1()
            def arch():
                os.system('echo "\e[97m"')
                q=input(">>> Select your choice: ")
                if q=="1":
                    os.system('echo "\e[93m"')
                    print("\nInstalling LXDE for Arch Linux\n")
                    os.system('echo "\e[97m"')
                    os.system('cd /home/')
                    os.system('pacman -Sy && pacman -Syu')                    
                    print("#################################################################\n")
                    print("Installing LXDE................\n")
                    os.system('pacman -S --noconfirm lxde')
                    os.system('systemctl enable lxdm')
                    os.system('pacman -S --noconfirm tigervnc')
                    print("#################################################################\n")
                    os.system('echo "\e[92m"')
                    print("Now start XFCE using vncserver")
                    print("Good Bye")
                    os.system('echo "\e[97m"')
                elif q=="2":
                    os.system('echo "\e[93m"')
                    print("\nInstalling XFCE for Arch Linux\n")
                    os.system('echo "\e[97m"')
                    os.system('cd /home/')
                    os.system('pacman -Sy && pacman -Syu')
                    print("#################################################################\n")
                    print("Installing XFCE................\n")
                    os.system('pacman -S --noconfirm xfce4')
                    os.system('systemctl enable lxdm')
                    os.system('pacman -S --noconfirm tigervnc')
                    print("#################################################################\n")
                    os.system('echo "\e[92m"')
                    print("Now start XFCE using vncserver")
                    print("Good Bye")
                    os.system('echo "\e[97m"')
                elif q=="3":
                    os.system('echo "\e[93m"')
                    print("\nInstalling MATE Desktop for Arch Linux\n")
                    os.system('echo "\e[97m"')
                    os.system('cd /home/')
                    os.system('pacman -Sy && pacman -Syu')                    
                    print("#################################################################\n")
                    print("Installing XFCE................\n")
                    os.system('pacman -S --noconfirm mate mate-extra')
                    os.system('pacman -S --noconfirm tigervnc')
                    print("#################################################################\n")
                    os.system('echo "\e[92m"')
                    print("Now start MATE Desktop using vncserver")
                    print("Good Bye")
                    os.system('echo "\e[97m"')
                elif q=="99":                    
                    list()
                    cho()                    
                else:
                    os.system('echo "\e[91m"')
                    print("\nInvalid option! Please try again :(\n")
                    l1()
                    arch()
            arch()
        elif q=="2":
            l1()
            def kali():
                q=input(">>> Select your choice: ")
                if q=="1":
                    os.system('echo "\e[93m"')
                    print("\nInstalling LXDE for Kali Linux/Nethunter\n")
                    os.system('echo "\e[97m"')
                    os.system('cd /home/')
                    os.system('sudo apt-get update -y')
                    print("#################################################################\n")
                    print("Installing LXDE................\n")
                    os.system('sudo apt-get install lxde-core lxde kali-defaults kali-root-login desktop-base tightvncserver -y')
                    print("#################################################################\n")
                    os.system('echo "\e[92m"')
                    print("Now start LXDE using vncserver")
                    print("Good Bye")
                    os.system('echo "\e[97m"')
                elif q=="2":
                    os.system('echo "\e[93m"')
                    print("\nInstalling XFCE for Kali Linux/Nethunter\n")
                    os.system('echo "\e[97m"')
                    os.system('cd /home/')
                    os.system('sudo apt-get update -y')
                    print("#################################################################\n")
                    print("Installing XFCE................\n")
                    os.system('sudo apt-get install kali-defaults kali-root-login desktop-base xfce4 xfce4-places-plugin xfce4-goodies tightvncserver -y')
                    print("#################################################################\n")
                    os.system('echo "\e[92m"')
                    print("Now start XFCE using vncserver")
                    print("Good Bye")
                    os.system('echo "\e[97m"')
                elif q=="3":
                    os.system('echo "\e[93m"')
                    print("\nInstalling MATE Desktop for Kali Linux/Nethunter\n")
                    os.system('cd /home/')
                    os.system('echo "\e[97m"')                    
                    os.system('sudo apt-get update -y')
                    print("#################################################################\n")                    
                    print("Installing MATE................\n")
                    os.system('sudo apt-get install mate tightvncserver -y')
                    print("#################################################################\n")
                    os.system('echo "\e[92m"')
                    print("Now start MATE Desktop using vncserver")
                    print("Good Bye")
                    os.system('echo "\e[97m"')
                elif q=="99":
                    list()
                    cho() 
                else:
                    os.system('echo "\e[91m"')
                    print("\nInvalid option! Please try again :(\n")
                    l1()
                    kali()
            kali()
        elif q=="3":
            l1()
            def ubu():
                q=input(">>> Select your choice: ")
                if q=="1":
                    os.system('echo "\e[93m"')
                    print("\nInstalling LXDE for Ubuntu\n")
                    os.system('echo "\e[97m"')
                    os.system('cd /home/')
                    os.system('sudo apt-get update -y')
                    print("#################################################################\n")
                    print("Installing LXDE................\n")
                    os.system('sudo apt-get install lxde tightvncserver -y')
                    print("#################################################################\n")                    
                    print("Now start LXDE using vncserver command")
                    print("Good Bye")
                    os.system('echo "\e[97m"')
                elif q=="2":
                    os.system('echo "\e[93m"')
                    print("\nInstalling XFCE for Ubuntu\n")
                    os.system('echo "\e[97m"')
                    os.system('cd /home/') 
                    os.system('sudo apt-get update -y')
                    print("#################################################################\n")
                    print("Installing XFCE................\n")
                    os.system('sudo apt-get install xfce4 tightvncserver -y')
                    print("#################################################################\n")
                    os.system('echo "\e[92m"')
                    print("Now start XFCE using vncserver")
                    print("Good Bye")
                    os.system('echo "\e[97m"')
                elif q=="3":
                    os.system('echo "\e[93m"')
                    print("\nInstalling MATE Desktop for Ubuntu\n")
                    os.system('echo "\e[97m"')
                    os.system('cd /home/')                    
                    os.system('sudo apt-get update -y')
                    print("#################################################################\n")                    
                    print("Installing MATE................\n")
                    os.system('sudo apt-get install mate tightvncserver -y')
                    print("#################################################################\n")
                    os.system('echo "\e[92m"')
                    print("Now start MATE Desktop using vncserver")
                    print("Good Bye")
                elif q=="99":
                    list()
                    cho() 
                else:
                    os.system('echo "\e[91m"')
                    print("\nInvalid option! Please try again :(\n")
                    l1()
                    ubu()
            ubu()
        elif q=="4":
            l1()
            def deb():
                q=input(">>> Select your choice: ")
                if q=="1":
                    os.system('echo "\e[93m"')
                    print("\nInstalling LXDE for Debian\n")
                    os.system('echo "\e[97m"')
                    os.system('cd /home/')
                    os.system('sudo apt-get update -y')
                    print("#################################################################\n")
                    print("Installing LXDE................\n")
                    os.system('sudo apt-get install lxde tightvncserver -y')
                    print("#################################################################\n")
                    os.system('echo "\e[92m"')
                    print("Now start LXDE using vncserver command")
                    print("Good Bye")
                    os.system('echo "\e[97m"')
                elif q=="2":
                    os.system('echo "\e[93m"')
                    print("\nInstalling XFCE for Debian\n")
                    os.system('echo "\e[97m"')
                    os.system('cd /home/') 
                    os.system('sudo apt-get update -y')
                    print("#################################################################\n")
                    print("Installing XFCE................\n")
                    os.system('sudo apt-get install xfce4 tightvncserver -y')
                    print("#################################################################\n")
                    os.system('echo "\e[92m"')
                    print("Now start XFCE using vncserver")
                    print("Good Bye")
                    os.system('echo "\e[97m"')
                elif q=="3":
                    os.system('echo "\e[93m"')
                    print("\nInstalling MATE Desktop for Debian\n")
                    os.system('echo "\e[97m"')
                    os.system('cd /home/')                    
                    os.system('sudo apt-get update -y')
                    print("#################################################################\n")                    
                    print("Installing MATE................\n")
                    os.system('sudo apt-get install mate tightvncserver -y')
                    print("#################################################################\n")
                    os.system('echo "\e[92m"')
                    print("Now start MATE Desktop using vncserver")
                    print("Good Bye")
                    os.system('echo "\e[97m"')
                elif q=="99":
                    list()
                    cho() 
                else:
                    os.system('echo "\e[91m"')
                    print("\nInvalid option! Please try again :(\n")
                    l1()
                    deb()
            deb()
        elif q=="5":
            l1()
            def par():
                q=input(">>> Select your choice: ")
                if q=="1":
                    os.system('echo "\e[93m"')
                    print("\nInstalling LXDE for Parrot OS\n")
                    os.system('echo "\e[97m"')
                    os.system('cd /home/')
                    os.system('sudo apt-get update -y')
                    print("#################################################################\n")
                    print("Installing LXDE................\n")
                    os.system('sudo apt-get install lxde tightvncserver -y')
                    print("#################################################################\n")
                    os.system('echo "\e[92m"')
                    print("Now start LXDE using vncserver command")
                    print("Good Bye")
                    os.system('echo "\e[97m"')
                elif q=="2":
                    os.system('echo "\e[93m"')
                    print("\nInstalling XFCE for Parrot OS\n")
                    os.system('echo "\e[97m"')
                    os.system('cd /home/') 
                    os.system('sudo apt-get update -y')
                    print("#################################################################\n")
                    print("Installing XFCE................\n")
                    os.system('sudo apt-get install xfce4 tightvncserver -y')
                    print("#################################################################\n")
                    os.system('echo "\e[92m"')
                    print("Now start XFCE using vncserver")
                    print("Good Bye")
                    os.system('echo "\e[97m"')
                elif q=="3":
                    os.system('echo "\e[93m"')
                    print("\nInstalling MATE Desktop for Parrot OS")
                    os.system('echo "\e[97m"')
                    os.system('cd /home/')                    
                    os.system('sudo apt-get update -y')
                    print("#################################################################\n")                
                    print("Installing MATE................")
                    os.system('sudo apt-get install mate tightvncserver -y')
                    print("#################################################################\n")
                    os.system('echo "\e[92m"')
                    print("Now start MATE Desktop using vncserver")
                    print("Good Bye")
                    os.system('echo "\e[97m"')
                elif q=="99":
                    list()
                    cho() 
                else:
                    os.system('echo "\e[91m"')
                    print("\nInvalid option! Please try again :(\n")
                    l1()
                    par()
            par()
        elif q=="99":
            os.system('echo "\e[93m"')
            print("\nExit.........\nGood Bye")
            os.system('echo "\e[97m"')
        else:
            os.system('echo "\e[91m"')
            print("\nInvalid option! Please try again :(\n")
            list()
            cho()
    cho()
    os.system('echo "\e[93m"')    
    print("""
#################################################################\n
                    Code by : Deadpool2000 
                Email : thetrickboy007@gmail.com \n
#################################################################""")
    os.system('echo "\e[97m"')
    
    
except KeyboardInterrupt:
    os.system('echo "\e[93m"')
    print("\nInterrupted ! Exit........................")
    os.system('echo "\e[97m"')
