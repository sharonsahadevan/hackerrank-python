import itertools

def combination(word,value):
    word = word.upper()
    word = sorted(word)
    for i in range(1,value+1):
        for item in itertools.combinations(word,i):
            print(''.join(item))
    
           
    
if __name__ == '__main__':
    inputWord =  input().split()
    word =  inputWord[0]
    value = int(inputWord[1])
    combination(word,value)
    
  






