import glob

for filename in glob.glob("Holmes_Training_Data/*.TXT"):
    trimmedFile_Name = "trim_" + filename
    trimmedFile = open(trimmedFile_Name, 'w')
    oriFile = open(filename)

    isHeader = True
    lines = oriFile.readlines()
    lineLen = len(lines)

    start = 0
    end = lineLen
    while start < lineLen:
        if lines[start][0:5] == "*END*":
            break
        start += 1
    start += 1

    for i in xrange(start, end):
        trimmedFile.write(lines[i])
    
    trimmedFile.close()
    oriFile.close()