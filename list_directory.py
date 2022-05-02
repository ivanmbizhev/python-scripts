import os
import fnmatch

def dir_list():
    print("Please write down the directory you wish to view:")
    d = input()
    files = os.listdir(d)
    for f in files:
        if fnmatch.fnmatch(f, 'passwd'):
            
            with open(fnmatch) as e:
                lines = e.readlines() 
                for a in lines:
                    print(a)
                

dir_list()
