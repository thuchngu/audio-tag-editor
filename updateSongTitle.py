import taglib
import argparse
import os

# Parse command line args
parser = argparse.ArgumentParser()
parser.add_argument("-h", "--help", dest = "help", default = "", help="Print Usage Information")
parser.add_argument("-s", "--source", dest = "source", default = "/", help="Source File Path")
parser.add_argument("-d", "--dest", dest = "dest", default = "/", help="Destination File Path")
parser.add_argument("-v", "--verbose", dest = "verbose", default = "", help="Verbose Output")
args = parser.parse_args()

# Get source path to music from arguments
#pathToMusic = input("Path to Music Files: ") # path in linux format in WSL terminal if on windows (ex. /mnt/c/Users/Thuc/Music/New/test)
pathToMusic = args.source

# Print files under source path
dirScan = os.scandir(pathToMusic)
print("Files under ", pathToMusic, ": ")

# Update names of songs under source path
for musicFile in dirScan:
    if musicFile.is_file():
        print(musicFile.name)
        song = taglib.File(musicFile)
        songTags = song.tags

        # TODO: turn into an option at runtime instead of just commenting it in and out when I need it
        #songTitle = musicFile.name
        #print("Current song title: ", songTags['TITLE'], " and artist: ", songTags['ARTIST'])
        #songTags['TITLE'] = [musicFile.name[3:].replace(".wav", "")]
        #song.save()
        #print("New song TITLE: ", songTags['TITLE'], " and artist: ", songTags['ARTIST'])

        # TODO: turn into an option at runtime instead of just commenting it in and out when I need it
        if len(songTags) > 0:
            max_key_len = max(len(key) for key in songTags.keys())
            for key, values in songTags.items():
                for value in values:
                    print(f"  {key.ljust(max_key_len)} = {value}")
            