import glob
import shutil

holmesFileNames = list()

for filename in glob.glob("trim_Holmes_Training_Data/*.TXT"):
    txtFile = open(filename)

    for line in txtFile:
        if "Sherlock Holmes" in line:
            holmesFileNames.append(filename)
            break

    txtFile.close()

for filename in holmesFileNames:
    shutil.copyfile(filename, "only_" + filename[5:])