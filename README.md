# TermDroid
Desktop Environment Installer for various OS running on Termux

![screenshot_termux_20181019-202436 2](https://user-images.githubusercontent.com/32305505/47226191-8527a080-d3dd-11e8-9ddc-68182f546140.png)


## Installation
1) git clone https://github.com/Deadpool2000/TermDroid.git
2) chmod +x install.py
3) python3 install.py

## Note: 

### 1) Use Python 3.x or upper version

### 2) If your phone have 2GB+ RAM then install MATE Desktop Environment otherwise install LXDE or XFCE

## How to use
### 1) LXDE Desktop Environment 
DISPLAY=:<session_number> startlxde &

e.g. DISPLAY=:1 startlxde &

### 2) XFCE4 Desktop Environment 
DISPLAY=:<session_number> startxfce4 &

e.g. DISPLAY=:1 startxfce4 &

### 3) MATE Desktop Environment 
DISPLAY=:<session_number> mate-session &

e.g. DISPLAY=:1 mate-session &

#### After this,Open VNC Viewer,Enter address as 'localhost:5901'(Here 1 in 5901 is your session number) and connect 

![screenshot_vnc viewer_20181024-092044 2](https://user-images.githubusercontent.com/32305505/47405269-6ecb6d00-d76e-11e8-8a5e-1ac3d54bbfef.png)



#### If you have any query,send an email at thetrickboy007@gmail.com
