# This script removes all preview files from projects that have less than 5 loops

import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
proj_list = os.listdir(ROOT_DIR + "\\Projects")
for dir in proj_list:
    final_dir = ROOT_DIR + "\\Projects" + "\\" + dir

    dir_list = os.listdir(final_dir)

    # Check if folder already has exported loop.wav
    count = 0
    for file in dir_list:
        if ".json" not in file and "Preview" not in file:
            count += 1
    if count != 5:
        print(f"{dir} preview is deleted")
        for file in dir_list:
            if "Preview" in file:
                os.remove(final_dir + "\\" + file)

    # uncomment if you wish to remove all preview files
    # for file in dir_list:
    #     if "Preview" in file:
    #         os.remove(final_dir + "\\" + file)
