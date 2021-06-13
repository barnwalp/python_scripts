import os
import subprocess


if os.getcwd() == 'C:\\Users\\panka\\github_repo':
    # check if the list items are subdirectory
    folders = [x for x in os.scandir() if x.is_dir()]
    for folder in folders:
        os.chdir(folder)
        print(os.getcwd())
        # subprocess.run('git fetch --all', shell=True)
        # subprocess.run('git reset --hard origin/master', shell=True)
        subprocess.run('git pull', shell=True)
        os.chdir('..')
