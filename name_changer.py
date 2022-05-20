# This script will change the name of all preview/output files

import os

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
            old_name = final_dir + "\\" + file
            new_name = final_dir + "\\" + f"Preview-{dir}.wav"
            print(old_name)
            # os.rename(old_name, new_name)