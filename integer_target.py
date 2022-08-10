
print("enter the number of elements of array")
n=int(input())
if(n<=104):
    print("enter an array to perform")
    lst =[]
    for i in range(n):
        ele=int(input())
        lst.append(ele)
    print(lst)
    print("\nenter the target value")
    tgt=int(input())
    for i in range(n):
        for j in range(1,n):
            if lst[i]+lst[j]==tgt:
                break
    print(i,j)
else:
    print("enter values less than 104")    