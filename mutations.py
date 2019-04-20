def mutate_string(string, position, character):
    converted_string = list(string)
    converted_string[position] = character
    delimiter = ''
    mutated_string = delimiter.join(converted_string)
    return mutated_string


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
