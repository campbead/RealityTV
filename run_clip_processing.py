# load packages

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip
import os
import argparse

# set variables

working_directory = '/home/adam/Projects/Reality_TV/data'
file_list = 'singlefile.txt'
server_location_file = 'serverlocation.txt'
clip_time = 300

ap = argparse.ArgumentParser()
ap.add_argument("--work_dir", required=True,
    help="working directory")
ap.add_argument("--file_list", required=True,
    help="text file with path locations for files")
ap.add_argument("--clip_time", required=True,
    help="time in seconds of clip")
ap.add_argument("--server", required=True,
    help="server location file")

args = vars(ap.parse_args())
working_directory = args["work_dir"]
file_list = args["file_list"]
clip_time = args["clip_time"]
server_location_file = args["server"]
clip_time = int(float(clip_time))

def process_video(video_file, working_directory, clip_time, server_name):
    file_name = video_file
    single_quote = "'"
    double_quote = '"'

    command = "scp -T " + server_name + ":" + double_quote +single_quote + file_name + single_quote + double_quote + " " + working_directory 
    os.system(command)

    # do the clip
    input_video = file_name.split('/')[-1]
    output_video = ".".join(input_video.split('.')[:-2]) + '_clip.mp4'
    clip = VideoFileClip(working_directory +'/'+ input_video)

    ffmpeg_extract_subclip(working_directory + '/'+ input_video, clip.duration - clip_time, (clip.duration ), targetname=working_directory +'/'+ output_video)

    # delete main video
    os.system('rm ' + working_directory + '/'+ input_video)

    # run scene detect
    output_dir = ".".join(output_video.split('.')[:-2]) 

    command = "scenedetect --input " + working_directory +'/'+ output_video +" --output " + working_directory +"/" + output_dir + " detect-content save-images list-scenes"
    os.system(command)


# run main program

# get the server name
f = open(working_directory + '/'+server_location_file, "r")
server_name = f.readline()
f.close()
server_name = server_name.split('\n')[0]


# run loop
file_list = 'filelist.txt'
files = []
f = open(working_directory + '/'+file_list, "r")
for line in f:
  file = line.split('\n')[0]
  files.append(file)
  
for file in files:
    process_video(file, working_directory, clip_time, server_name)
