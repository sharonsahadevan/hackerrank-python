import itertools

def permute(word,value):
    word = word.upper()
    word = sorted(word)
    result = itertools.permutations(word,value)
    for item in result:
        print(''.join(item))
    
           
    
if __name__ == '__main__':
    inputWord =  input().split()
    word =  inputWord[0]
    value = int(inputWord[1])
    permute(word,value)
    
  




 