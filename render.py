import os
from os import listdir
from os.path import isfile, join
import subprocess
cwd = str(os.getcwd())
os.chdir(cwd + '/BLEND files')
onlyfiles = [f for f in listdir(os.curdir) if isfile(join(os.curdir, f))]

print(onlyfiles)

b = 0


Bpath = '"C:/Program Files/Blender Foundation/Blender 3.0/blender.exe"'

for i in onlyfiles:
    args = " -b " + (str(os.curdir).replace('.', '') + i) + " -o //outputs/" + str(i).replace(".blend", "") + "-## -F PNG -x 1 -f 2 -- --cycles-device CUDA"
    cmd = Bpath + args
    subprocess.call(cmd, shell=True)
    print("rendered file" + i)