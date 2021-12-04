#!/usr/local/bin/python3

_numbers = [83,69,34,46,30,23,19,75,22,37,89,78,32,39,11,44,95,43,26,48,84,53,94,88,18,40,62,35,27,42,15,2,91,20,4,64,99,71,54,97,52,36,28,7,74,45,70,86,98,1,61,50,68,6,77,8,57,47,51,72,65,3,49,24,79,13,17,92,41,80,63,67,82,90,55,0,10,93,38,21,59,73,33,31,9,76,5,66,16,58,85,87,12,29,25,14,96,56,60,81]

def checkCard(myList):
    #check horizontal
    for card in myList:
        for row in card:
            if all(x=='' for x in row):
                print ('match on row')
                print (card)
                print ('*'*16)
                return card
    #check vertical
    for card in myList:
        for column in zip(*card):
            if all(x==''for x in column):
                print ('match on column')
                print (card)
                print ('*'*16)
                return card
    return None

def checkCard2(myList,val):
    #check horizontal
    for card in myList:
        for row in card:
            if all(x=='' for x in row):
                print ('match on row')
                print (card)
                print (val)
                print ('*'*16)
                myList.remove(card)
    #check vertical
    for card in myList:
        for column in zip(*card):
            if all(x==''for x in column):
                print ('match on column')
                print (card)
                print (val)
                print ('*'*16)
                myList.remove(card)
    return myList

def part1():
    with open('./day4.input') as f:
        lines = list(f)
        lines = [x.strip() for x in lines if x.strip() != '']
    numbers = lines.pop(0).strip().split(',')
    card_list = [[[z for z in y.split(' ') if z != ''] for y in lines[x:x+5]] for x in range(0, len(lines),5)]
    for pos,val in enumerate(numbers):
        for card in card_list:
            for row in card:
                if val in row:
                    row[row.index(val)] = ''
        if pos >= 4:
            winner = checkCard(card_list)
            if winner:
                print('We have a winner')
                print(pos)
                print ('The answer is %d'%(sum([sum([int(y) for y in x if y != '']) for x in winner])*int(val)))
                break

def part2():
    #add it manually from the last one cuz i'm lazy
    with open('./day4.input') as f:
        lines = list(f)
        lines = [x.strip() for x in lines if x.strip() != '']

    numbers = lines.pop(0).strip().split(',')
    card_list = [[[z for z in y.split(' ') if z != ''] for y in lines[x:x+5]] for x in range(0, len(lines),5)]
    for pos,val in enumerate(numbers):
        for card in card_list:
            for row in card:
                if val in row:
                    row[row.index(val)] = ''
        if pos >= 4:
            card_list = checkCard2(card_list,val)
            print("Length of new card list is %d"%len(card_list))

           
if __name__ == '__main__':
    part1()
    part2()




