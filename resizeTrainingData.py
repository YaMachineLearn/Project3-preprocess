import random

TRAIN_FILE = "training_v5_noTag.txt"
OUT_FILE_1 = "training_v5_noTag_1_4.txt"
OUT_FILE_2 = "training_v5_noTag_3_4.txt"

trainFile = open(TRAIN_FILE)
outFile1 = open(OUT_FILE_1, 'w')
outFile2 = open(OUT_FILE_2, 'w')

lines = trainFile.readlines()

index = range(len(lines))
random.shuffle(index)

for i in xrange( len(lines)/4 ):
    outFile1.write(lines[index[i]])

for i in xrange(len(lines)/4, len(lines)):
    outFile2.write(lines[index[i]])
