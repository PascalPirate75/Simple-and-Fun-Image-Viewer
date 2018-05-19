# Simple-and-Fun-Image-Viewer
I wanted a simple image viewer that I could use to cull useless images.  So I made this.  For now it probably only works on Linux.  Must be ran from the terminal.  When it is run it creates a junk folder in the current directory and any files not wanted are moved there.  The image move is triggered by hitting the "z" key and happens without confirmation, it was done this way for speed, hence the move to the junk folder instead of outright delete.  Move to the next image by hitting [SpaceBar], and q exits script.  Click gear in upper left or hit "h" for helpful hints.


There is curently 3 files:

saf_view.py                 = The actual python script.

saf_view_splash.png         = The first image.

saf_view                    = The bash script that runs starts the script



I placed all three files in the "/usr/local/bin/"

In the future:

Hope to add, "undo move", and prev image controls, and tweek for execution on the other OS some people still use :)



http://pascalpiratescove.com


