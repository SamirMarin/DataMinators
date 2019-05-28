import os
import pathlib
basepath = os.path.expanduser('~') + '/esldata'
count = 0 
#for dirpath, dirnames, files in os.walk(basepath):
#    if count <= 2:
#        print(dirpath.rfind('/'))
#        print(dirpath[dirpath.rfind('/')+1:len(dirpath)])
#        print(f'Found directory: {dirpath}')
#        print(dirnames)
#        print(files)
#    #for file_name in files:
#    #    print(file_name)
#    count += 1

def get_map_of_files(path):
    basepath = os.path.expanduser('~/') + path

    for dirpath, dirnames, files in os.walk(basepath):
        current_dirname = get_dir_name(dirpath)
        dirmap = {} 
        dirmap['files'] = files
        dirmap['dir'] = dirnames
        return dirmap
        


def get_dir_name(dirpath):
    return print(dirpath[dirpath.rfind('/')+1:len(dirpath)])

print(get_map_of_files(basepath))
