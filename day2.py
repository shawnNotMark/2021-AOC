#!/usr/local/bin/python3

def part1():
    with open('./day2.input','r') as f: 
        start_h = 0
        start_v = 0
        s = f.read()
        myList = s.split('\n')
        forwardTotal = sum([int(x.split(' ')[1]) for x in myList if x.split(' ')[0] in ['forward']])
        downTotal = sum([int(x.split(' ')[1]) for x in myList if x.split(' ')[0] in ['down']])
        upTotal = sum([int(x.split(' ')[1]) for x in myList if x.split(' ')[0] in ['up']])
        answer = forwardTotal * (downTotal-upTotal)
        print ('Answer is %d'%answer)

def part2():
    with open('./day2.input','r') as f: 
        start_h = 0
        start_v = 0
        aim = 0
        s = f.read()
        myList = [x.split(' ') for x in s.split('\n')]
        for x in myList:
            if x[0] == 'forward':
                start_h += int(x[1])
                start_v += aim * int(x[1])
            elif x[0] == 'down':
                aim += int(x[1])
            elif x[0] == 'up':
                aim -= int(x[1])
            else:
                print('did not match x %s'%x)
        answer = start_h*start_v
        print('Answer is %d'%answer)

if __name__ == '__main__':
    part1()
    part2()

