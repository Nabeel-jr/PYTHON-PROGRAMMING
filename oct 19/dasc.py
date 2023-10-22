d={"c":2,"d":3,"a":4,"b":1}
print(d)
asce=dict(sorted(d.items()))

temp=0
for x in asce:
    for y in asce:
        if asce[x]<asce[y]:
            temp=asce[x]
            asce[x]=asce[y]
            asce[y]=temp
print(asce)


desc=dict(sorted(asce.items(),reverse=True))
print(desc)