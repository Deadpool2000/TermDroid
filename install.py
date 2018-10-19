import os
def list():
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
#              Desktop Environment Installer               #
############################################################

Desktop Environment Installer for OS running on Termux

Note: Before using,please read README.md file

Select Operating system for installation
1) Arch Linux
2) Kali Linux/Nethunter
3) Ubuntu
4) Debian
00) Exit
""")
def l1():
    os.system('echo "\e[96m"')
    print("""
#################################################################

Choose which type of Desktop Environment
1) LXDE Desktop Environment
2) XFCE Desktop Environment
3) MATE Desktop Environment
""")
list()
q=input("Select your choice: ")
if q=="1":
    l1()
    q=input("Select your choice: ")
    if q=="1":
        os.system('echo "\e[92m"')
        print("Installing LXDE for Arch Linux")
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
        print("Installing XFCE for Arch Linux")
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
        print("Installing MATE Desktop for Arch Linux")
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
    else:
        os.system('echo "\e[91m"')
        print("Invalid option!Please try again :(")
elif q=="2":
    l1()
    q=input("Select your choice: ")
    if q=="1":
        os.system('echo "\e[92m"')
        print("Installing LXDE for Kali Nethunter")
        os.system('cd /home/')
        os.system('apt-get update && apt-get upgrade -y')
        print("#################################################################\n")
        print("Installing LXDE................")
        os.system('apt-get install lxde-core lxde kali-defaults kali-root-login desktop-base tightvncserver -y')
        print("#################################################################\n")
        os.system('echo "\e[95m"')
        print("Now start LXDE using vncserver")
        print("Good Bye")
    elif q=="2":
        os.system('echo "\e[92m"')
        print("Installing XFCE for Kali Nethunter")
        os.system('cd /home/')
        os.system('apt-get update && apt-get upgrade -y')
        print("#################################################################\n")
        print("Installing XFCE................")
        os.system('apt-get install kali-defaults kali-root-login desktop-base xfce4 xfce4-places-plugin xfce4-goodies tightvncserver -y')
        print("#################################################################\n")
        os.system('echo "\e[95m"')
        print("Now start XFCE using vncserver")
        print("Good Bye")
    elif q=="3":
        os.system('echo "\e[92m"')
        print("Installing MATE Desktop for Kali Nethunter")
        os.system('cd /home/')
        os.system('echo "\e[92m"')
        os.system('apt-get update && apt-get upgrade -y')
        print("#################################################################\n")
        os.system('echo "\e[92m"')
        print("Installing MATE................")
        os.system('apt-get install mate tightvncserver -y')
        print("#################################################################\n")
        os.system('echo "\e[95m"')
        print("Now start MATE Desktop using vncserver")
        print("Good Bye")
    else:
        os.system('echo "\e[91m"')
        print("Invalid option!Please try again :(")
elif q=="3":
    l1()
    q=input("Select your choice: ")
    if q=="1":
        print("Installing LXDE for Ubuntu")
        os.system('cd /home/')
        os.system('apt-get update && apt-get upgrade -y')
        print("#################################################################\n")
        print("Installing LXDE................")
        os.system('apt-get install lxde tightvncserver -y')
        print("#################################################################\n")
        os.system('echo "\e[92m"')
        print("Now start LXDE using vncserver command")
        print("Good Bye")
    elif q=="2":
        os.system('echo "\e[92m"')
        print("Installing XFCE for Ubuntu")
        os.system('cd /home/') 
        os.system('apt-get update && apt-get upgrade -y')
        print("#################################################################\n")
        print("Installing XFCE................")
        os.system('apt-get install xfce4 tightvncserver -y')
        print("#################################################################\n")
        os.system('echo "\e[95m"')
        print("Now start XFCE using vncserver")
        print("Good Bye")
    elif q=="3":
        os.system('echo "\e[92m"')
        print("Installing MATE Desktop for Ubuntu")
        os.system('cd /home/')
        os.system('echo "\e[92m"')
        os.system('apt-get update && apt-get upgrade -y')
        print("#################################################################\n")
        os.system('echo "\e[92m"')
        print("Installing MATE................")
        os.system('apt-get install mate tightvncserver -y')
        print("#################################################################\n")
        os.system('echo "\e[95m"')
        print("Now start MATE Desktop using vncserver")
        print("Good Bye")
    else:
        os.system('echo "\e[91m"')
        print("Invalid option!Please try again :(")
elif q=="4":
    l1()
    q=input("Select your choice: ")
    if q=="1":
        print("Installing LXDE for Debian")
        os.system('cd /home/')
        os.system('apt-get update && apt-get upgrade -y')
        print("#################################################################\n")
        print("Installing LXDE................")
        os.system('apt-get install lxde tightvncserver -y')
        print("#################################################################\n")
        os.system('echo "\e[95m"')
        print("Now start LXDE using vncserver command")
        print("Good Bye")
    elif q=="2":
        os.system('echo "\e[92m"')
        print("Installing XFCE for Debian")
        os.system('cd /home/') 
        os.system('apt-get update && apt-get upgrade -y')
        print("#################################################################\n")
        print("Installing XFCE................")
        os.system('apt-get install xfce4 tightvncserver -y')
        print("#################################################################\n")
        os.system('echo "\e[95m"')
        print("Now start XFCE using vncserver")
        print("Good Bye")
    elif q=="3":
        os.system('echo "\e[92m"')
        print("Installing MATE Desktop for Debian")
        os.system('cd /home/')
        os.system('echo "\e[92m"')
        os.system('apt-get update && apt-get upgrade -y')
        print("#################################################################\n")
        os.system('echo "\e[92m"')
        print("Installing MATE................")
        os.system('apt-get install mate tightvncserver -y')
        print("#################################################################\n")
        os.system('echo "\e[95m"')
        print("Now start MATE Desktop using vncserver")
        print("Good Bye")
    else:
        os.system('echo "\e[91m"')
        print("Invalid option!Please try again :(")
elif q=="00":
    os.system('echo "\e[34m"')
    print("Exit.........\nGood Bye")
else:
    os.system('echo "\e[91m"')
    print("Invalid option")
    print("Good Bye")
