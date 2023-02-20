import keyword
print(keyword.kwlist)
lst = [10,20,30,40,50,60,70,80,90]
lst.remove(10)
print(lst)
lst.pop(2)
print(lst)


s1 = {10,20,30,40,50,60,70}
s2 = {10,20,30,40,50,60}
s3 = {10,20,30,40,50}

print(s2.issubset(s1))
print(s1.difference(s2))