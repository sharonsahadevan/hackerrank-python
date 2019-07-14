def product(firstList,secondList):
    output = []
    for x in firstList:
        for y in secondList:
            output.append((x,y))
    
    for i in output:
        print(i,end='')
    


if __name__ == '__main__':
    firstList =  list(map(int,input().split()))
    secondList =  list(map(int,input().split()))
    product(firstList,secondList)


 