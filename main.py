import sorter, dupe_finder, audio_combiner, archive, os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR_LIST = os.listdir(ROOT_DIR)

# Make Archive folder
if "~Archive" not in ROOT_DIR_LIST:
    os.mkdir(f"{ROOT_DIR}\\~Archive")
if "Projects" not in ROOT_DIR_LIST:
    os.mkdir(f"{ROOT_DIR}\\Projects")


# Find the target directory [the ROLAND folder as YYYY-MM-DD]
target_dir = ""
for folder in ROOT_DIR_LIST:
    if os.path.isdir(f"{ROOT_DIR}\\{folder}"):
        if folder[0].isdigit() and folder[1].isdigit():
            target_dir = folder

if target_dir:
    print("Running script")
    sorter.run(target_dir)
    dupe_finder.run(target_dir)
    audio_combiner.run()
    archive.run()
else:
    print("No folder found that start with two digits -> YYYY-MM-DD")

