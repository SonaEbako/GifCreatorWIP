"""
Slide Show - Make an application that shows various pictures in a slide show format.
Optional: Try adding various effects like fade in/out, star wipe and window blinds transitions.
"""

import imageio
import tkinter

file1, file2 = askopenfilename()

filenames = [file1,file2]
images = []
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('Image-Slideshow/movie.gif', images,'GIF',duration=1)