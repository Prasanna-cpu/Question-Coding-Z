def print_pattern(string:str):
    length=len(string)

    for i in range(length):
        line=[" "]*length

        line[i]=string[i]
        line[length-i-1]=string[length-i-1]


        print("".join(line))

print(print_pattern("123456"))
