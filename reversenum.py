#1) Let input string be 'str[]' and length of string be 'n'
#2) l = 0, r = n-1
#3) While l is smaller than r, do following
#    a) If str[l] is not an alphabetic character, do l++
#    b) Else If str[r] is not an alphabetic character, do r--
#    c) Else swap str[l] and str[r]#

def reverse(str1):
    l1=list(str1)
    n=len(str1)
    l=0
    r=n-1
    while l<r:
        if not l1[l].isalnum():
            l+=1
        elif not l1[r].isalnum():
            r-=1
        else:
            l1[l],l1[r]=l1[r],l1[l]
            l+=1
            r-=1
    return ''.join(l1)

str1="Acd$er123#kjlbv?1@jbkk"
print(str1)
ans =reverse(str1)
print(ans)
