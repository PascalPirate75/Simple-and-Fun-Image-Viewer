import os
from tkinter import messagebox
from tkinter import filedialog
from tkinter import *

from PIL import Image, ImageTk

import sys

fTypes = [".jpg", ".jpeg", ".png", ".gif"]  #".jpg", ".jpeg", ".png", ".gif"
img = []
cf = ""

cwd = os.getcwd()

if (not os.path.exists(os.getcwd()+"/junk")):
	try:
		print("Attempting to creat dir [" + (cwd + "/junk/") + "]")
		os.mkdir((cwd + "/junk/"))
	except OSError as err:
		print("OS error: {0}!  Exiting Can't Continue!".format(err))
		exit()



def loadDir():

	global img
	global cwd
	img = []
	for fT in fTypes:
		for file in os.listdir(cwd + "/"):
			if file.endswith(fT):
				img.append(file)


loadDir()

def nextPic(fn):

	imname = (cwd + "/" + fn)
	image = Image.open(imname)

	root.title("PPC's SAF Image Viewer! - " + imname)

	wh = root.winfo_height()-30

	if (image.size[1] < wh):
		baseheight = image.size[1]
	else:
		baseheight = wh

	
#  this is the resizeing stuff 
	hpercent = (baseheight / float(image.size[1]))
	wsize = int((float(image.size[0]) * float(hpercent)))
	image = image.resize((wsize, baseheight), Image.ANTIALIAS)
#
	photo = ImageTk.PhotoImage(image)
	label.configure(image = photo)

	label.image = photo 

def showHelp(self):
	messagebox.showinfo('Help', "[SPACEBAR] = next picture\n[Z] = move picture to junk folder\n[D] = load new folder\n[H] = This help\n[Q] = quit\n\nBy The Pascal Pirate."
)

def handelKeys(event):
	global cf
	global img
	global cwd

	if event.char == 'z':
		print(cwd + "/" + cf, " moved to " + cwd + "/junk/" + cf)
		os.rename(cwd + "/" + cf, cwd + "/junk/" + cf)
		try:		
			fn = img.pop()
		except: 
			print("End of images asking for new directory...")
			tmp = filedialog.askdirectory()
			if tmp:
				cwd = tmp
				loadDir()

		cf = fn
		nextPic(fn)

	elif event.char == 'q':
		print("Quit!")
		root.destroy()

	elif event.char == '?' or event.char == "h":
		showHelp(False)

	elif event.char == ' ':
		try:
			fn = img.pop()
			cf = fn
			print("Next! " + cwd + "/" + fn)
			nextPic(fn)

		except: 
			print("End of images asking for new directory...")
			tmp = filedialog.askdirectory()
			if tmp:
				cwd = tmp
				loadDir()

	elif event.char == "d":
		tmp = filedialog.askdirectory()
		if tmp:
			cwd = tmp
			loadDir()


root = Tk()
# get screen width and height
ws = root.winfo_screenwidth()-380 # width of the screen

hs = root.winfo_screenheight()-300 # height of the screen

root.title("PPC's SAF Image Viewer!")
root.geometry('%dx%d+170+120' % (ws, hs))

photo = PhotoImage(file="/usr/local/bin/saf_view_splash.png")

if not photo:
	cf = img.pop()
	photo = PhotoImage(file=cf)

label = Label(root, image=photo)
label.pack()

ent = Entry(root)
ent.bind_all('<Key>', handelKeys)
ent.focus_set()

wl = ws-20
instructions = Label(root, text=u"\u2699", fg="grey", wraplength=ws)
instructions.config(font=("Times", 16))
instructions.place(x=1, y=1)
instructions.bind("<Button-1>", showHelp)

showHelp(False)

root.mainloop()


