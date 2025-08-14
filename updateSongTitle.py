import taglib
import argparse
import os

# Parse command line args
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--source", dest = "source", required=True, default = "/", help="Source File Path")
parser.add_argument("-a", "--artist", dest = "artist", required=True, default = "none", help="Artist Name")
parser.add_argument("-v", "--verbose", action='store_true', help="Verbose Output")
parser.add_argument("-u", "--update", action='store_true', help="Update the tags in source")
args = parser.parse_args()

# Get source path to music from arguments
#pathToMusic = input("Path to Music Files: ") # path in linux format in WSL terminal if on windows (ex. /mnt/c/Users/Thuc/Music/New/test)
pathToMusic = args.source
songArtist = args.artist
showVerbose = args.verbose
doUpdate = args.update

# Print files under source path
dirScan = os.scandir(pathToMusic)
print("Files under ", pathToMusic, ": ")

# TODO Read in a text file with metadata to use to update like Album Name
# TODO OR include as command line arguments

# Update names of songs under source path
for musicFile in dirScan:
    if musicFile.is_file():
        print(musicFile.name)
        song = taglib.File(musicFile)
        songTags = song.tags

        # TODO Add Album update here as well
        if doUpdate:
            songTitle = musicFile.name
            print("Updating song title: ", songTags['TITLE'], " and artist: ", songTags['ARTIST'], " to ", songTitle, " and ", songArtist)
            if musicFile.name.find(".wav"):
                songTags['TITLE'] = [musicFile.name[3:].replace(".wav", "")]
            elif musicFile.name.find(".mp3"):
                songTags['TITLE'] = [musicFile.name[3:].replace(".mp3", "")]
            else:
                print("File is not a valid audio file")
            songTags['ARTIST'] = songArtist
            song.save()

        if showVerbose:
            if len(songTags) > 0:
                max_key_len = max(len(key) for key in songTags.keys())
                for key, values in songTags.items():
                    for value in values:
                        print(f"  {key.ljust(max_key_len)} = {value}")
            