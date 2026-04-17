def merge(l1,l2):
    if(l1 == sorted(l1) and l2 == sorted(l2)):
        a = l1 + l2
        return f"The merged sorted list is {a}"
    else:
        l1.sort()
        l2.sort()
        a1 = l1 + l2
        return f"After sorted and merged list is {a1}"           

l1 = list(map(int,input("Enter l1: ").split()))
l2 = list(map(int,input("Enter l2: ").split()))
print(merge(l1,l2))