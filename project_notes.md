# Predicting winners and losers of reality shows
Python based data science project by Adam Campbell

## Summary
Can we predict who the winner or loser of the show is from the quick cuts ahead of the announcement of the winner or loser?  I'm going to collect data from a few reality shows, at this point I'm thinking Great British Bake off, Great British Sewing bee, Making it and Worst Cooks in America.  I'm going to look at the number and order of cuts in the pre-reveal scenes, and the timing of the cuts.  The idea is that this could answer some basic questions I have when watching reality shows.  <i> is it always the first persion they show? is it the person who they linger on the longest? </i> This dataset can be used to explore those simple relations and as a jumping off point for more machine-learing predictions. 

## Data table schema
### metadata
Column - TV show

Column - Season number 

Column - Episode number

### independent data
Column 1 - Cut number where first shown.

Column 2 - Total number of cuts for individual contestent

Column 3 - Total number of cuts for all contestent

Column 4 - Total time shown for individual contestent

Column 5 - Total time of cuts for all contestent

Column 6 - Total number of contestents previewed

### labels data
Column - Were they the winner/loser

Column - Was there a winner/loser

## Step 1 - Get data

So first thing I'll need to do is get the data.  I'm going to assume the clips are in the last five minutes of the show.  So I'll clip out the last five minutes of each episosde.  This is mostly to improve processing times.  I'll use a tool called [pyscenedetect](https://pyscenedetect.readthedocs.io/en/latest/) to cut the video into individual shots with associcated times for each shot.  It's a really nifty tool and exactly what I needed for this project.  To determine the rest of the data I'll watch the clips and code in the data myself.  

I found a useful command for getting data I need

`find "$PWD" -name *.mp4`

I'm saving this info in `filelist.txt`

Now the question I have is if I can process the .mkv files.  If so, I'll need to figure out how to convert them to .mp4 format.

`scp $host_moviebox:"'filepath'" ~/Downloads`

Ok so I ran the command:

`scenedetect --input making.it.s01e01.web.x264-tbs.mkv detect-content list-scenes`

And it worked.  Therefore `.mkv` are okay to use with this tool.  I need to confirm that the clipping tool works.

Ok so I tested that and that works as well.


## Current to-do list:
- finish the filelist.txt
- figure out to run scenedetect natively OR if you have to call it.  (does this affect performance?)
- write a script to download the file, clip it, run the analsysis, and deleted the data files.

## Update 8 Jan 2020
I was unable to call the os command from python I think there are some work-arounds but it might be best to simply write a shell script that download and processes the data. 

 
