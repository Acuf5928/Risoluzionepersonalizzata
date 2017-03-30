#! /usr/bin/python

uno = 'xrandr --addmode HDMI-0 1440x900_60.00\n'
due = 'xrandr --newmode "1440x900_60.00"  106.50  1440 1528 1672 1904  900 903 909 934 -hsync +vsync\n'
tre = 'xrandr --output HDMI-0 --mode 1440x900_60.00\n'
quattro='        source_with_error_check "$file"\n'
cinque='    fi\n'
sei='done\n'

controllo = 0
i = 0

files = open('/usr/sbin/lightdm-session', 'r+')
lines = files.readlines()
files.close()
files = open('/usr/sbin/lightdm-session', 'r+')

while i < len(lines):
    if lines[i] == uno or lines[i] == due or lines[i] == tre:
        controllo = controllo + 1
    i = i + 1

if controllo != 0:
    print "Impossibile continuare, risoluzione gia' impostata."

else:
    i = 0
    while i < len(lines): 
        if lines[i] == quattro and lines[i+1] == cinque and lines[i+2] == sei:
            controllo = i+3
        i = i + 1
            
    i = len(lines)
    lines.extend(['','','','','','','','','',''])
    
    print controllo

    while i > controllo:
        lines[i+4] = lines[i]
        i = i - 1

    lines[controllo] = '\n'
    lines[controllo+1] = uno
    lines[controllo+2] = due
    lines[controllo+3] = tre
    lines[controllo+4] = '\n'

    files.writelines(lines)	
files.close()
