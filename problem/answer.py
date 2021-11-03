#### ANSWER: START
import random 

def calculateSecond(day,hour,min,sec):
    day = day*24*60*60
    hour = hour*60*60
    min = min*60
    result = day+hour+min+sec
    return result

def reverseString(str) :
    result = str[::-1]
    return result

def calcTwoCharactersFromString(str,ch1,ch2):
    result = 0
    for i in str:   
        if i == ch1:
            result +=1
    for i in str:
        if i == ch2:
            result +=1
    return result

def calcTwoCharactersFromStringV2(str,ch1,ch2):
    result = 0
    if ch1 == ch2:
        return -1
    else:
        for i in str:   
            if i == ch1:
                result +=1
        for i in str:
            if i == ch2:
                result +=1
    return result    

def calcTwoCharactersFromStringV3(str,list):
    result = 0
    for i in range(len(list)):
        for j in str:
            if j == list[i]:
                result += 1
    return result

def mergeAndSortTwoList(list1,list2):
    result = []
    temp = list1 + list2
    for i in temp:
        if i not in result:
            result.append(i)
    result.sort()
    return result

def mergeAndSortTwoListReverse(list1,list2):
    result = []
    temp = list1 + list2
    for i in temp:
        if i not in result:
            result.append(i)
    result.sort(reverse=True)
    return result

def searchMatchedCharacter(list,ch):
    result = []
    for i in list:
        if i[0] == ch:
            result.append(i)
    result.sort()
    return result

def makeRandomTenIntegers():
    result = []
    cnt = 0
    while True:
        if cnt == 10:
            break
        temp = random.randrange(1,11)
        if temp not in result:
            result.append(temp)
            cnt += 1
    return result

def makeRandomIntegersExtended(start,end):
    result = []
    cnt = 0
    if start<= 0 or end<=0:
        return -1
    elif start==end:
        return -1
    elif start<end:
        return -1
    else:
        while True:
            if cnt == 20:
                break
            temp = random.randrange(end,start+1)
            if temp not in result:
                result.append(temp)
                cnt += 1
    return result
    


#### ANSWER: END

#### Self Scoring : Start ####

TotalScore = 0

try:
    if calculateSecond(1,1,1,2) == 90062:
        TotalScore += 5
        print("[Q01-PASSED.1] Score - ", TotalScore)
    else:
        print("[Q01-failed.1] Score - ", TotalScore)
    if calculateSecond(2,3,4,5) == 183845:
        TotalScore += 5
        print("[Q01-PASSED.2] Score - ", TotalScore)
    else:
        print("[Q01-failed.2] Score - ", TotalScore)
except:
    print("[Q01-failed.except] Score - ", TotalScore)

try:
    if reverseString("Hello World!!") == '!!dlroW olleH':
        TotalScore += 5
        print("[Q02-PASSED.1] Score - ", TotalScore)
    else:
        print("[Q02-failed.1] Score - ", TotalScore)
    if reverseString("Welcome to Hell!!") == '!!lleH ot emocleW':
        TotalScore += 5
        print("[Q02-PASSED.2] Score - ", TotalScore)
    else:
        print("[Q02-failed.2] Score - ", TotalScore)
except:
    print("[Q02-failed.except] Score - ", TotalScore)

try:
    if calcTwoCharactersFromString("You only live once", 'o', 'o') == 6:
        TotalScore += 5
        print("[Q03-PASSED.1] Score - ", TotalScore)
    else:
        print("[Q03-failed.1] Score - ", TotalScore)
    if calcTwoCharactersFromString("You only live once", 'o', 'Y') == 4:
        TotalScore += 5
        print("[Q03-PASSED.2] Score - ", TotalScore)
    else:
        print("[Q03-failed.2] Score - ", TotalScore)
except:
    print("[Q03-failed.except] Score - ", TotalScore)

try: 
    if calcTwoCharactersFromStringV2("You only live once", 'o', 'o') == -1:
        TotalScore += 5
        print("[Q04-PASSED.1] Score - ", TotalScore)
    else:
        print("[Q04-failed.1] Score - ", TotalScore)
    if calcTwoCharactersFromStringV2("You only live once", 'o', 'Y') == 4:
        TotalScore += 5
        print("[Q04-PASSED.2] Score - ", TotalScore)
    else:
        print("[Q04-failed.2] Score - ", TotalScore)
except:
    print("[Q04-failed.except] Score - ", TotalScore)

try:
    if calcTwoCharactersFromStringV3("You only live once", ['a', 'o', 'o']) == 6:
        TotalScore += 10
        print("[Q05-PASSED] Score - ", TotalScore)
    else:
        print("[Q05-failed.try] Score - ", TotalScore)
except:
    print("[Q05-failed.except] Score - ", TotalScore)

try:
    if mergeAndSortTwoList([1,1,2,3,5,8,13,24,34,55], [1,1,2,3,4,5,6,7,8,9,10,11,12]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 24, 34, 55]:
        TotalScore += 10
        print("[Q06-PASSED] Score - ", TotalScore)
    else:
        print("[Q06-failed.except] try - ", TotalScore)
except:
    print("[Q06-failed.except] Score - ", TotalScore)

try: 
    if mergeAndSortTwoListReverse([1,1,2,3,5,8,13,24,34,55], [1,1,2,3,4,5,6,7,8,9,10,11,12]) == [55, 34, 24, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]:
        TotalScore += 10
        print("[Q07-PASSED] Score - ", TotalScore)
    else:
        print("[Q07-failed.try] Score - ", TotalScore)
except:
    print("[Q07-failed.except] Score - ", TotalScore)

try:
    kingdoms = ['Bacteria', 'Protozoa','Chromista','Plantae','Fungi','Animalia']
    if searchMatchedCharacter(kingdoms, 'P') == ['Plantae', 'Protozoa']:
        TotalScore += 10
        print("[Q08-PASSED] Score - ", TotalScore)
    else:
        print("[Q08-failed.try] Score - ", TotalScore)
except:
    print("[Q08-failed.except] Score - ", TotalScore)

try:
    examResult = makeRandomTenIntegers()
    examResult.sort()
    if examResult == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        TotalScore += 10
        print("[Q09-PASSED] Score - ", TotalScore)
    else:
        print("[Q09-failed.try] Score - ", TotalScore)
except:
    print("[Q09-failed.except] Score - ", TotalScore)

try:
    examResult = makeRandomIntegersExtended(20,1)
    examResult.sort()
    if examResult == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]:
        TotalScore += 10
        print("[Q10-PASSED] Score - ", TotalScore)
    else:
        print("[Q10-failed.try] Score - ", TotalScore)
except:
    print("[Q10-failed.except] Score - ", TotalScore)

#### Self Scoring : End ####

print("==>> FINAL SCORE: ", TotalScore)
