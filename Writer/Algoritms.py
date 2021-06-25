from collections import Counter
import DataBase
import codecs
import matplotlib.pyplot as plt
from datetime import datetime, date, time
from matplotlib import rc


from matplotlib.ticker import NullFormatter
font = {'family': 'Arial',
        'weight': 'normal',
        'size': 14}

ignoredWords = ["the","a","of","on","for","in","out", "at", "for"]
total_count = dict()

def updateIgnoredWords(name):

    for i in DataBase.getStyle(name):
        ignoredWords.append(i[0])

def countOfWords(path):
    with codecs.open(path, 'r', encoding="utf-8") as lines:
        text = lines.readlines()
        w = 1
        if (text[0]):
            for i in text[0]:
                if (i == ' '):
                    w += 1
        lines.close()
        return w




def indexCoolManual(path):
    lines = open(path, 'r', encoding="utf-8")
    text = lines.readlines()
    l = 0
    w = 1
    se = 0
    if (text[0]):
        for i in text[0]:
            if (i.isalpha()):
                l += 1
            elif (i == ' '):
                w += 1
            elif (i == '?' or i == '!' or i == '.'):
                se += 1

        L = float(l / w * 100)
        S = float(se / w * 100)
        index = round((float)(0.0588 * L - 0.296 * S - 15.8))
        lines.close()
        return index




def productiv(startTime, endTime, diference):
    totalTime = int((endTime - startTime).total_seconds())
    return (diference / totalTime) * 100


def tovtologic(path):
    lines = open(path, 'r', encoding="utf-8")
    text = lines.readlines()
    myDict = (Counter([''.join(filter(str.isalpha, x.lower())) for x in text[0].split() if ''.join(filter(str.isalpha, x.lower()))]))


    myDict = dict(sorted(myDict.items(), key=lambda item: item[1], reverse= True))

    for i in ignoredWords:
        if i in myDict:
            del myDict[i]

    names = list(myDict.keys())[:5]
    values = list(myDict.values())[:5]

    fig, axs = plt.subplots()
    axs.bar(names, values)
    fig.suptitle('Tovtologic gisto')

    plt.show()
    return values[0]

def setProd(prodArr, name):
        try:
            present = prodArr[-1]
            past = prodArr[-2]
            if(present[0] > past[0]):
                return "Your productive has incresed\n well done!"
            elif(present[0] < past[0]):
                 return"Your productive has decrease \n don't worry it's ok"
            else:
                return "Your productive has not changed"
        except:
            return "Your productiv was added"

def setTov(tovArr, name):
        try:
            present = tovArr[-1]
            past = tovArr[-2]
            if(present[0] > past[0]):
                return f"Your tovtologic has incresed \n well {name} !"
            elif(present[0] < past[0]):
                 return f"Your tovtologic has decrease \n don't worry it's ok"
            else:
                return "Your tovtologic has not changed"
        except:
            return "Your tovtologic was added"

def setGrade(gradeArr, name):
        try:
            present = gradeArr[-1]
            past = gradeArr[-2]
            if(present[0] > past[0]):
                return "Your grade has incresed \n well done!"
            elif(present[0] < past[0]):
                 return"Your grade has decrease \n don't worry it's ok"
            else:
                return "Your grade has not changed"
        except:
            return "Your grade was added"


def ShowGrafics(filename, name):
    gradeArr = DataBase.getGrade(filename)
    tovArr = DataBase.getTov(filename)
    prodArr = DataBase.getProd(filename)

    plt.plot(gradeArr, 'g')
    plt.title("Grade ")
    plt.xlabel(f'{setGrade(gradeArr, name)}', color='red')
    plt.subplots_adjust(bottom=0.15)
    plt.grid(True)
    plt.show()


    plt.plot(tovArr, c="g")
    plt.title("Tovtologic")
    plt.xlabel(f'{setTov(tovArr, name)}', color='red')
    plt.subplots_adjust(bottom=0.15)
    plt.show()
    plt.grid(True)

    plt.plot(prodArr,'b')
    plt.title("Productive")
    plt.xlabel(f'{setProd(prodArr, name)}', color='red')
    plt.subplots_adjust(bottom=0.15)
    plt.grid(True)

    plt.show()


#ShowGrafics("D:/DimonCource/MytestFile.txt")