# def remove_vowels(s:str):
#     vowels="aeiouAEIOU"
#
#     result=[]
#     i=0
#
#     while i<len(s):
#         if s[i] in vowels:
#             j = i
#             while j < len(s) and s[j] in vowels:
#                 j += 1
#             # Ignore the whole sequence of consecutive vowels
#             if j > i + 1:
#                 i = j
#             else:
#                 result.append(s[i])
#                 i += 1
#
#         else:
#             result.append(s[i])
#             i += 1
#
#     return ''.join(result)

def is_vowel(c):
    lowercase = c.lower()
    return lowercase == 'a' or lowercase == 'e' or lowercase == 'i' or lowercase == 'o' or lowercase == 'u'

def remove_vowels(input_str):
    result = ""

    for c in input_str:
        if not is_vowel(c):
            result += c

    return result

