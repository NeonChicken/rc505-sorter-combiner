# This script will seek out new rc-505 projects from the to_copy folder
# that do not yet exist in the Projects folder, and put them in there

import os
from distutils.dir_util import copy_tree

to_copy = "2022-5-5"

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

try:
    os.mkdir(ROOT_DIR + "\\" + "Projects")
except FileExistsError:
    pass

project_dir = ROOT_DIR + "\\" + "Projects"
copy_dir = ROOT_DIR + "\\" + to_copy + "\\SORTED"

print("Copying files...")

dir_list = os.listdir(copy_dir)
project_list = os.listdir(project_dir)
for dir in dir_list:
    dot_loc = dir.find(".")
    # proj_name is after the index, dot and space -->  0. PROJ_NAME
    proj_name = dir[dot_loc + 2:]
    if proj_name != "A" and proj_name != "INIT MEMORY":
        if proj_name not in project_list:
            os.mkdir(project_dir + "\\" + proj_name)
            copy_tree(copy_dir + "\\" + dir, project_dir + "\\" + proj_name)

print("Success!")

# If already in projects, do not copy
# Remove ID
