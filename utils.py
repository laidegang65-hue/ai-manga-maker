import os
from moviepy.editor import ImageSequenceClip, AudioFileClip

def make_video(image_folder, output_file, fps=1):
    image_files = sorted([os.path.join(image_folder, img) for img in os.listdir(image_folder) if img.endswith(".png")])
    clip = ImageSequenceClip(image_files, fps=fps)
    clip.write_videofile(output_file, codec='libx264')
