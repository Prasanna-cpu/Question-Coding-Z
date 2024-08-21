

def expand_string(input:str):
    result=""
    i=0

    while i<len(input):
        letter=input[i]
        i+=1

        num_str=""
        while i<len(input) and input[i].isdigit():
            num_str+=input[i]
            i+=1

        num=int(num_str)
        result+=letter*num

    return result

print(expand_string("a5b2"))

