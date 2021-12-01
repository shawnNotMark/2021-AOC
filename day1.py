#part 1
def part1():
    with open('./day1.input','r') as f: 
        s = f.read()
        myList = s.split('\n')
        myList = [int(x) for x in myList]
        newList = [y for x,y in enumerate(myList) if y > myList[x-1] ]
        print('Answer for part 1 is: %d'%len(newList))

def part2():
    with open('./day1.input','r') as f: 
        s = f.read()
        myList = s.split('\n')
        myList = [int(x) for x in myList]
        slidingList = [y+myList[x+1]+myList[x+2] for x,y in enumerate(myList) if x+1 < len(myList) and x+2 < len(myList)]
        newList = [y for x,y in enumerate(slidingList) if int(y) > int(slidingList[x-1]) ]
        print('Answer for part 2 is: %d'%len(newList))

if __name__ == '__main__':
    part1()
    part2()
    