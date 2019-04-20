s = "This is a simple string"

char = list(s)

print(char)
converted_list = []
for i in range(0, len(char)):
    if(char[i].isupper()):
        converted_list.append(char[i].lower())
    elif(char[i].islower()):
        converted_list.append(char[i].upper())
    elif(char[i] == ' '):
        converted_list.append(char[i])

delimiter = ''
converted_back_to_sting = delimiter.join(converted_list)
print(converted_back_to_sting)
