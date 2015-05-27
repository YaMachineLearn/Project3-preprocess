#parse the answers from Holmes.machine_format.answers.txt
#output in character/index/csv formats

import re

ANSWER_FILE = "Holmes.machine_format.answers.txt"
OUT_FILE_1 = "correctAnswer_chr.txt"
OUT_FILE_2 = "correctAnswer_idx.txt"
OUT_FILE_3 = "correctAnswer.csv"

answersChr = list()
answersIdx = list()

pattern = "(\d+)(\w)"

with open(ANSWER_FILE) as answerFile:
    for line in answerFile:
        m = re.match(pattern, line)
        answersChr.append(m.group(2))
        answersIdx.append( ord(m.group(2)) - 97 )

with open(OUT_FILE_1, 'w') as out1:
    for answer in answersChr:
        out1.write(answer + '\n')

with open(OUT_FILE_2, 'w') as out2:
    for answer in answersIdx:
        out2.write(str(answer) + '\n')

with open(OUT_FILE_3, 'w') as outputFile:
    outputFile.write('Id,Answer\n')
    for i in xrange(1040):
        outputFile.write(str(i + 1) + ',' + answersChr[i] + '\n' )

