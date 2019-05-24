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