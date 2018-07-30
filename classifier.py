import os
import shutil

rootPath = "/Users/garyhsu/workspace/dataset/AgeClassifier/"

sourcePath = "/Users/garyhsu/workspace/dataset/UTKFace/"

prefix = "age"

os.mkdir(rootPath, 0755)

for file in os.listdir(sourcePath):
    if not os.path.exists(rootPath + prefix + file.split('_').pop(0)):
        os.mkdir(rootPath + prefix + file.split('_').pop(0), 0755)
    shutil.copy2(sourcePath+file, rootPath + prefix + file.split('_').pop(0)+"/"+file)



