TRAIN_FILE = "training_v4_tag.txt"
OUTPUT_FILE = "training_v5_tag.txt"
REMOVE_FILE = "training_v5_tag_remove.txt"

LEN_THRESHOLD = 66

trainFile = open(TRAIN_FILE)
outFile = open(OUTPUT_FILE, 'w')
rmFile = open(REMOVE_FILE, 'w')

for line in trainFile:
    strippedLine = line.rstrip()
    if strippedLine:   #not empty after strip
        lineList = strippedLine.split(' ')
        if len(lineList) > LEN_THRESHOLD:
            rmFile.write(line)
        else:
            outFile.write(line)



