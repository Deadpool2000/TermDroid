import os
try:    
    os.system('echo "\e[93m"')
    print("""
############################################################
#   _______ ______ _____  __  __ _____            _     _  #
#  |__   __|  ____|  __ \|  \/  |  __ \          (_)   | | #
#     | |  | |__  | |__) | \  / | |  | |_ __ ___  _  __| | #
#     | |  |  __| |  _  /| |\/| | |  | | '__/ _ \| |/ _` | #
#     | |  | |____| | \ \| |  | | |__| | | | (_) | | (_| | #
#     |_|  |______|_|  \_\_|  |_|_____/|_|  \___/|_|\__,_| #
#                                                          #
#       GUI Installer for Linux running on Termux (v2.0)   #
############################################################

Note: Before using,please read README.md file""")
    def list():
        print("""
#################################################################

--> Select your operating system for installation

1) Arch Linux
2) Kali Linux/Nethunter
3) Ubuntu
4) Debian
5) Parrot OS
00) Exit\n""")
    def l1():
        os.system('echo "Default \e[96m"')
        print("""
#################################################################

--> Choose which type of Desktop Environment

1) LXDE Desktop Environment
2) XFCE Desktop Environment
3) MATE Desktop Environment
00) Exit\n""")
    list()
    def cho():
        q=input(">>> Select your choice: ")
        if q=="1":
            l1()
            def arch():
                q=input(">>> Select your choice: ")
                if q=="1":
                    os.system('echo "\e[92m"')
                    print("\nInstalling LXDE for Arch Linux")
                    os.system('cd /home/')
                    os.system('pacman -Sy && pacman -Syu')
                    os.system('echo "\e[92m"')
                    print("#################################################################\n")
                    print("Installing LXDE................")
                    os.system('pacman -S --noconfirm lxde')
                    os.system('systemctl enable lxdm')
                    os.system('pacman -S --noconfirm tigervnc')
                    print("#################################################################\n")
                    os.system('echo "\e[95m"')
                    print("Now start XFCE using vncserver")
                    print("Good Bye")
                elif q=="2":
                    os.system('echo "\e[92m"')
                    print("\nInstalling XFCE for Arch Linux")
                    os.system('cd /home/')
                    os.system('pacman -Sy && pacman -Syu')
                    os.system('echo "\e[92m"')
                    print("#################################################################\n")
                    print("Installing XFCE................")
                    os.system('pacman -S --noconfirm xfce4')
                    os.system('systemctl enable lxdm')
                    os.system('pacman -S --noconfirm tigervnc')
                    print("#################################################################\n")
                    os.system('echo "\e[95m"')
                    print("Now start XFCE using vncserver")
                    print("Good Bye")
                elif q=="3":
                    os.system('echo "\e[92m"')
                    print("\nInstalling MATE Desktop for Arch Linux")
                    os.system('cd /home/')
                    os.system('echo "\e[92m"')
                    os.system('pacman -Sy && pacman -Syu')
                    os.system('echo "\e[92m"')
                    print("#################################################################\n")
                    print("Installing XFCE................")
                    os.system('pacman -S --noconfirm mate mate-extra')
                    os.system('pacman -S --noconfirm tigervnc')
                    print("#################################################################\n")
                    os.system('echo "\e[95m"')
                    print("Now start MATE Desktop using vncserver")
                    print("Good Bye")
                elif q=="00":
                    os.system('echo "\e[34m"')
                    print("\nExit.........\nGood Bye")
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
                    os.system('echo "\e[92m"')
                    print("\nInstalling LXDE for Kali Linux/Nethunter")
                    os.system('cd /home/')
                    os.system('sudo apt-get update -y')
                    print("#################################################################\n")
                    print("Installing LXDE................")
                    os.system('sudo apt-get install lxde-core lxde kali-defaults kali-root-login desktop-base tightvncserver -y')
                    print("#################################################################\n")
                    os.system('echo "\e[95m"')
                    print("Now start LXDE using vncserver")
                    print("Good Bye")
                elif q=="2":
                    os.system('echo "\e[92m"')
                    print("\nInstalling XFCE for Kali Linux/Nethunter")
                    os.system('cd /home/')
                    os.system('sudo apt-get update -y')
                    print("#################################################################\n")
                    print("Installing XFCE................")
                    os.system('sudo apt-get install kali-defaults kali-root-login desktop-base xfce4 xfce4-places-plugin xfce4-goodies tightvncserver -y')
                    print("#################################################################\n")
                    os.system('echo "\e[95m"')
                    print("Now start XFCE using vncserver")
                    print("Good Bye")
                elif q=="3":
                    os.system('echo "\e[92m"')
                    print("\nInstalling MATE Desktop for Kali Linux/Nethunter")
                    os.system('cd /home/')
                    os.system('echo "\e[92m"')
                    os.system('sudo apt-get update -y')
                    print("#################################################################\n")
                    os.system('echo "\e[92m"')
                    print("Installing MATE................")
                    os.system('sudo apt-get install mate tightvncserver -y')
                    print("#################################################################\n")
                    os.system('echo "\e[95m"')
                    print("Now start MATE Desktop using vncserver")
                    print("Good Bye")
                elif q=="00":
                    os.system('echo "\e[34m"')
                    print("\nExit.........\nGood Bye")
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
                    print("\nInstalling LXDE for Ubuntu")
                    os.system('cd /home/')
                    os.system('sudo apt-get update -y')
                    print("#################################################################\n")
                    print("Installing LXDE................")
                    os.system('sudo apt-get install lxde tightvncserver -y')
                    print("#################################################################\n")
                    os.system('echo "\e[92m"')
                    print("Now start LXDE using vncserver command")
                    print("Good Bye")
                elif q=="2":
                    os.system('echo "\e[92m"')
                    print("\nInstalling XFCE for Ubuntu")
                    os.system('cd /home/') 
                    os.system('sudo apt-get update -y')
                    print("#################################################################\n")
                    print("Installing XFCE................")
                    os.system('sudo apt-get install xfce4 tightvncserver -y')
                    print("#################################################################\n")
                    os.system('echo "\e[95m"')
                    print("Now start XFCE using vncserver")
                    print("Good Bye")
                elif q=="3":
                    os.system('echo "\e[92m"')
                    print("\nInstalling MATE Desktop for Ubuntu")
                    os.system('cd /home/')
                    os.system('echo "\e[92m"')
                    os.system('sudo apt-get update -y')
                    print("#################################################################\n")
                    os.system('echo "\e[92m"')
                    print("Installing MATE................")
                    os.system('sudo apt-get install mate tightvncserver -y')
                    print("#################################################################\n")
                    os.system('echo "\e[95m"')
                    print("Now start MATE Desktop using vncserver")
                    print("Good Bye")
                elif q=="00":
                    os.system('echo "\e[34m"')
                    print("\nExit.........\nGood Bye")
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
                    print("\nInstalling LXDE for Debian")
                    os.system('cd /home/')
                    os.system('sudo apt-get update -y')
                    print("#################################################################\n")
                    print("Installing LXDE................")
                    os.system('sudo apt-get install lxde tightvncserver -y')
                    print("#################################################################\n")
                    os.system('echo "\e[95m"')
                    print("Now start LXDE using vncserver command")
                    print("Good Bye")
                elif q=="2":
                    os.system('echo "\e[92m"')
                    print("\nInstalling XFCE for Debian")
                    os.system('cd /home/') 
                    os.system('sudo apt-get update -y')
                    print("#################################################################\n")
                    print("Installing XFCE................")
                    os.system('sudo apt-get install xfce4 tightvncserver -y')
                    print("#################################################################\n")
                    os.system('echo "\e[95m"')
                    print("Now start XFCE using vncserver")
                    print("Good Bye")
                elif q=="3":
                    os.system('echo "\e[92m"')
                    print("\nInstalling MATE Desktop for Debian")
                    os.system('cd /home/')
                    os.system('echo "\e[92m"')
                    os.system('sudo apt-get update -y')
                    print("#################################################################\n")
                    os.system('echo "\e[92m"')
                    print("Installing MATE................")
                    os.system('sudo apt-get install mate tightvncserver -y')
                    print("#################################################################\n")
                    os.system('echo "\e[95m"')
                    print("Now start MATE Desktop using vncserver")
                    print("Good Bye")
                elif q=="00":
                    os.system('echo "\e[34m"')
                    print("\nExit.........\nGood Bye")
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
                    print("\nInstalling LXDE for Parrot OS")
                    os.system('cd /home/')
                    os.system('sudo apt-get update -y')
                    print("#################################################################\n")
                    print("Installing LXDE................")
                    os.system('sudo apt-get install lxde tightvncserver -y')
                    print("#################################################################\n")
                    os.system('echo "\e[92m"')
                    print("Now start LXDE using vncserver command")
                    print("Good Bye")
                elif q=="2":
                    os.system('echo "\e[92m"')
                    print("\nInstalling XFCE for Parrot OS")
                    os.system('cd /home/') 
                    os.system('sudo apt-get update -y')
                    print("#################################################################\n")
                    print("Installing XFCE................")
                    os.system('sudo apt-get install xfce4 tightvncserver -y')
                    print("#################################################################\n")
                    os.system('echo "\e[95m"')
                    print("Now start XFCE using vncserver")
                    print("Good Bye")
                elif q=="3":
                    os.system('echo "\e[92m"')
                    print("\nInstalling MATE Desktop for Parrot OS")
                    os.system('cd /home/')
                    os.system('echo "\e[92m"')
                    os.system('sudo apt-get update -y')
                    print("#################################################################\n")
                    os.system('echo "\e[92m"')
                    print("Installing MATE................")
                    os.system('sudo apt-get install mate tightvncserver -y')
                    print("#################################################################\n")
                    os.system('echo "\e[95m"')
                    print("Now start MATE Desktop using vncserver")
                    print("Good Bye")
                elif q=="00":
                    os.system('echo "\e[34m"')
                    print("\nExit.........\nGood Bye")
                else:
                    os.system('echo "\e[91m"')
                    print("\nInvalid option! Please try again :(\n")
                    l1()
                    par()
            par()
        elif q=="00":
            os.system('echo "\e[34m"')
            print("\nExit.........\nGood Bye")
        else:
            os.system('echo "\e[91m"')
            print("\nInvalid option! Please try again :(\n")
            list()
            cho()
    cho()
    print("#################################################################\n")
    print("######## Code by : Deadpool2000 ##########")
    print("######## Email : thetrickboy007@gmail.com ###########\n")
    print("#################################################################")
    
except KeyboardInterrupt:
    print("\nInterrupted ! Exit........................")
