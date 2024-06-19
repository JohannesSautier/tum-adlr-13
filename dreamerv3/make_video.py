from PIL import Image
import subprocess


#Make a Video of the frames that are stored logir_new_model/frames adn have the name with a upcounting number frame-1.png, frame-2.png, frame-3.png, ...
subprocess.call(['ffmpeg', '-framerate', '2', '-i', 'logir_new_model/frames/frame-%d.png', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', 'logir_new_model/frames/video.mp4'])