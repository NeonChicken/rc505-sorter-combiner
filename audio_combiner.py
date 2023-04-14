# This script will check in the Projects folder if there are any new projects that do not have a Preview file yet
# It will then combine the loops into a new audio file

import os
import ffmpeg
import json
from pydub import AudioSegment
from pydub.playback import play

def run():
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    proj_list = os.listdir(ROOT_DIR + "\\Projects")
    for dir in proj_list:
        output_file_exists = False

        print(f"Checking {dir}", end="\n\n")

        final_dir = ROOT_DIR + "\\Projects" + "\\" + dir

        dir_list = os.listdir(final_dir)

        # Check if folder already has exported loop.wav
        for file in dir_list:
            if "Preview" in file:
                output_file_exists = True
        if output_file_exists:
            continue

        # Append tracks
        # Add empty tracks for missing loops (from 5 total loops)
        audio_files = []
        bools = [False for i in range(5)]
        for file in dir_list:
            if ".json" not in file:
                segment = AudioSegment.from_file(final_dir + "\\" + file, format="wav")
                bools[int(file[4]) - 1] = True
                audio_files.append(segment)
        for idx, bool in enumerate(bools):
            if bool == False:
                segment = AudioSegment.empty()
                audio_files.insert(idx, segment)

        print("Audio files appended.", end="\n\n")

        print("Checking which loop is the longest...")

        # Check longest loop
        longest = 0
        longest_idx = 0
        duration = 0
        for idx, audio in enumerate(audio_files):
            duration = audio.duration_seconds
            if duration > longest:
                longest = duration
                longest_idx = idx

        print(f"Loop idx {longest_idx} is longest with {round(longest, ndigits=2)} seconds", end="\n\n")


        # todo # Git, Drie Ton have single-play mods (<PlyMod>)
        # todo # Output different audio files for every single-play mod as trackName-v1, trackName-v2 etc.
        # Getting volumes from json
        volumes = []
        json_file = ""
        for file in dir_list:
            if ".json" in file:
                json_file = file
        with open(final_dir + f"\\{json_file}") as f:
            the_json = json.load(f)
            volumes = the_json["volume"]
        # Getting decibels
        dbs = []
        for volume in volumes:
            # Transform 0<>100 vol to -10<>10 db
            db = int(volume) * 0.2 - 10
            dbs.append(round(db, ndigits=2))

        sound = audio_files[longest_idx]
        # Adjust volume in decibel
        overlay = sound + dbs[longest_idx]
        for idx, audio in enumerate(audio_files):
            if idx == longest_idx:
                continue
            for file in dir_list:
                try:
                    if idx == int(file[4]) - 1:
                        print(f"Overlaying sound {idx}.")
                        audio = audio + dbs[idx]
                        overlay = overlay.overlay(audio, position=0, loop=True)
                except:
                    pass

        print("Exporting file...", end="\n\n")

        output_dest = final_dir + f"\\Preview-{dir}.wav"
        overlay.export(output_dest, format="wav")

        print("Done!")
