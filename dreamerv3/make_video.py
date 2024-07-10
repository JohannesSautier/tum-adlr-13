from PIL import Image
import subprocess
import datetime

# Generate a timestamp string
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Modify the output video filename to include the timestamp
output_video_path = f'log_videos/video_{timestamp}.mp4'

# Adjusted framerate for slower playback
framerate = '10'  # Adjust this value as needed

subprocess.call([
    'ffmpeg',
    '-framerate', '30',  # This is the input framerate, not the output framerate
    '-i', 'logdir_debug/frames/frame-%d.png',
    '-filter:v', 'select=not(mod(n\,4))',  # Select every 4th frame
    '-r', framerate,  # This sets the output framerate, making the video play slower
    '-vsync', 'vfr',
    '-c:v', 'libx264',
    '-pix_fmt', 'yuv420p',
    output_video_path
])