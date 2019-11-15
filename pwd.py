import glob
import os

def cng(fName):
    for path, dirs, files in os.walk('E:\\Google Drive\\Machine Learning\\Scientific'):
        for d in dirs:
            for f in glob.iglob(os.path.join(path, d, '*.py')):
                if fName in f:
                    os.chdir(os.path.join(path, f).replace(fName, ""))
                    #print(os.path.join(path, f).replace(fName, ""))