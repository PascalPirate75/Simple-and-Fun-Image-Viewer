import os
from tkinter import *

from PIL import Image, ImageTk

pastSplash = False

fTypes = [".jpg", ".jpeg", ".png", ".gif"]  #".jpg", ".jpeg", ".png", ".gif"
img = []
cf = ""
cwd = os.getcwd()  # make new junk dir at       cwd + "/junk/"

if (not os.path.exists(os.getcwd()+"/junk")):
	try:
		print("Attempting to creat dir [" + (cwd + "/junk/") + "]")
		os.mkdir((cwd + "/junk/"))
	except OSError as err:
		print("OS error: {0}!  Exiting Can't Continue!".format(err))
		exit()


for fT in fTypes:
	for file in os.listdir(cwd + "/"):
		if file.endswith(fT):
			img.append(file)



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
	global pastSplash

	if event.char == 'z':
		if (not pastSplash):
			return False
		print(cwd + "/" + cf, " moved to " + cwd + "/junk/" + cf)
		os.rename(cwd + "/" + cf, cwd + "/junk/" + cf)
		try:		
			fn = img.pop()
		except: 
			print("End of images terminating script...")
			exit()
		cf = fn
		nextPic(fn)

	elif event.char == 'q':
		print("Quit!")
		root.destroy()

	elif event.char == ' ':
		pastSplash = True
		try:
			fn = img.pop()
		except: 
			print("End of images terminating script...")
			exit()
		cf = fn
		print("Next! " + cwd + "/" + fn)
		nextPic(fn)

root = Tk()

# get screen width and height
ws = root.winfo_screenwidth()-100 # width of the screen
hs = root.winfo_screenheight()-100 # height of the screen
root.title("PPC's SAF Image Viewer!")
root.geometry('%dx%d+20+20' % (ws, hs))

instructions = Label(root, text="[SPACEBAR] = next picture.  -   [Z] = move picture to junk folder.  -   [Q] = quit.   By The Pascal Pirate", bg="blue", fg="white")
instructions.pack()

#cf = img.pop()
photo = PhotoImage(file="/usr/local/bin/saf_view_splash.png")

label = Label(root, image=photo)
label.pack()

ent = Entry(root)
ent.bind_all('<Key>', newPhoto)
ent.focus_set()

root.mainloop()


