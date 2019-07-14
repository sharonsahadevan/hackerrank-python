import itertools

def combination_replacement(word,value):
    word = word.upper()
    word = sorted(word)
    result = itertools.combinations_with_replacement(word,value)
    for i in result:
        print(''.join(i))
    
           
    
if __name__ == '__main__':
    inputWord =  input().split()
    word =  inputWord[0]
    value = int(inputWord[1])
    combination_replacement(word,value)
    
  






