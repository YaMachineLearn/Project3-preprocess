import re

CORRECT_ANSWER_FILE = "correctAnswer.csv"
SUBMIT_ANSWER_FILE = "result.csv"

def main():
    correctAnswerIndices = parseAnswerFromCsv(CORRECT_ANSWER_FILE)
    submitAnswerIndices = parseAnswerFromCsv(SUBMIT_ANSWER_FILE)

    correctNum = 0
    for i in xrange(len(correctAnswerIndices)):
        if correctAnswerIndices[i] == submitAnswerIndices[i]:
            correctNum += 1
    accuracy = float(correctNum) / len(correctAnswerIndices)

    print "accuracy: ", accuracy

def parseAnswerFromCsv(csvFileName):
    answerIndices = list()

    pattern = "(\d+)(,)(\w)"
    with open(csvFileName) as csvFile:
        next(csvFile)
        for line in csvFile:
            strippedLine = line.rstrip()
            if strippedLine:   #not empty after strip
                m = re.match(pattern, line)
                answerChr = m.group(3)
                answerIdx = ord(answerChr) - 97
                answerIndices.append(answerIdx)
    return answerIndices

if __name__ == '__main__':
    main()
