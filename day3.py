#!/usr/local/bin/python3

def part1():
    with open('day3.input','r') as f:
        s = f.read().split('\n')
        myList = [list(x) for x in s]
        temp = [str() for c in 'c' * len(myList[0])]
        for pos,val in enumerate(myList):
            for pos2,val2 in enumerate(val):
                temp[pos2] += val2
        gammaRate = ''
        epsilonRate = ''
        for val in temp:
            cnt_1 = val.count('1')
            cnt_0 = val.count('0')
            if cnt_1 > cnt_0:
                gammaRate += '1'
                epsilonRate += '0'
            else:
                gammaRate += '0'
                epsilonRate += '1'
        print('Answer is %d'%(int(gammaRate,2)*int(epsilonRate,2)))

def ogr(pos1,myList):
    temp = ""
    returnList = []
    for pos,val in enumerate(myList):
        temp += val[pos1]
    if temp.count('1') > temp.count('0') or temp.count('1') == temp.count('0'):
        for pos,val in enumerate(myList):
            if val[pos1] == '1':
                returnList.append(val)
    else:
        for pos,val in enumerate(myList):
            if val[pos1] == '0':
                returnList.append(val)
    if pos1 + 1 >= len(myList[0]) or len(returnList) == 1 :
        return returnList
    else:
        return ogr(pos1+1,returnList)

def cor(pos1,myList):
    temp = ""
    returnList = []
    for pos,val in enumerate(myList):
        temp += val[pos1]
    if temp.count('1') < temp.count('0'):
        for pos,val in enumerate(myList):
            if val[pos1] == '1':
                returnList.append(val)
    else:
        for pos,val in enumerate(myList):
            if val[pos1] == '0':
                returnList.append(val)
    if pos1 + 1 >= len(myList[0]) or len(returnList) == 1 :
        return returnList
    else:
        return cor(pos1+1,returnList)

def part2():
    with open('day3.input','r') as f:
        s = f.read().split('\n')
        myList = [list(x) for x in s]
        ogrList = ogr(0,myList)
        corList = cor(0,myList)
        print('Answer is %s'%(int(''.join(ogrList[0]),2)*int(''.join(corList[0]),2)))

if __name__ == '__main__':
    part1()
    part2()