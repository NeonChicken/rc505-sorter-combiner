# Keep file- and folder names, but remove .wav to save space
# The .wav files have been copied to the Projects folder anyways

import os


def run():
    ARCHIVE_DIR = os.path.dirname(os.path.abspath(__file__)) + "\\~Archive"
    ARCHIVE_LIST = os.listdir(ARCHIVE_DIR)
    for dir in ARCHIVE_LIST:
        print(f"\nChecking {dir}", end="\n\n")

        date_dir = ARCHIVE_DIR + "\\" + dir

        dir_list = os.listdir(date_dir)

        # Check if folder already has exported loop.wav
        for folder in dir_list:
            date_dir = ARCHIVE_DIR + "\\" + dir

            if folder == "SORTED":
                sorted_dir = date_dir + "\\" + folder
                sorted_dir_list = os.listdir(sorted_dir)

                for song_dir in sorted_dir_list:
                    current_song_dir = sorted_dir + "\\" + song_dir
                    current_song_dir_list = os.listdir(current_song_dir)
                    for file in current_song_dir_list:
                        os.remove(current_song_dir + "\\" + file)

            if folder == "WAVE":
                wave_dir = date_dir + "\\" + folder
                wave_dir_list = os.listdir(wave_dir)
                for wave_folder in wave_dir_list:
                    wave_folder_dir = wave_dir + "\\" + wave_folder
                    wave_folder_list = os.listdir(wave_folder_dir)
                    for wave_file in wave_folder_list:
                        os.remove(wave_folder_dir + "\\" + wave_file)
                    os.rmdir(wave_folder_dir)
                os.rmdir(wave_dir)