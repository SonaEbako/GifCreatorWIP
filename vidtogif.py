from tkinter.filedialog import askopenfilename
from moviepy.editor import *
import tkinter
from moviepy.editor import *

video = askopenfilename()
clip = (VideoFileClip(video).subclip((2.25),(6.25))
        .resize(0.3))
clip.write_gif("output.gif")