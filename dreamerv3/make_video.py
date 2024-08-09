import subprocess
import datetime

# Generate a timestamp string
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Modify the output video filename to include the timestamp
output_video_path = f'log_videos/video_{timestamp}.mp4'

subprocess.call([
    'ffmpeg',
    '-framerate', '30',
    '-i', 'logdir/frames/frame-%d.png',
    '-vsync', 'vfr',  
    '-c:v', 'libx264',
    '-pix_fmt', 'yuv420p',
    output_video_path
])