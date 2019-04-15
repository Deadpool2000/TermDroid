# TermDroid (v2.0)
GUI Installer for various OS running on Termux

![Screenshot at 2019-04-15 22-02-38](https://user-images.githubusercontent.com/32305505/56149678-b7037380-5fca-11e9-8282-9ce21c3ca9e0.png)

## What's new?
- Added support for Parrot OS 
- Various improvements and bugs fixed

## Installation
1) First run your respective os on termux
2) git clone https://github.com/Deadpool2000/TermDroid.git
3) chmod +x install.py
4) python3 install.py

## Note: Use Python 3.x or upper version

## How to use

#### 1) LXDE Desktop Environment 
DISPLAY=:<session_number> startlxde &

e.g. DISPLAY=:1 startlxde &

#### 2) XFCE4 Desktop Environment 
DISPLAY=:<session_number> startxfce4 &

e.g. DISPLAY=:1 startxfce4 &

#### 3) MATE Desktop Environment 
DISPLAY=:<session_number> mate-session &

e.g. DISPLAY=:1 mate-session &

#### After this,Open VNC Viewer,Enter address as 'localhost:5901'(Here 1 in 5901 is your session number) and connect 

![screenshot_vnc viewer_20181024-092044 2](https://user-images.githubusercontent.com/32305505/47405269-6ecb6d00-d76e-11e8-8a5e-1ac3d54bbfef.png)



#### If you have any query,send an email at thetrickboy007@gmail.com
