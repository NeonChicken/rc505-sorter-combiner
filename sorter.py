# Sorts new tracks

import os
import shutil
import json

def run(folder_name):
    dir = folder_name

    memory_dir = dir + "/DATA/MEMORY.RC0"
    with open(memory_dir) as f:
        file = f.readlines()

    tracks = []
    track = {
        "id": 0,
        "name": [],
        "volume": [],
        "data": []
    }
    data = []
    volume = []
    name = []
    count = 0
    in_track = False
    in_name = False
    for line in file:
        if "<mem id=" in line:
            in_track = True
        if "</mem>" in line:
            track["data"] = data
            full_name = ""
            for c in name:
                full_name += c
            track["name"] = full_name.rstrip()
            track["id"] = count
            track["volume"] = volume
            count += 1
            tracks.append(track)
            name = []
            data = []
            volume = []
            track = {"id": 0, "name": [], "volume": [], "data": []}
            in_track = False
        if in_track:
            data.append(line)

        if "<NAME>" in line:
            in_name = True
        if "</NAME>" in line:
            in_name = False
        if "<PlyLvl>" in line:
            volume_str = line[9:]
            volume_int = volume_str[:volume_str.find('<')]
            volume.append(volume_int)
        if in_name:
            if "<C" in line:
                trim_left = line[6:]
                trim_right_idx = trim_left.find("<")
                char = int(trim_left[:trim_right_idx])
                name.append(chr(char))

    print("Data has been read.")
    print("Copying files...")

    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    ROOT_DIR += "\\" + dir

    dir_list = os.listdir(ROOT_DIR + "\\WAVE")
    for track in tracks:
        dir_name = str(track["id"]) + ". "
        dir_name += track["name"]
        track_dir = ROOT_DIR + "\\SORTED\\" + dir_name
        try:
            os.mkdir(track_dir)
        except FileNotFoundError:
            # If sorted directory does not yet exist
            os.mkdir(ROOT_DIR + "\\SORTED\\")
            try:
                os.mkdir(track_dir)
            except FileExistsError:
                pass
        except FileExistsError:
            pass

        for dir in dir_list:
            track_id = track["id"] + 1
            if str(track_id) in dir[:3]:
                # Found folder 001 in list
                for t_dir in dir_list:
                    if dir[:3] in t_dir:
                        # For every 001 folder in list (001_1-001_5 < t_dir)
                        wav_path = ROOT_DIR + "\\WAVE\\" + t_dir + f"\\{t_dir}.WAV"
                        if os.path.isfile(wav_path):
                            # Copy file to track_dir
                            shutil.copy2(wav_path, track_dir)
                # All 5 wav files have been copied
                # Make a text file with data (volume info etc.)
                with open(track_dir + f"\\{dir[:3]}.json", 'w') as j:
                    json.dump(track, j, indent=4)
                break

    print("Success!")