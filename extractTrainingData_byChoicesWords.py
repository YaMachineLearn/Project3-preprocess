import re

RAW_TEST_FILE = "testing_data.txt"
TRAIN_FILE = "training_v5_noTag.txt"
OUT_FILE = "training_v5_noTag_choice_removeWordsWithMarks.txt"

def main():
    choicesWordSet = parseChoices(RAW_TEST_FILE)
    print "keyword count: ", len(choicesWordSet)

    extractSentences(TRAIN_FILE, OUT_FILE, choicesWordSet)

def parseChoices(RAW_TEST_FILE):
    #RAW_TEST_FILE should be "testing_data.txt"

    choicesWordSet = set()

    pattern1 = "(.+\[)([^\]]+)"  #get anything inside [ ]
    #pattern2 = "(\w)[(^\w)]?[(\w)]?"   #split with any symbols
    with open(RAW_TEST_FILE) as testFile:
        for line in testFile:
            # strippedLine = line.rstrip()
            # if strippedLine:   #not empty after strip
            m1 = re.match(pattern1, line)
            choice = m1.group(2)
            #choicesWordSet.add(choice)

            choice = choice.lower()
            # choice = choice.replace("n't", " not")
            # choice = choice.replace("-", " ")
            # choice = choice.replace("'", " ")
            if "-" in choice:
                continue
            if "'" in choice:
                continue
            if "," in choice:   #remove numbers
                continue
            # words = choice.split()
            # for word in words:
            choicesWordSet.add(choice)

    return choicesWordSet

def extractSentences(TRAIN_FILE, OUT_FILE, keywordSet):
    #if a sentence contains any word in keywordSet, extract it
    trainFile = open(TRAIN_FILE)
    outFile = open(OUT_FILE, 'w')

    extractSentenceCounter = 0
    for line in trainFile:
        for word in line.split():
            if word in keywordSet:
                extractSentenceCounter += 1
                outFile.write(line)
                break
    print "extract sentence count: ", extractSentenceCounter

    trainFile.close()
    outFile.close()


if __name__ == '__main__':
    main()