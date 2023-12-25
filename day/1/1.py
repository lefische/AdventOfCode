import re
import os


def word_to_digit(text: str) -> str:
    word_to_num = {
        "one": "1",
        "two": "2",
        "three": "3"
    }
    pattern = re.compile(r"\b(" + "|".join(word_to_num.keys()) + r")\b")
    return pattern.sub(lambda x: word_to_num[x.group()], text)

def lineConverter(strLine): 
    strLine = strLine.replace("one", "o1e")
    strLine = strLine.replace("two", "t2o")
    strLine = strLine.replace("three", "th3ee")
    strLine = strLine.replace("four", "fo4r")
    strLine = strLine.replace("five", "fi5e")
    strLine = strLine.replace("six", "s6x")
    strLine = strLine.replace("seven", "se7en")
    strLine = strLine.replace("eight", "ei8ht")
    strLine = strLine.replace("nine", "ni9e")

    return strLine


print ("Current Directory: " + os.getcwd())

fileName = './input/input.txt'
#fileName = './input/test.txt'

print (fileName)

resultSum = 0
numLines = 0

#helloWorld()

with open(fileName, 'r') as file:
    line = "start"
    while line:
        line = file.readline()
        if line == "":
            break
        line = lineConverter(line)
        
        new_result = re.findall('[0-9]', line)
        resultSum = resultSum + int(new_result[0]) * 10 + int(new_result[-1])
        #print (int(new_result[0]) * 10 + int(new_result[-1]))
        numLines += 1

print ("Summe:" + str(resultSum))
print ("Lines:" + str(numLines))



exit




