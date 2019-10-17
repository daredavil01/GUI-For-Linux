#!/usr/bin/env python3
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image 
import subprocess
import os
from os.path import expanduser
from pathlib import Path
from subprocess import Popen
#function run1
def run1():
    subprocess.run(["zenity","--info","--text=\"Welcome to GUI for Linux...\""])
    subprocess.run(["zenity","--notification","--window-icon=info","--text","GUI Initiated Successfully"])

#function run2
def run2(): 
    subprocess.run(["touch","/home/sanket/Desktop/UserRecord.txt"])
    subprocess.run(["tail","-n","5","/etc/passwd",">","/home/sanket/Desktop/UserRecord.txt"])
    #subprocess.run(["zenity","--text-info","--title=\"User Records\"","--filename=/home/danie/Desktop/UserRecord.txt --html"])
def run3():
	subprocess.run(["zenity","--text-info","--filename=/home/sanket/Desktop/UserRecord.txt"]) 
def run4():
	path_to_output_file = '/tmp/myoutput.txt'
	myoutput = open(path_to_output_file,'w')
	p = Popen(["users"], stdout=myoutput, stderr=subprocess.PIPE, universal_newlines=True)
	subprocess.run(["zenity","--text-info","--filename=/tmp/myoutput.txt"])
	#output, errors = p.communicate()
def run5():
	path_to_output_file = '/tmp/myoutput1.txt'
	myoutput = open(path_to_output_file,'w')
	p = Popen(["hostname","-I"], stdout=myoutput, stderr=subprocess.PIPE, universal_newlines=True)
	subprocess.run(["zenity","--text-info","--filename=/tmp/myoutput1.txt"])
	#subprocess.run(["ip","-4","addr","|","grep","-oP","'(?<=inet\s)\d+(\.\d+){3}'"])

#creating application main window
top=Tk()


#adding title
top.title("GUI for Linux")
#menu bar
menubar = Menu(top)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=top.quit)
menubar.add_cascade(label="File", menu=filemenu)

# Creating a photoimage object to use image 
img = ImageTk.PhotoImage(Image.open("icon.png"))
panel = Label(top, image = img )
panel.pack(side = "bottom", fill = "both", expand = "yes" , pady = 10 )  
#top.create_image(20,20, anchor=NW, image=photo)  
button1=Button(top, text="Show Welcome Window", command=run1,fg="red")
button1.pack()
button2=Button(top, text="Backup Users Record", command=run2,fg="black")
button2.pack()
button3=Button(top, text="Show User Records", command=run3,fg="red")
button3.pack()
button5=Button(top, text="Show Username", command=run4,fg="red")
button5.pack()
button6=Button(top, text="Show IP Address", command=run5,fg="red")
button6.pack()
button4=Button(top, text="Close", command=top.quit,fg="red")
button4.pack()
#Entering the main event loop
top.mainloop()

#tail -n 5 /etc/passwd >> /home/sanket/Desktop/UserRecord.txt
