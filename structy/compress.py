def compress(s):

#   this is technically O(n^2) since we run through the while loop n times 
#   and strings are immutable in python 

#   s += '!'
#   i = 0 
#   j = 0 
#   rv = ''
#   while j < len(s):
#     if s[i] == s[j]: 
#       j += 1 
#     else: 
#       num = str(j-i)
#       if num == '1': 
#         rv += (s[i])
#       else: rv += (num + s[i])
#       i = j 
#   return rv 

#   this version is o(n) since we use a list 

    s += '!'
    i = 0 
    j = 0 
    rv = []
    while j < len(s): 
        if s[i] == s[j]:
            j += 1 
        else: 
            num = str(j-i)
            if num == '1': 
                rv.append(s[i])
            else: 
                rv.append(num)
                rv.append(s[i])
            i = j 
    return ''.join(rv)



assert compress('ccaaatsss') == '2c3at3s'
assert compress('ssssbbz') == '4s2bz'
assert compress('ppoppppp') == '2po5p'