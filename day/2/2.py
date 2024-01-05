import re
import os


print ("Current Directory: " + os.getcwd())

fileName = './2/input.txt'
#fileName = './2/test.txt'

print (fileName)


maxRed = 12
maxGreen = 13
maxBlue = 14

result = 0

numLines = 0

with open(fileName, 'r') as file:
    line = "start"
    while line:
        line = file.readline()
        if line == "":
            break
    
        valid = True

        id = re.findall (r'Game\s(.*):.*', line)
        blue = re.findall (r'.?(\d{1,2}) blue', line)
        blue = list(map(int, blue))
        
        red = re.findall (r'.?(\d{1,2}) red', line)
        red = list(map(int, red))
        
        green = re.findall (r'.?(\d{1,2}) green', line)
        green = list(map(int, green))

        print (id)
        print(blue, red, green)
        if max(blue)>maxBlue : valid = False
        if max(red)>maxRed : valid = False
        if max(green)>maxGreen : valid = False
        
        power = max(red) * max(green) * max(blue)

        result = result + power
        
        numLines += 1


print ("Lines:" + str(numLines))
print ("Result:" + str(result))

