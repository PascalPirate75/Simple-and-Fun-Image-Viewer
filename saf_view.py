import os
from tkinter import filedialog
from tkinter import *

from PIL import Image, ImageTk

import sys
# if sys.stdin.isatty():
#     # running interactively
#     print ("running interactively")



fTypes = [".jpg", ".jpeg", ".png", ".gif"]  #".jpg", ".jpeg", ".png", ".gif"
img = []
cf = ""

# if sys.stdin.isatty():

cwd = os.getcwd()

# make new junk dir at       cwd + "/junk/"

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

# loadDir(filedialog.askdirectory())




def nextPic(fn):


	image = Image.open((cwd + "/" + fn))

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

def newPhoto(event):
	global cf
	global img
	global cwd

	if event.char == 'z':
		print(cwd + "/" + cf, " moved to " + cwd + "/junk/" + cf)
		os.rename(cwd + "/" + cf, cwd + "/junk/" + cf)
		try:		
			fn = img.pop()
		except: 
			print("End of images terminating script...")
			cwd = filedialog.askdirectory()
			loadDir()
			# exit()

		cf = fn
		nextPic(fn)

	elif event.char == 'q':
		print("Quit!")
		root.destroy()

	elif event.char == ' ':
		try:
			fn = img.pop()
			cf = fn
			print("Next! " + cwd + "/" + fn)
			nextPic(fn)

		except: 
			print("End of images terminating script...")
			# exit()
			cwd = filedialog.askdirectory()
			loadDir()



	elif event.char == "d":
		cwd = filedialog.askdirectory()
		loadDir()


root = Tk()
# get screen width and height
ws = root.winfo_screenwidth()-100 # width of the screen

hs = root.winfo_screenheight()-100 # height of the screen
root.title("PPC's SAF Image Viewer!")
root.geometry('%dx%d+20+20' % (ws, hs))

instructions = Label(root, text="[SPACEBAR] = next picture.  -   [Z] = move picture to junk folder.  -   [D] = load new folder  -   [Q] = quit.   By The Pascal Pirate.", bg="blue", fg="white")
instructions.pack()

cf = img.pop()
photo = PhotoImage(file=cf)

label = Label(root, image=photo)
label.pack()

ent = Entry(root)
ent.bind_all('<Key>', newPhoto)
ent.focus_set()


root.mainloop()


