def remove(duplicate):
    lst=[]
    for i in duplicate:
        if i not in lst:
            lst.append(i)
    return lst
#drivercode
duplicate=[]
n=int(input("Enter the size:"))
for i in range(0,n):
    print("Enter number at location:",i,":")
    ele=int(input())
    duplicate.append(ele)
print("the original list is:",duplicate)

print("after removing duplicates",remove(duplicate))
