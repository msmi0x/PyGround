#!/usr/bin/env python
import webbrowser
import time
import os

#wait some time, in seconds
time.sleep(10)

#a list of the stackexchange network websites
stack_network = ['http://stackoverflow.com/',           #stackoverflow                 
                 'http://unix.stackexchange.com/',      #unix,linux                 
                 'http://askubuntu.com/']               #askubuntu

#select chromium to do the job
b = webbrowser.get('chromium-browser')

#loop over each website
for site in stack_network:
	b.open_new_tab(site)    #open website in a new tab
	time.sleep(5)           #wait some time, bw each tab and the next
	
	
#after opening all sites, wait till everything loads fine
time.sleep(10)

#close any instantiation of the chromium browser, this is system-specific and works only on unix-linux
os.system('pkill -15 -f chromium')  
